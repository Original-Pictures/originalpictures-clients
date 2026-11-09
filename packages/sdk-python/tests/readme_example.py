"""Strictly typechecked companion to the public README upload example."""

from originalpictures import Client, CreateUploadRequest


def upload_example(client: Client) -> object:
    body: CreateUploadRequest = {
        "byte_length": 12,
        "declared_media_type": "image/png",
        "mode": "single",
        "sha256": "0" * 64,
    }
    return client.create_upload(body=body)
