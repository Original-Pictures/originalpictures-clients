"""Non-secret profile configuration and OS keyring credential storage."""

from __future__ import annotations

import json
import os
import re
import stat
import tempfile
from collections.abc import Mapping, MutableMapping
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol
from urllib.parse import urlsplit

import keyring
from platformdirs import PlatformDirs

DEFAULT_API_URL = "https://api.originalpictures.com"
DEFAULT_PROFILE = "default"
MAX_CONFIG_BYTES = 256 * 1024
_PROFILE_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,63}$")


class ConfigurationFailure(ValueError):
    """Local configuration is absent, unsafe, or invalid."""


class CredentialBackend(Protocol):
    def get_password(self, service_name: str, username: str) -> str | None: ...

    def set_password(self, service_name: str, username: str, password: str) -> None: ...

    def delete_password(self, service_name: str, username: str) -> None: ...


@dataclass(frozen=True)
class ResolvedProfile:
    name: str
    api_url: str
    api_key: str | None
    credential_source: str | None


class ConfigStore:
    """Read profile settings from platformdirs and credentials from keyring."""

    service_name = "originalpictures-cli"

    def __init__(
        self,
        *,
        config_dir: Path | None = None,
        credential_backend: CredentialBackend | None = None,
        environ: Mapping[str, str] | None = None,
    ) -> None:
        platform_dir = PlatformDirs("Original Pictures", "Original Pictures").user_config_path
        self.config_dir = config_dir or platform_dir
        self.path = self.config_dir / "config.json"
        self._credentials = credential_backend or keyring
        self._environ = environ if environ is not None else os.environ

    @property
    def default_profile(self) -> str:
        return validate_profile_name(self._environ.get("ORIGINALPICTURES_PROFILE", DEFAULT_PROFILE))

    def resolve(self, *, profile: str | None = None, api_url: str | None = None) -> ResolvedProfile:
        name = validate_profile_name(profile or self.default_profile)
        data = self._load()
        profiles = data.get("profiles", {})
        if not isinstance(profiles, dict):
            raise ConfigurationFailure("configuration profiles must be an object")
        profile_data = profiles.get(name, {})
        if not isinstance(profile_data, dict):
            raise ConfigurationFailure(f"profile {name!r} is malformed")
        configured_url = profile_data.get("api_url", DEFAULT_API_URL)
        env_url = self._environ.get("ORIGINALPICTURES_API_URL")
        resolved_url = validate_api_url(api_url or env_url or configured_url)

        env_key = self._environ.get("ORIGINALPICTURES_API_KEY")
        if env_key:
            return ResolvedProfile(name, resolved_url, _validate_api_key(env_key), "environment")
        try:
            stored_key = self._credentials.get_password(self.service_name, name)
        except Exception as error:  # keyring backends expose platform-specific exceptions
            raise ConfigurationFailure("the operating-system keyring is unavailable") from error
        if stored_key:
            return ResolvedProfile(name, resolved_url, _validate_api_key(stored_key), "keyring")
        return ResolvedProfile(name, resolved_url, None, None)

    def set_api_url(self, profile: str, api_url: str) -> ResolvedProfile:
        name = validate_profile_name(profile)
        validated_url = validate_api_url(api_url)
        data = self._load()
        profiles = data.setdefault("profiles", {})
        if not isinstance(profiles, dict):
            raise ConfigurationFailure("configuration profiles must be an object")
        profiles[name] = {"api_url": validated_url}
        self._save(data)
        return ResolvedProfile(name, validated_url, None, None)

    def set_api_key(self, profile: str, api_key: str) -> None:
        name = validate_profile_name(profile)
        validated_key = _validate_api_key(api_key)
        try:
            self._credentials.set_password(self.service_name, name, validated_key)
        except Exception as error:
            raise ConfigurationFailure(
                "the operating-system keyring rejected the credential"
            ) from error

    def delete_api_key(self, profile: str) -> bool:
        name = validate_profile_name(profile)
        try:
            if self._credentials.get_password(self.service_name, name) is None:
                return False
            self._credentials.delete_password(self.service_name, name)
        except Exception as error:
            raise ConfigurationFailure(
                "the operating-system keyring could not remove the credential"
            ) from error
        return True

    def list_profiles(self) -> list[dict[str, object]]:
        data = self._load()
        profiles = data.get("profiles", {})
        if not isinstance(profiles, dict):
            raise ConfigurationFailure("configuration profiles must be an object")
        names = sorted(set(profiles) | {self.default_profile})
        result: list[dict[str, object]] = []
        for name in names:
            resolved = self.resolve(profile=name)
            result.append(
                {
                    "api_url": resolved.api_url,
                    "credential_configured": resolved.api_key is not None,
                    "credential_source": resolved.credential_source,
                    "name": name,
                }
            )
        return result

    def _load(self) -> MutableMapping[str, object]:
        if not self.path.exists():
            return {"profiles": {}}
        if self.path.is_symlink():
            raise ConfigurationFailure("refusing to read a symlinked configuration file")
        file_mode = stat.S_IMODE(self.path.stat().st_mode)
        if file_mode & 0o077:
            raise ConfigurationFailure(
                "configuration permissions must not allow group/other access"
            )
        if self.path.stat().st_size > MAX_CONFIG_BYTES:
            raise ConfigurationFailure("configuration file exceeds the 256 KiB limit")
        try:
            value = json.loads(self.path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as error:
            raise ConfigurationFailure("configuration file is not valid UTF-8 JSON") from error
        if not isinstance(value, dict):
            raise ConfigurationFailure("configuration root must be an object")
        return value

    def _save(self, data: Mapping[str, object]) -> None:
        self.config_dir.mkdir(mode=0o700, parents=True, exist_ok=True)
        try:
            os.chmod(self.config_dir, 0o700)
            with tempfile.NamedTemporaryFile(
                mode="w",
                encoding="utf-8",
                dir=self.config_dir,
                prefix=".config-",
                suffix=".json",
                delete=False,
            ) as temporary:
                json.dump(
                    data, temporary, ensure_ascii=False, separators=(",", ":"), sort_keys=True
                )
                temporary.write("\n")
                temporary.flush()
                os.fsync(temporary.fileno())
                temporary_path = Path(temporary.name)
            os.chmod(temporary_path, 0o600)
            os.replace(temporary_path, self.path)
        except OSError as error:
            raise ConfigurationFailure("configuration could not be written securely") from error


def validate_profile_name(value: str) -> str:
    if not _PROFILE_RE.fullmatch(value):
        raise ConfigurationFailure(
            "profile name must be 1-64 letters, digits, dots, underscores, or hyphens"
        )
    return value


def validate_api_url(value: object) -> str:
    if not isinstance(value, str):
        raise ConfigurationFailure("API URL must be a string")
    parsed = urlsplit(value)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ConfigurationFailure("API URL must be an absolute http(s) URL")
    if parsed.username or parsed.password or parsed.query or parsed.fragment:
        raise ConfigurationFailure("API URL must not contain credentials, a query, or a fragment")
    return value.rstrip("/")


def _validate_api_key(value: str) -> str:
    stripped = value.strip()
    if not stripped or len(stripped) > 4096 or any(char.isspace() for char in stripped):
        raise ConfigurationFailure("API credential must be 1-4096 non-whitespace characters")
    return stripped


__all__ = [
    "ConfigurationFailure",
    "ConfigStore",
    "DEFAULT_API_URL",
    "DEFAULT_PROFILE",
    "ResolvedProfile",
    "validate_api_url",
    "validate_profile_name",
]
