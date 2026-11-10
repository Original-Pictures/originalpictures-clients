// GENERATED FILE — do not edit by hand.
// Source: packages/contracts/openapi/openapi.yaml
// Regenerate with: pnpm contracts:generate

export const PUBLIC_API_OPENAPI_SHA256 = "dae3f9e07fda334eaeb7de8e2769869fd4074f4594501fc5b0eeab91b0bf9609"; // gitleaks:allow — deterministic public contract digest
export const PUBLIC_API_VERSION = "1.0.0";

export const PUBLIC_API_OPERATIONS = [
  {
    "operationId": "getHealthz",
    "method": "GET",
    "path": "/healthz",
    "audience": "public-system",
    "securityAlternatives": [],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getDatabaseHealth",
    "method": "GET",
    "path": "/healthz/db",
    "audience": "public-system",
    "securityAlternatives": [],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getReadyz",
    "method": "GET",
    "path": "/readyz",
    "audience": "public-system",
    "securityAlternatives": [],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getGovernanceReadyz",
    "method": "GET",
    "path": "/readyz/governance",
    "audience": "public-system",
    "securityAlternatives": [],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "listApiKeys",
    "method": "GET",
    "path": "/v1/api-keys",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "createApiKey",
    "method": "POST",
    "path": "/v1/api-keys",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "201",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "revokeApiKey",
    "method": "DELETE",
    "path": "/v1/api-keys/{api_key_id}",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getApiKey",
    "method": "GET",
    "path": "/v1/api-keys/{api_key_id}",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getApiKeyRestrictions",
    "method": "GET",
    "path": "/v1/api-keys/{api_key_id}/restrictions",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "setApiKeyRestrictions",
    "method": "PUT",
    "path": "/v1/api-keys/{api_key_id}/restrictions",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getApiKeyRetention",
    "method": "GET",
    "path": "/v1/api-keys/{api_key_id}/retention",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "setApiKeyRetention",
    "method": "PUT",
    "path": "/v1/api-keys/{api_key_id}/retention",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "rotateApiKey",
    "method": "POST",
    "path": "/v1/api-keys/{api_key_id}/rotate",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "201",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "cancelApiKeyRotation",
    "method": "POST",
    "path": "/v1/api-keys/{api_key_id}/rotation/cancel",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "completeApiKeyRotation",
    "method": "POST",
    "path": "/v1/api-keys/{api_key_id}/rotation/complete",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getApiKeySigningProfile",
    "method": "GET",
    "path": "/v1/api-keys/{api_key_id}/signing-profile",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "setApiKeySigningProfile",
    "method": "PUT",
    "path": "/v1/api-keys/{api_key_id}/signing-profile",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "listApiKeyScopes",
    "method": "GET",
    "path": "/v1/api-keys/scopes",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "listApiRequestLogs",
    "method": "GET",
    "path": "/v1/api-request-logs",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "summarizeApiRequestLogs",
    "method": "GET",
    "path": "/v1/api-request-logs/summary",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "listAssets",
    "method": "GET",
    "path": "/v1/assets",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getAsset",
    "method": "GET",
    "path": "/v1/assets/{asset_id}",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getAssetDetail",
    "method": "GET",
    "path": "/v1/assets/{asset_id}/detail",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "createAssetDownload",
    "method": "POST",
    "path": "/v1/assets/{asset_id}/download",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "createAssetPreview",
    "method": "POST",
    "path": "/v1/assets/{asset_id}/preview",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "redeemAssetPreview",
    "method": "GET",
    "path": "/v1/assets/{asset_id}/preview/{capability}",
    "audience": "tenant",
    "securityAlternatives": [],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "image/jpeg"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getBillingAccount",
    "method": "GET",
    "path": "/v1/billing/account",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "listBillingCharges",
    "method": "GET",
    "path": "/v1/billing/charges",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "createBillingCheckoutIntent",
    "method": "POST",
    "path": "/v1/billing/checkout-intents",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "201",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "502",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "listBillingInvoices",
    "method": "GET",
    "path": "/v1/billing/invoices",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getBillingPlans",
    "method": "GET",
    "path": "/v1/billing/plans",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "createBillingPortalIntent",
    "method": "POST",
    "path": "/v1/billing/portal-intents",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "201",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "502",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getBillingPricing",
    "method": "GET",
    "path": "/v1/billing/pricing",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "createBillingQuote",
    "method": "POST",
    "path": "/v1/billing/quotes",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getBillingWallet",
    "method": "GET",
    "path": "/v1/billing/wallet",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "setBillingWalletSettings",
    "method": "PUT",
    "path": "/v1/billing/wallet/settings",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getCapabilities",
    "method": "GET",
    "path": "/v1/capabilities",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "createCaptureAdmissionChallenge",
    "method": "POST",
    "path": "/v1/capture-admission-challenges",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "201",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "listCaptureAdmissions",
    "method": "GET",
    "path": "/v1/capture-admissions",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "createCaptureAdmission",
    "method": "POST",
    "path": "/v1/capture-admissions",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "201",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getCaptureAdmission",
    "method": "GET",
    "path": "/v1/capture-admissions/{capture_admission_id}",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "304",
        "contentTypes": []
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "listCaptureIdentities",
    "method": "GET",
    "path": "/v1/capture-identities",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "createCaptureIdentity",
    "method": "POST",
    "path": "/v1/capture-identities",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "201",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getCaptureIdentity",
    "method": "GET",
    "path": "/v1/capture-identities/{capture_identity_id}",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "304",
        "contentTypes": []
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "revokeCaptureIdentity",
    "method": "POST",
    "path": "/v1/capture-identities/{capture_identity_id}/revoke",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "createCaptureIdentityEnrollment",
    "method": "POST",
    "path": "/v1/capture-identity-enrollments",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "201",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getConnectCatalog",
    "method": "GET",
    "path": "/v1/connect-catalog",
    "audience": "public-system",
    "securityAlternatives": [],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getCreatorDisclosurePolicy",
    "method": "GET",
    "path": "/v1/creator-disclosure-policy",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "updateCreatorDisclosurePolicy",
    "method": "PUT",
    "path": "/v1/creator-disclosure-policy",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "listCreatorIdentities",
    "method": "GET",
    "path": "/v1/creator-identities",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "createCreatorIdentity",
    "method": "POST",
    "path": "/v1/creator-identities",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "201",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getCreatorIdentity",
    "method": "GET",
    "path": "/v1/creator-identities/{creator_identity_id}",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "discloseCreatorIdentity",
    "method": "GET",
    "path": "/v1/creator-identities/{creator_identity_id}/disclosure",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "withdrawCreatorIdentity",
    "method": "POST",
    "path": "/v1/creator-identities/{creator_identity_id}/withdraw",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getDeveloperOnboarding",
    "method": "GET",
    "path": "/v1/developer-onboarding",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "listDisclosureEvents",
    "method": "GET",
    "path": "/v1/disclosures/events",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "createDisclosureEvent",
    "method": "POST",
    "path": "/v1/disclosures/events",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "201",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getDisclosurePolicies",
    "method": "GET",
    "path": "/v1/disclosures/policies",
    "audience": "public-system",
    "securityAlternatives": [],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "submitFeedback",
    "method": "POST",
    "path": "/v1/feedback",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "201",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "queryGovernanceAudit",
    "method": "GET",
    "path": "/v1/governance/audit",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "listGovernanceDeletions",
    "method": "GET",
    "path": "/v1/governance/deletions",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "createGovernanceDeletion",
    "method": "POST",
    "path": "/v1/governance/deletions",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "202",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getGovernanceDeletion",
    "method": "GET",
    "path": "/v1/governance/deletions/{deletion_id}",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "listGovernanceExports",
    "method": "GET",
    "path": "/v1/governance/exports",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "createGovernanceExport",
    "method": "POST",
    "path": "/v1/governance/exports",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "202",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getGovernanceExport",
    "method": "GET",
    "path": "/v1/governance/exports/{export_id}",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "listGovernanceLegalHolds",
    "method": "GET",
    "path": "/v1/governance/legal-holds",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "releaseHistorySnapshot",
    "method": "DELETE",
    "path": "/v1/history/snapshots",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "204",
        "contentTypes": []
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "listIdentityCredentials",
    "method": "GET",
    "path": "/v1/identity-credentials",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "listImageProfiles",
    "method": "GET",
    "path": "/v1/image-profiles",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "listJobs",
    "method": "GET",
    "path": "/v1/jobs",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getJob",
    "method": "GET",
    "path": "/v1/jobs/{job_id}",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "cancelJob",
    "method": "POST",
    "path": "/v1/jobs/{job_id}/cancel",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "createMarkingCheck",
    "method": "POST",
    "path": "/v1/marking-checks",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "202",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getMarkingCheck",
    "method": "GET",
    "path": "/v1/marking-checks/{marking_check_id}",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getCurrentUser",
    "method": "GET",
    "path": "/v1/me",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getOverview",
    "method": "GET",
    "path": "/v1/overview",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getPublicVerifyPage",
    "method": "GET",
    "path": "/v1/public/verify-pages/{slug}",
    "audience": "public-system",
    "securityAlternatives": [],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "createPublicCheck",
    "method": "POST",
    "path": "/v1/public/verify-pages/{slug}/checks",
    "audience": "public-system",
    "securityAlternatives": [],
    "executable": true,
    "requestContentTypes": [
      "multipart/form-data"
    ],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "202",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "413",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "415",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getPublicCheck",
    "method": "GET",
    "path": "/v1/public/verify-pages/{slug}/checks/{check_id}",
    "audience": "public-system",
    "securityAlternatives": [],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getPublicVerifyPageLogo",
    "method": "GET",
    "path": "/v1/public/verify-pages/{slug}/logo",
    "audience": "public-system",
    "securityAlternatives": [],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "image/jpeg",
          "image/png",
          "image/webp"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "listReceipts",
    "method": "GET",
    "path": "/v1/receipts",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getSigningReceipt",
    "method": "GET",
    "path": "/v1/receipts/{receipt_id}",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "listRecipes",
    "method": "GET",
    "path": "/v1/recipes",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getRecipe",
    "method": "GET",
    "path": "/v1/recipes/{recipe_id}",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getSharedVerification",
    "method": "GET",
    "path": "/v1/shared-verifications/{token}",
    "audience": "public-system",
    "securityAlternatives": [],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "acceptSigningJob",
    "method": "POST",
    "path": "/v1/sign",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "202",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "402",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "acceptSigningJobBatch",
    "method": "POST",
    "path": "/v1/sign/batch",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "202",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "createUpload",
    "method": "POST",
    "path": "/v1/uploads",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "201",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "abortUpload",
    "method": "POST",
    "path": "/v1/uploads/{upload_id}/abort",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "completeUpload",
    "method": "POST",
    "path": "/v1/uploads/{upload_id}/complete",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "410",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getUsage",
    "method": "GET",
    "path": "/v1/usage",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getVerificationEvidence",
    "method": "GET",
    "path": "/v1/verification-evidence/{verification_id}",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "createVerificationReport",
    "method": "POST",
    "path": "/v1/verification-evidence/{verification_id}/reports",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "202",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "listVerificationShares",
    "method": "GET",
    "path": "/v1/verification-evidence/{verification_id}/shares",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "createVerificationShare",
    "method": "POST",
    "path": "/v1/verification-evidence/{verification_id}/shares",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "201",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getVerificationHistory",
    "method": "GET",
    "path": "/v1/verification-history/{verification_id}",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getVerificationReport",
    "method": "GET",
    "path": "/v1/verification-reports/{report_id}",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "closeVerificationShare",
    "method": "POST",
    "path": "/v1/verification-shares/{share_id}/close",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "listVerifications",
    "method": "GET",
    "path": "/v1/verifications",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "createVerification",
    "method": "POST",
    "path": "/v1/verifications",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "202",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getVerification",
    "method": "GET",
    "path": "/v1/verifications/{verification_id}",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "createVerificationBatch",
    "method": "POST",
    "path": "/v1/verifications/batch",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "202",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getVerifyPage",
    "method": "GET",
    "path": "/v1/verify-pages",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "putVerifyPage",
    "method": "PUT",
    "path": "/v1/verify-pages",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "listWebhookEndpoints",
    "method": "GET",
    "path": "/v1/webhook-endpoints",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "createWebhookEndpoint",
    "method": "POST",
    "path": "/v1/webhook-endpoints",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "201",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "deleteWebhookEndpoint",
    "method": "DELETE",
    "path": "/v1/webhook-endpoints/{endpoint_id}",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "204",
        "contentTypes": []
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getWebhookEndpoint",
    "method": "GET",
    "path": "/v1/webhook-endpoints/{endpoint_id}",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "updateWebhookEndpoint",
    "method": "PATCH",
    "path": "/v1/webhook-endpoints/{endpoint_id}",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "listWebhookDeliveries",
    "method": "GET",
    "path": "/v1/webhook-endpoints/{endpoint_id}/deliveries",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "disableWebhookEndpoint",
    "method": "POST",
    "path": "/v1/webhook-endpoints/{endpoint_id}/disable",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "204",
        "contentTypes": []
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "enableWebhookEndpoint",
    "method": "POST",
    "path": "/v1/webhook-endpoints/{endpoint_id}/enable",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "rotateWebhookEndpointSecret",
    "method": "POST",
    "path": "/v1/webhook-endpoints/{endpoint_id}/rotate-secret",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "completeWebhookEndpointSecretOverlap",
    "method": "POST",
    "path": "/v1/webhook-endpoints/{endpoint_id}/secret-overlap/complete",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "sendWebhookTestEvent",
    "method": "POST",
    "path": "/v1/webhook-endpoints/{endpoint_id}/test",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "202",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getWebhookDelivery",
    "method": "GET",
    "path": "/v1/webhook-endpoints/deliveries/{delivery_id}",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "listWebhookDeliveryAttempts",
    "method": "GET",
    "path": "/v1/webhook-endpoints/deliveries/{delivery_id}/attempts",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "replayWebhookDelivery",
    "method": "POST",
    "path": "/v1/webhook-endpoints/deliveries/{delivery_id}/replay",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getWebhookEventCatalog",
    "method": "GET",
    "path": "/v1/webhook-endpoints/event-catalog",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "replayWebhookEvent",
    "method": "POST",
    "path": "/v1/webhook-events/{event_id}/replay",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "listWorkflowTemplates",
    "method": "GET",
    "path": "/v1/workflow-templates",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "createWorkflowTemplate",
    "method": "POST",
    "path": "/v1/workflow-templates",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "201",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "deleteWorkflowTemplate",
    "method": "DELETE",
    "path": "/v1/workflow-templates/{template_id}",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "204",
        "contentTypes": []
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "getWorkflowTemplate",
    "method": "GET",
    "path": "/v1/workflow-templates/{template_id}",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "replaceWorkflowTemplate",
    "method": "PUT",
    "path": "/v1/workflow-templates/{template_id}",
    "audience": "tenant",
    "securityAlternatives": [
      [
        "bearerAuth"
      ]
    ],
    "executable": true,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "401",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "403",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "404",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "429",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "receiveClerkWebhook",
    "method": "POST",
    "path": "/webhooks/clerk",
    "audience": "provider-webhook",
    "securityAlternatives": [
      [
        "clerkWebhookSignature"
      ]
    ],
    "executable": false,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "200",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "400",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "413",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "422",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  },
  {
    "operationId": "receiveStripeWebhook",
    "method": "POST",
    "path": "/webhooks/stripe",
    "audience": "provider-webhook",
    "securityAlternatives": [
      [
        "stripeWebhookSignature"
      ]
    ],
    "executable": false,
    "requestContentTypes": [
      "application/json"
    ],
    "responses": [
      {
        "statusCode": "202",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "400",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "409",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "413",
        "contentTypes": [
          "application/json"
        ]
      },
      {
        "statusCode": "503",
        "contentTypes": [
          "application/json"
        ]
      }
    ]
  }
] as const;

export type PublicApiOperation = (typeof PUBLIC_API_OPERATIONS)[number];
export type PublicApiOperationId = PublicApiOperation["operationId"];
export type ExecutablePublicApiOperation = Extract<PublicApiOperation, { executable: true }>;
export type ExecutablePublicApiOperationId = ExecutablePublicApiOperation["operationId"];
export type PublicApiPath = PublicApiOperation["path"];

// Complete generated schema and operation model surface.
export interface AbortUploadResponse {
  "status": UploadStatus;
  "upload_id": string;
}

export interface AiActionResponse {
  "description": string;
  "id": string;
  "kind": "copy" | "deep_link";
  "label": string;
  "maximum_prompt_characters": number | null;
  "over_limit_fallback_action_id": string | null;
  "target": "clipboard" | "cursor" | "claude" | "chatgpt";
  "url_template": string | null;
}

export interface AiDeclarationRequest {
  "digital_source_type": "trainedAlgorithmicMedia" | "compositeWithTrainedAlgorithmicMedia" | "compositeSynthetic";
  "human_oversight_level"?: "human-in-the-loop" | "human-on-the-loop" | "human-out-of-the-loop" | null;
  "models"?: ReadonlyArray<AiModelDisclosureRequest>;
  "software_agent_name": string;
  "software_agent_version"?: string | null;
}

export interface AiDeclaredSigningReceiptEvidenceResponse {
  "ai_declaration": ReceiptAiDeclarationResponse;
  "asset_id": string;
  "bindings": ReceiptBindingSetResponse | SidecarReceiptBindingSetResponse;
  "job_id": string;
  "manifest": ReceiptManifestResponse;
  "output": ReceiptOutputResponse;
  "product": ReceiptProductResponse;
  "published_at": string;
  "schema_version": "op.signing-receipt.ai-declared.v1";
  "signing": ReceiptSigningResponse;
  "validation": ReceiptValidationResponse;
}

export interface AiMarkBlock {
  "declaration": AiDeclarationRequest;
  "type": "ai_mark";
}

export interface AiModelDisclosureRequest {
  "name": string;
  "scientific_domain"?: string | null;
  "version"?: string | null;
}

export interface AiPromptResponse {
  "credential_environment_variable": string;
  "id": string;
  "secret_substitution_allowed": boolean;
  "section_order": ReadonlyArray<string>;
  "template_id": string;
  "title": string;
}

export interface ApiKeyCreateRequest {
  "expires_at"?: string | null;
  "name"?: string | null;
  "preset"?: ApiKeyPreset | null;
  "restrictions"?: ApiKeyRestrictionsRequest | null;
  "retention_mode"?: "1h" | "24h" | "72h" | "retain" | null;
  "scopes"?: ReadonlyArray<string> | null;
  "signing_profile"?: ApiKeySigningProfileDocument | null;
}

export interface ApiKeyListResponse {
  "data": ReadonlyArray<ApiKeyMetadataResponse>;
}

export interface ApiKeyMetadataResponse {
  "created_at": string;
  "display_hint": string;
  "expires_at": string | null;
  "id": string;
  "last_used_at": string | null;
  "name": string | null;
  "restrictions"?: ApiKeyRestrictionsView | null;
  "revoked_at": string | null;
  "rotated_from_id": string | null;
  "rotation"?: ApiKeyRotationResponse | null;
  "scopes": ReadonlyArray<string>;
  "status": ApiKeyStatus;
}

export type ApiKeyPreset = "full_access" | "publishable_disclosure";

export interface ApiKeyRestrictionsRequest {
  "allowed_ip_cidrs"?: ReadonlyArray<string> | null;
  "allowed_origins"?: ReadonlyArray<string> | null;
  "rate_limit_per_minute"?: number | null;
}

export interface ApiKeyRestrictionsResponse {
  "allowed_ip_cidrs": ReadonlyArray<string> | null;
  "allowed_origins"?: ReadonlyArray<string> | null;
  "api_key_id": string;
  "ip_allowlist_available": boolean;
  "rate_limit_per_minute": number | null;
  "version": number;
}

export interface ApiKeyRestrictionsUpdateRequest {
  "allowed_ip_cidrs": ReadonlyArray<string> | null;
  "allowed_origins"?: ReadonlyArray<string> | null;
  "expected_version": number;
  "rate_limit_per_minute": number | null;
}

export interface ApiKeyRestrictionsView {
  "allowed_ip_cidrs": ReadonlyArray<string> | null;
  "allowed_origins"?: ReadonlyArray<string> | null;
  "rate_limit_per_minute": number | null;
  "version": number;
}

export interface ApiKeyRetentionRequest {
  "expected_version": number;
  "retention_mode": "1h" | "24h" | "72h" | "retain";
}

export interface ApiKeyRetentionResponse {
  "api_key_id": string;
  "clock_starts_at": "validated_publication";
  "effective_for": "future_job_admissions";
  "retention_mode": "legacy" | "1h" | "24h" | "72h" | "retain";
  "version": number;
}

export interface ApiKeyRotateRequest {
  "expires_at"?: string | null;
  "overlap_seconds"?: number;
}

export interface ApiKeyRotationResponse {
  "deadline_at": string;
  "peer_id": string;
  "role": ApiKeyRotationRole;
  "started_at": string;
}

export type ApiKeyRotationRole = "outgoing" | "successor";

export interface ApiKeyScopeCatalogResponse {
  "catalog_version": string;
  "groups": ReadonlyArray<ApiKeyScopeGroupResponse>;
  "scopes": ReadonlyArray<ApiKeyScopeDescriptorResponse>;
  "wildcard_supported"?: false;
}

export interface ApiKeyScopeDescriptorResponse {
  "description": string;
  "group": string;
  "label": string;
  "scope": string;
}

export interface ApiKeyScopeGroupResponse {
  "description": string;
  "id": string;
  "label": string;
}

export interface ApiKeySigningProfileDocument {
  "allowed_fingerprint_algorithms"?: ReadonlyArray<string> | null;
  "allowed_media_types"?: ReadonlyArray<string> | null;
  "allowed_recipes"?: ReadonlyArray<string> | null;
  "allowed_watermark_algorithms"?: ReadonlyArray<string> | null;
  "allowed_watermark_strengths"?: ReadonlyArray<"subtle" | "balanced" | "robust"> | null;
  "default_fingerprint_algorithms"?: ReadonlyArray<string> | null;
  "default_recipe"?: string | null;
  "default_watermark_algorithm"?: string | null;
  "default_watermark_strength"?: "subtle" | "balanced" | "robust" | null;
}

export interface ApiKeySigningProfileResponse {
  "api_key_id": string;
  "profile": ApiKeySigningProfileDocument;
  "version": number;
}

export interface ApiKeySigningProfileUpdateRequest {
  "expected_version": number;
  "profile": ApiKeySigningProfileDocument;
}

export type ApiKeyStatus = "active" | "expired" | "revoked" | "rotated";

export interface ApiRequestLogItem {
  "api_key_id": string | null;
  "client_ip": string | null;
  "client_network": string | null;
  "duration_ms": number;
  "method": string;
  "occurred_at": string;
  "reason_code": string | null;
  "request_id": string | null;
  "route": string;
  "status": number;
}

export interface ApiRequestLogPageResponse {
  "best_effort"?: true;
  "data": ReadonlyArray<ApiRequestLogItem>;
  "next_cursor": string | null;
}

export interface ApiRequestLogStatusClasses {
  "client_error": number;
  "redirect": number;
  "server_error": number;
  "success": number;
}

export interface ApiRequestLogSummaryResponse {
  "best_effort"?: true;
  "p50_duration_ms": number | null;
  "p95_duration_ms": number | null;
  "refused": number;
  "since": string;
  "status_classes": ApiRequestLogStatusClasses;
  "total": number;
  "window": SummaryWindow;
}

export type AssetAction = "download" | "preview" | "verify_again" | "request_deletion" | "request_account_export";

export type AssetActionReason = "not_published" | "restricted" | "already_deleted" | "deletion_in_progress" | "legal_hold" | "preview_pending" | "preview_unavailable" | "still_processing";

export interface AssetActionResponse {
  "action": AssetAction;
  "available": boolean;
  "reason": AssetActionReason | null;
}

export interface AssetActivityEventResponse {
  "kind": AssetActivityKind;
  "occurred_at": string;
  "related_id": string | null;
  "related_url": string | null;
}

export type AssetActivityKind = "upload_completed" | "job_started" | "job_completed" | "job_failed" | "published" | "receipt_issued" | "verification_completed" | "preview_derived" | "deletion_requested" | "deletion_completed" | "deletion_failed" | "legal_hold_placed" | "legal_hold_released";

export interface AssetActivityResponse {
  "items": ReadonlyArray<AssetActivityEventResponse>;
  "next_cursor": string | null;
}

export type AssetDeletionState = "requested" | "processing" | "retry_wait" | "blocked_legal_hold" | "completed" | "failed";

export interface AssetDetailResponse {
  "actions": ReadonlyArray<AssetActionResponse>;
  "activity": AssetActivityResponse;
  "as_of": string;
  "asset": AssetHistoryResponse;
  "verification_history": AssetVerificationHistoryResponse;
  "workspace_governance": WorkspaceGovernanceResponse;
}

export interface AssetGovernanceResponse {
  "deletion_state": AssetDeletionState | null;
  "legal_hold_active": boolean;
  "retention"?: AssetRetentionResponse | null;
}

export type AssetHistoryKind = "uninspected" | "image" | "audio" | "video" | "text" | "fonts" | "mlModel" | "documents" | "imageSidecar" | "audioSidecar" | "videoSidecar";

export type AssetHistoryOrigin = "upload" | "capture" | "derived";

export interface AssetHistoryPageResponse {
  "items": ReadonlyArray<AssetHistoryResponse>;
  "next_cursor": string | null;
  "total_count": number;
  "workspace_governance": WorkspaceGovernanceResponse;
}

export interface AssetHistoryResponse {
  "asset_id": string;
  "asset_url": string;
  "byte_length": number | null;
  "created_at": string;
  "display_name": string;
  "download_url": string | null;
  "governance": AssetGovernanceResponse;
  "job": AssetJobResponse | null;
  "kind": AssetHistoryKind;
  "media": AssetMediaResponse;
  "media_type": HistoryMediaType | null;
  "origin": AssetHistoryOrigin;
  "preview_state": AssetPreviewState;
  "publication_id": string | null;
  "receipt_id": string | null;
  "sha256": string | null;
  "status": AssetHistoryStatus;
  "verification": AssetVerificationResponse;
  "verification_id": string | null;
}

export type AssetHistoryStatus = "pending" | "ready" | "processing" | "signed" | "watermarked" | "failed" | "deleted";

export interface AssetJobResponse {
  "created_at": string;
  "error_code": string | null;
  "failed_steps": number;
  "job_id": string;
  "job_url": string;
  "kind": JobKind;
  "recipe_id": string;
  "recipe_version": number;
  "state": JobState;
  "succeeded_steps": number;
  "total_steps": number;
  "updated_at": string;
}

export type AssetMediaFamily = "image" | "audio" | "video" | "text";

export interface AssetMediaResponse {
  "byte_length": number | null;
  "codec_label": string | null;
  "duration_microseconds": number | null;
  "family": AssetMediaFamily | null;
  "frame_rate_denominator": number | null;
  "frame_rate_numerator": number | null;
  "height": number | null;
  "inspected": boolean;
  "media_type": HistoryMediaType | null;
  "width": number | null;
}

export type AssetPreviewState = "available" | "pending" | "unavailable" | "restricted";

export interface AssetResponse {
  "asset_id": string;
  "created_at": string;
  "kind": string;
  "media_type": string | null;
  "publication": PublicationResponse | null;
  "status": string;
}

export interface AssetRetentionClassResponse {
  "data_class": string;
  "delete_after"?: string | null;
  "is_indefinite": boolean;
  "object_count": number;
}

export interface AssetRetentionResponse {
  "classes": ReadonlyArray<AssetRetentionClassResponse>;
  "indefinite_object_count": number;
  "latest_delete_after"?: string | null;
  "object_count": number;
  "soonest_delete_after"?: string | null;
}

export interface AssetVerificationEntryResponse {
  "created_at": string;
  "evidence_url": string;
  "overall": VerificationOverall;
  "validated_at": string;
  "validation_path": string | null;
  "verification_id": string;
  "verification_url": string;
}

export interface AssetVerificationHistoryResponse {
  "items": ReadonlyArray<AssetVerificationEntryResponse>;
  "next_cursor": string | null;
}

export interface AssetVerificationResponse {
  "count": number;
  "latest_overall": VerificationOverall | null;
  "latest_validated_at": string | null;
  "latest_validation_path": ValidationPath | null;
  "latest_verification_id": string | null;
}

export type AttestationKind = "app_attest" | "play_integrity" | "hardware_key_attestation";

export type AudioCodec = "pcm_u8" | "pcm_s16le" | "pcm_s24le" | "pcm_s32le" | "mp3" | "aac_lc";

export interface AudioTrackFacts {
  "bits_per_sample": number;
  "channel_layout": string;
  "channels": number;
  "codec": AudioCodec;
  "codec_profile": string;
  "decoded_byte_length": number;
  "duration_microseconds": number;
  "frame_count": number;
  "sample_count": number;
  "sample_rate_hz": number;
  "stream_index": number;
  "time_base_denominator": number;
  "time_base_numerator": number;
}

export interface AuditEventResponse {
  "action": string;
  "actor_id": string | null;
  "actor_type": string;
  "data_sha256": string | null;
  "event_id": string;
  "occurred_at": string;
  "request_id": string | null;
  "resource_id": string | null;
  "resource_type": string | null;
}

export interface BillingAccountResponse {
  "cancel_at_period_end": boolean;
  "caps": Record<string, unknown>;
  "current_period_end": string | null;
  "current_service_period_end": string | null;
  "current_service_period_start": string | null;
  "id": string;
  "plan": string;
  "plan_display_name": string | null;
  "portal_available": boolean;
  "provider_customer_provisioned": boolean;
  "renewal_at": string | null;
  "status": string;
}

export interface BillingIntentResponse {
  "actionable": boolean;
  "expires_at": string;
  "id": string;
  "mode": "simulation" | "sandbox" | "provider";
  "url": string | null;
}

export interface BillingInvoiceResponse {
  "amount_due": string | null;
  "created_at": string;
  "currency": string | null;
  "hosted_invoice_url": string | null;
  "id": string;
  "number": string | null;
  "period": string;
  "service_period_end": string | null;
  "service_period_start": string | null;
  "status": string | null;
}

export interface BillingInvoicesResponse {
  "items": ReadonlyArray<BillingInvoiceResponse>;
  "next_before": string | null;
}

export type BillingPlanId = "plan_10k" | "plan_50k" | "plan_150k" | "plan_500k" | "payg" | "platform" | "cawg_identity_individual" | "cawg_identity_organisation";

export interface BillingPlanResponse {
  "availability"?: "available" | "on_request" | "on_enrolment";
  "availability_note"?: string | null;
  "billing_model": "subscription" | "metered";
  "checkout_available": boolean;
  "display_name": string;
  "id": BillingPlanId;
  "interval"?: "month" | "year";
  "monthly_assets": number | null;
  "monthly_usd": string;
}

export interface BillingPlansResponse {
  "currency"?: "USD";
  "plans": ReadonlyArray<BillingPlanResponse>;
  "pricing_version": string;
  "provider_mode": "simulation" | "sandbox" | "provider" | null;
}

export interface BindingReceiptEvidenceResponse {
  "asset_id": string;
  "bindings": ReceiptBindingSetResponse;
  "job_id": string;
  "output": ReceiptOutputResponse;
  "product": ReceiptProductResponse;
  "published_at": string;
  "schema_version": "op.binding-receipt.v1";
  "validation": ReceiptValidationResponse;
}

export interface ByteRange {
  "length": number;
  "offset": number;
}

export type C2PAStatusVocabularyVersion = "op.c2pa-status.v1" | "op.c2pa-status.v2";

export interface CancelJobRequest {
  "reason"?: string | null;
}

export interface CanonicalCallResponse {
  "id": string;
  "method": string;
  "path": string;
  "purpose": string;
  "required_scope": string;
}

export interface CapabilityAvailabilityResponse {
  "available": boolean;
  "configured": boolean;
  "state": CapabilityAvailabilityState;
}

export type CapabilityAvailabilityState = "available" | "temporarily_unavailable" | "unavailable";

export interface CapabilityDiscoveryResponse {
  "capture": CaptureCapabilityResponse;
  "contract": ContractCapabilityResponse;
  "media": ReadonlyArray<MediaCapabilityResponse>;
  "recipes": ReadonlyArray<ReviewedRecipeAvailabilityResponse>;
  "schema_version": "op.capability-discovery.v1";
}

export interface CapabilityRecipeResponse {
  "capabilities": ReadonlyArray<PublicRecipeCapability>;
  "display_name": string;
  "recipe_id": string;
  "summary": string;
  "supported_media_types": ReadonlyArray<"application/epub+zip" | "application/onnx" | "application/oxps" | "application/pdf" | "application/vnd.oasis.opendocument.text" | "application/vnd.openxmlformats-officedocument.wordprocessingml.document" | "application/x-jax" | "application/x-keras" | "application/x-mlnet" | "application/x-mxnet" | "application/x-npy" | "application/x-openvino-ir+xml" | "application/x-openvino-weights" | "application/x-pickle" | "application/x-protobuf" | "application/x-pytorch" | "application/x-tensorflow" | "application/x-tensorflow-savedmodel" | "application/x-zip-based" | "application/xhtml+xml" | "application/xml" | "audio/MPA" | "audio/aac" | "audio/flac" | "audio/mp4" | "audio/mpeg" | "audio/wav" | "audio/x-riff-based" | "font/otf" | "image/avif" | "image/gif" | "image/heic" | "image/heic-sequence" | "image/heif" | "image/heif-sequence" | "image/jpeg" | "image/jxl" | "image/png" | "image/svg+xml" | "image/tiff" | "image/webp" | "image/x-adobe-dng" | "image/x-riff-based" | "image/x-tiff-based" | "text/html" | "text/plain" | "text/xml" | "video/mp4" | "video/quicktime" | "video/x-bmff-based" | "video/x-msvideo" | "video/x-riff-based">;
  "version": number;
}

export interface CaptureAdmissionChallengeRequest {
  "capture_identity_id": string;
}

export interface CaptureAdmissionChallengeResponse {
  "capture_identity_id": string;
  "challenge_id": string;
  "challenge_secret": string;
  "expires_at": string;
}

export type CaptureAdmissionDecision = "pass" | "reject";

export interface CaptureAdmissionDetail {
  "admission_policy_version": string;
  "asset_id": string | null;
  "capture_admission_id": string;
  "capture_identity_id": string;
  "capture_policy_id": string;
  "capture_policy_version": string;
  "decided_at": string;
  "decision": CaptureAdmissionDecision;
  "evidence_schema_version": string;
  "failed_gates": ReadonlyArray<PublicCaptureAdmissionReason>;
  "governance_policy_version": string;
  "identity_version_id": string;
  "job_id": string | null;
  "provider_class": CaptureProviderClass;
  "reason": PublicCaptureAdmissionReason;
  "revocation_snapshot_version": string;
  "trust_snapshot_version": string;
  "upload_object_id": string;
  "verifier_version": string;
}

export interface CaptureAdmissionListResponse {
  "items": ReadonlyArray<CaptureAdmissionSummary>;
  "next_cursor": string | null;
}

export interface CaptureAdmissionSubmissionRequest {
  "attestation_kind": AttestationKind;
  "capture_identity_id": string;
  "challenge_id": string;
  "challenge_secret": string;
  "installation_id_sha256": string;
  "sensor_evidence"?: Record<string, unknown> | null;
  "sensor_schema_version"?: string | null;
  "statement": string;
  "upload_object_id": string;
}

export interface CaptureAdmissionSubmissionResponse {
  "capture_admission_id": string;
  "decision": CaptureAdmissionDecision;
  "failed_gates": ReadonlyArray<PublicCaptureAdmissionReason>;
  "job_id": string | null;
  "reason": PublicCaptureAdmissionReason;
}

export interface CaptureAdmissionSummary {
  "asset_id": string | null;
  "capture_admission_id": string;
  "capture_identity_id": string;
  "decided_at": string;
  "decision": CaptureAdmissionDecision;
  "failed_gates": ReadonlyArray<PublicCaptureAdmissionReason>;
  "job_id": string | null;
  "reason": PublicCaptureAdmissionReason;
  "upload_object_id": string;
}

export interface CaptureCapabilityResponse {
  "availability": CapabilityAvailabilityResponse;
}

export interface CaptureIdentityCreationRequest {
  "attestation_kind": AttestationKind;
  "capture_identity_enrollment_id": string;
  "challenge_secret": string;
  "statement": string;
}

export interface CaptureIdentityDetail {
  "capture_identity_id": string;
  "capture_policy_id": string;
  "capture_policy_version": string;
  "enrolled_at": string;
  "evidence_schema_version": string;
  "identity_version": number;
  "identity_version_id": string;
  "last_capture_at": string | null;
  "last_verified_at": string | null;
  "platform": CaptureIdentityPlatform;
  "provider_class": CaptureProviderClass;
  "revocation_snapshot_version": string;
  "revoked_at": string | null;
  "state": CaptureIdentityState;
  "trust_snapshot_version": string;
  "verifier_version": string;
}

export interface CaptureIdentityEnrollmentRequest {
  "platform": CaptureIdentityPlatform;
}

export interface CaptureIdentityEnrollmentResponse {
  "capture_identity_enrollment_id": string;
  "challenge_secret": string;
  "expires_at": string;
}

export interface CaptureIdentityEnrollmentResult {
  "capture_identity_id": string;
  "enrolled_at": string;
  "identity_version": number;
  "identity_version_id": string;
}

export type CaptureIdentityFilterState = "active" | "revoked";

export interface CaptureIdentityListResponse {
  "items": ReadonlyArray<CaptureIdentitySummary>;
  "next_cursor": string | null;
}

export type CaptureIdentityPlatform = "ios" | "android";

export interface CaptureIdentityRevocationResponse {
  "capture_identity_id": string;
  "revocation_id": string;
  "revoked_at": string;
  "schema_version"?: "op.capture-identity-revocation.v1";
  "state"?: "revoked";
}

export type CaptureIdentityState = "active" | "revoked";

export interface CaptureIdentitySummary {
  "capture_identity_id": string;
  "enrolled_at": string;
  "last_capture_at": string | null;
  "last_verified_at": string | null;
  "platform": CaptureIdentityPlatform;
  "provider_class": CaptureProviderClass;
  "revoked_at": string | null;
  "state": CaptureIdentityState;
}

export type CaptureManagementErrorCode = "CAPTURE_ENROLLMENT_NOT_FOUND" | "CAPTURE_CHALLENGE_NOT_FOUND" | "CAPTURE_IDENTITY_NOT_FOUND" | "CAPTURE_ADMISSION_NOT_FOUND" | "CAPTURE_ENROLLMENT_EXPIRED" | "CAPTURE_CHALLENGE_EXPIRED" | "CAPTURE_IDEMPOTENCY_IN_PROGRESS" | "CAPTURE_IDEMPOTENCY_CONFLICT" | "CAPTURE_ENROLLMENT_SECRET_ALREADY_ISSUED" | "CAPTURE_CHALLENGE_SECRET_ALREADY_ISSUED" | "CAPTURE_ENROLLMENT_REPLAY_CONFLICT" | "CAPTURE_ADMISSION_REPLAY_CONFLICT" | "CAPTURE_ENROLLMENT_REJECTED" | "CAPTURE_AUTHORITY_UNAVAILABLE" | "CAPTURE_CURSOR_INVALID" | "CAPTURE_VALIDATION_FAILED";

export interface CaptureManagementErrorResponse {
  "code": CaptureManagementErrorCode;
  "message": string;
  "request_id": string;
  "retryable": boolean;
}

export type CaptureProviderClass = "apple_app_attest" | "google_play_integrity" | "android_key_attestation" | "other";

export interface CawgIdentityBlock {
  "credential_id": string;
  "type": "cawg_identity";
}

export interface CheckoutIntentRequest {
  "amount_usd"?: number | string | null;
  "cancel_url": string;
  "plan"?: BillingPlanId | null;
  "purpose"?: "subscription" | "wallet_top_up";
  "success_url": string;
}

export interface CloseShareRequest {
  "state": "revoked" | "unpublished";
}

export interface CloseShareResponse {
  "share_id": string;
  "state": "revoked" | "unpublished";
}

export interface ColorProfileFacts {
  "byte_length": number;
  "sha256": string;
  "validated"?: true;
}

export interface CommonErrorMeaningResponse {
  "meaning": string;
  "retryable": boolean;
  "status": number;
}

export interface CompletePartRequest {
  "etag": string;
  "part_number": number;
}

export interface CompleteUploadRequest {
  "parts"?: ReadonlyArray<CompletePartRequest>;
}

export interface CompleteUploadResponse {
  "asset_id": string;
  "asset_object_id": string;
  "byte_length": number;
  "sha256": string;
  "status": UploadStatus;
  "upload_id": string;
}

export interface ComponentVersion {
  "name": string;
  "version": string;
}

export interface ConnectCatalogResponse {
  "ai_actions": ReadonlyArray<AiActionResponse>;
  "ai_prompt": AiPromptResponse;
  "api_reference_url": string;
  "authorization_header": string;
  "canonical_calls": ReadonlyArray<CanonicalCallResponse>;
  "clients": ReadonlyArray<ConnectClientResponse>;
  "common_errors": ReadonlyArray<CommonErrorMeaningResponse>;
  "connection_modes": ReadonlyArray<ConnectModeResponse>;
  "documentation_url": string;
  "environment_variables": ReadonlyArray<ConnectEnvironmentVariableResponse>;
  "limits_and_cost": LimitsCostGuidanceResponse;
  "mcp_clients": ReadonlyArray<McpClientResponse>;
  "mcp_feature_groups": ReadonlyArray<McpFeatureGroupResponse>;
  "processing_modes": ReadonlyArray<string>;
  "public_api_origin": string;
  "safety": ReadonlyArray<SafetyStatementResponse>;
  "templates": ReadonlyArray<ConnectTemplateResponse>;
  "version": string;
}

export interface ConnectClientResponse {
  "filename": string;
  "id": string;
  "install_template_id": string;
  "label": string;
  "language": string | null;
  "mode": string;
  "quickstart_template_id": string;
}

export interface ConnectEnvironmentVariableResponse {
  "default": string | null;
  "description": string;
  "name": string;
  "required": boolean;
  "secret": boolean;
}

export interface ConnectModeResponse {
  "description": string;
  "id": string;
  "label": string;
}

export type ConnectTemplatePartKind = "literal" | "environment_variable";

export interface ConnectTemplatePartResponse {
  "kind": ConnectTemplatePartKind;
  "value": string;
}

export interface ConnectTemplateResponse {
  "id": string;
  "kind": "install_command" | "code" | "configuration" | "prompt";
  "media_type": string;
  "parts": ReadonlyArray<ConnectTemplatePartResponse>;
}

export interface ContractCapabilityResponse {
  "api_version": string;
  "digest": string;
  "digest_algorithm": "sha256";
}

export interface CreateReportRequest {
  "format": ReportFormat;
  "include_creator"?: boolean;
}

export interface CreateShareRequest {
  "expires_at"?: string | null;
  "include_attribution"?: boolean;
}

export interface CreateShareResponse {
  "share_id": string;
  "token": string | null;
}

export interface CreateUploadRequest {
  "byte_length": number;
  "declared_media_type": string;
  "filename"?: string | null;
  "mode": UploadMode;
  "parts"?: ReadonlyArray<MultipartPartRequest>;
  "sha256": string;
}

export interface CreateUploadResponse {
  "asset_id": string;
  "expires_at": string;
  "mode": UploadMode;
  "parts"?: ReadonlyArray<PresignedPartResponse>;
  "status": UploadStatus;
  "upload"?: PresignedRequestResponse | null;
  "upload_id": string;
}

export interface CreateVerificationRequest {
  "manifest_object_id"?: string | null;
  "object_id": string;
}

export interface CreateWebhookEndpointRequest {
  "auto_disable_after_failures"?: number;
  "event_catalog_version": CustomerEventCatalogVersion;
  "events": ReadonlyArray<CustomerEventType>;
  "max_concurrency"?: number;
  "rate_limit_per_minute"?: number;
  "url": string;
}

export interface CreatorConsentRequest {
  "captured_at": string;
  "captured_by"?: string | null;
  "notice_version": string;
}

export interface CreatorDisclosurePolicyRequest {
  "brand_name": string;
  "console_disclosure"?: "none" | "attributed" | "name" | "name_and_email";
  "notice_version"?: string | null;
  "share_disclosure"?: "none" | "attributed" | "name";
}

export interface CreatorDisclosurePolicyResponse {
  "brand_name": string;
  "console_disclosure": "none" | "attributed" | "name" | "name_and_email";
  "notice_version"?: string | null;
  "share_disclosure": "none" | "attributed" | "name";
}

export interface CreatorDisclosureResponse {
  "assurance_level": "self_asserted" | "verified";
  "assurance_statement": string;
  "audience": "operator" | "owning_tenant" | "public";
  "commitment"?: Record<string, string> | null;
  "creator_ref"?: string | null;
  "disclosure_state": "disclosed" | "withheld" | "withdrawn" | "erased" | "unavailable";
  "end_user"?: Record<string, unknown> | null;
  "schema_version": "op.creator-disclosure.v1";
  "tenant": Record<string, unknown>;
}

export interface CreatorIdentityCreateRequest {
  "consent": CreatorConsentRequest;
  "email": string;
  "name"?: string | null;
}

export interface CreatorIdentityListResponse {
  "items": ReadonlyArray<CreatorIdentityResponse>;
  "next_cursor"?: string | null;
}

export interface CreatorIdentityResponse {
  "assurance_level": "self_asserted" | "verified";
  "created_at": string;
  "creator_id": string;
  "display_name_present": boolean;
  "erased_at"?: string | null;
  "status": "active" | "withdrawn" | "erased";
  "withdrawn_at"?: string | null;
}

export interface CustomerEventCatalogResponse {
  "catalog_version": CustomerEventCatalogVersion;
  "events": ReadonlyArray<CustomerEventDescriptorResponse>;
  "wildcard_supported"?: false;
}

export type CustomerEventCatalogVersion = "op.customer-events.v1";

export interface CustomerEventDescriptorResponse {
  "description": string;
  "event_type": CustomerEventType;
  "label": string;
}

export type CustomerEventType = "asset.signed" | "asset.watermarked";

export interface DbHealthResponse {
  "status": string;
}

export type DeclaredCredentialsStatus = "valid" | "valid_untrusted" | "invalid" | "absent";

export interface DeclaredOrigin {
  "actions": ReadonlyArray<string>;
  "ai_generated": boolean;
  "claim_generator": string | null;
  "digital_source_type": string | null;
  "signed_at": string | null;
  "signed_by": string | null;
  "software_agent": string | null;
}

export interface DeletionPageResponse {
  "items": ReadonlyArray<DeletionResponse>;
  "next_cursor": string | null;
}

export interface DeletionRequestBody {
  "asset_id"?: string | null;
  "creator_id"?: string | null;
  "scope": "asset" | "user_data" | "creator_identity";
}

export interface DeletionResponse {
  "asset_id"?: string | null;
  "completed_at"?: string | null;
  "created_at"?: string | null;
  "deletion_request_id": string;
  "scope"?: string | null;
  "status"?: string | null;
}

export interface DeveloperOnboardingResponse {
  "api_keys": OnboardingApiKeysResponse;
}

export type DigitalSourceType = "http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia" | "http://cv.iptc.org/newscodes/digitalsourcetype/compositeWithTrainedAlgorithmicMedia" | "http://cv.iptc.org/newscodes/digitalsourcetype/compositeSynthetic" | "http://cv.iptc.org/newscodes/digitalsourcetype/humanEdits" | "http://c2pa.org/digitalsourcetype/empty";

export interface DisclosureActor {
  "id": string;
  "type": "api_key" | "user";
}

export interface DisclosureBadgeSet {
  "id": "ai-generated" | "ai-manipulated" | "ai-interaction" | "ai-assisted";
  "label": string;
  "meaning": string;
  "variants": ReadonlyArray<"brand-light" | "brand-dark" | "neutral">;
}

export interface DisclosureChainHead {
  "hash": string;
  "sequence": number;
}

export interface DisclosureEventBlock {
  "jurisdiction": "EU" | "US-CA" | "US-ME" | "US-NH" | "US-NY" | "US-UT" | "IN" | "CN" | "KR";
  "kind": DisclosureEventKind;
  "type": "disclosure_event";
}

export type DisclosureEventKind = "ai_interaction_notice" | "visible_label_offered" | "visible_label_applied" | "user_acknowledged";

export interface DisclosureEventPage {
  "chain_head": DisclosureChainHead | null;
  "data": ReadonlyArray<DisclosureEventRecord>;
  "next_cursor": string | null;
}

export interface DisclosureEventReceipt {
  "event_id": string;
  "hash": string;
  "prev_hash": string;
  "received_at": string;
  "sequence": number;
}

export interface DisclosureEventRecord {
  "account_id": string;
  "actor": DisclosureActor;
  "client_time": string;
  "content_ref": string | null;
  "event_id": string;
  "hash": string;
  "jurisdiction": "EU" | "US-CA" | "US-ME" | "US-NH" | "US-NY" | "US-UT" | "IN" | "CN" | "KR";
  "kind": DisclosureEventKind;
  "locale": string | null;
  "origin"?: string | null;
  "policy_version": string;
  "prev_hash": string;
  "received_at": string;
  "rule_id": string | null;
  "schema_version": "op.disclosure-event.v1" | "op.disclosure-event.v2";
  "sequence": number;
  "subject_ref": string;
  "surface": string | null;
}

export interface DisclosureEventRequest {
  "client_time": string;
  "content_ref"?: string | null;
  "jurisdiction": "EU" | "US-CA" | "US-ME" | "US-NH" | "US-NY" | "US-UT" | "IN" | "CN" | "KR";
  "kind": DisclosureEventKind;
  "locale"?: string | null;
  "policy_version": string;
  "rule_id"?: string | null;
  "subject_ref": string;
  "surface"?: "web" | "app" | "voice" | "api" | "other" | null;
}

export interface DisclosureInstrument {
  "applies_from": string | null;
  "citation": string;
  "id": string;
  "status": "in_force" | "enacted_not_in_force" | "amended" | "proposed";
  "title": string;
  "url": string | null;
}

export interface DisclosureJurisdictionPolicy {
  "id": "EU" | "US-CA" | "US-ME" | "US-NH" | "US-NY" | "US-UT" | "IN" | "CN" | "KR";
  "instruments": ReadonlyArray<DisclosureInstrument>;
  "name": string;
  "rules": ReadonlyArray<DisclosureRule>;
}

export interface DisclosurePolicyDocument {
  "badge_sets": ReadonlyArray<DisclosureBadgeSet>;
  "disclaimer": string;
  "jurisdictions": ReadonlyArray<DisclosureJurisdictionPolicy>;
  "needs_legal_review": boolean;
  "policy_version": string;
  "published_at": string;
  "schema_version": "op.disclosure-policy.2026-10.v1";
}

export interface DisclosureRule {
  "badge_set": string | null;
  "exceptions": ReadonlyArray<string>;
  "form": string;
  "id": string;
  "instrument": string;
  "kind": "ai_interaction_notice" | "visible_label" | "deepfake_label" | "machine_readable_marking";
  "needs_legal_review": boolean;
  "obligated_party": "provider" | "deployer" | "operator" | "platform";
  "provision": string;
  "texts": ReadonlyArray<DisclosureText>;
  "timing": "before_first_interaction" | "at_first_interaction" | "on_display" | "on_publication" | "on_request";
  "trigger": string;
}

export interface DisclosureText {
  "locale": string;
  "text": string;
}

export interface DownloadResponse {
  "byte_length": number;
  "expires_at": string;
  "filename": string;
  "headers": Record<string, string>;
  "media_type": "application/epub+zip" | "application/onnx" | "application/oxps" | "application/pdf" | "application/vnd.oasis.opendocument.text" | "application/vnd.openxmlformats-officedocument.wordprocessingml.document" | "application/x-jax" | "application/x-keras" | "application/x-mlnet" | "application/x-mxnet" | "application/x-npy" | "application/x-openvino-ir+xml" | "application/x-openvino-weights" | "application/x-pickle" | "application/x-protobuf" | "application/x-pytorch" | "application/x-tensorflow" | "application/x-tensorflow-savedmodel" | "application/x-zip-based" | "application/xhtml+xml" | "application/xml" | "audio/MPA" | "audio/aac" | "audio/flac" | "audio/mp4" | "audio/mpeg" | "audio/wav" | "audio/x-riff-based" | "font/otf" | "image/avif" | "image/gif" | "image/heic" | "image/heic-sequence" | "image/heif" | "image/heif-sequence" | "image/jpeg" | "image/jxl" | "image/png" | "image/svg+xml" | "image/tiff" | "image/webp" | "image/x-adobe-dng" | "image/x-riff-based" | "image/x-tiff-based" | "text/html" | "text/plain" | "text/xml" | "video/mp4" | "video/quicktime" | "video/x-bmff-based" | "video/x-msvideo" | "video/x-riff-based";
  "method": "GET";
  "sha256": string;
  "sidecar_manifest"?: SidecarManifestResponse | null;
  "storage_version_sha256": string;
  "url": string;
}

export type EmbeddingPlacement = "jpeg_after_last_app0" | "png_before_first_idat" | "webp_riff_end" | "tiff_terminal_ifd" | "wav_riff_end" | "mp3_id3v2_geob" | "bmff_top_level_uuid" | "markdown_front_matter" | "gif_application_extension_after_color_table" | "jxl_container_top_level_jumb" | "svg_root_metadata" | "avi_riff_end" | "flac_leading_id3v2_geob";

export interface EmbeddingPlan {
  "maximum_fragments": number;
  "maximum_manifest_store_bytes": number;
  "placement": EmbeddingPlacement;
  "post_write_validation_required"?: true;
  "replace_existing_manifest"?: true;
  "source_remains_immutable"?: true;
  "write_new_output_object"?: true;
}

export interface ErrorResponse {
  "code": ReasonCode;
  "detail_code"?: ReasonCode | null;
  "documentation_url": string;
  "field_details": Record<string, string>;
  "job_reference"?: string | null;
  "message": string;
  "request_id": string;
  "retryable": boolean;
}

export interface ExportItemResponse {
  "byte_length": number | null;
  "download_expires_at"?: string | null;
  "download_url"?: string | null;
  "resource_id": string;
  "resource_type": string;
  "sha256": string | null;
}

export interface ExportMetadataResponse {
  "expires_at": string;
  "export_id": string;
  "item_count": number;
  "kind": string;
  "manifest_sha256": string | null;
  "ready_at": string | null;
  "requested_at": string;
  "status": string;
  "total_bytes": number;
}

export interface ExportPageResponse {
  "items": ReadonlyArray<ExportMetadataResponse>;
  "next_cursor": string | null;
}

export interface ExportResponse {
  "expires_at": string;
  "export_id": string;
  "filters"?: Record<string, unknown> | null;
  "item_count": number;
  "items"?: ReadonlyArray<ExportItemResponse>;
  "kind": string;
  "manifest"?: Record<string, unknown> | null;
  "manifest_sha256": string | null;
  "status": string;
  "total_bytes": number;
}

export interface ExpressSignResponse {
  "active_plan_revision": number;
  "asset_id": string;
  "cancel_requested_at": string | null;
  "download": DownloadResponse | null;
  "error_code": string | null;
  "fingerprint"?: boolean | null;
  "job_id": string;
  "media_inspection": NormalizedInspectionFacts | null;
  "policy_version": string;
  "progress": JobProgressResponse;
  "recipe_id": string;
  "recipe_version": number;
  "result": JobResultResponse | null;
  "state": JobState;
  "steps": ReadonlyArray<JobStepResponse>;
  "terminal_at": string | null;
  "watermark"?: boolean | null;
}

export interface FeedbackBody {
  "category"?: string | null;
  "contact_consented"?: boolean;
  "contexts"?: ReadonlyArray<FeedbackContextBody>;
  "message": string;
}

export interface FeedbackContextBody {
  "diagnostic_code"?: string | null;
  "diagnostic_version"?: string | null;
  "resource_id": string;
  "resource_type": "asset" | "job" | "publication" | "receipt" | "upload";
}

export interface FeedbackResponse {
  "feedback_id": string;
}

export interface FingerprintAlgorithmResponse {
  "algorithm_id": string;
  "default": boolean;
  "display_name": string;
  "locked": boolean;
  "soft_binding_registry_id"?: number | null;
  "strength_note": string;
}

export interface FingerprintBlock {
  "algorithms"?: ReadonlyArray<"audfprint" | "chromaprint" | "dinov2" | "dinov2-lsh256" | "iscc-audio" | "iscc-image" | "pdq" | "tmk-pdqf" | "vpdq"> | null;
  "type": "fingerprint";
}

export interface GovernanceErrorResponse {
  "code": string;
  "documentation_url": string;
  "field_details": Record<string, string>;
  "message": string;
  "request_id": string;
  "retryable": boolean;
}

export interface GovernanceReadinessResponse {
  "capture_authority": boolean;
  "commercial_authority": boolean;
  "derived_index_reconciler": boolean;
  "status": string;
}

export type HardBindingExclusionTarget = "jpeg_c2pa_app11" | "png_c2pa_cabx" | "webp_c2pa_chunk" | "tiff_c2pa_tag" | "wav_c2pa_chunk" | "mp3_c2pa_geob" | "bmff_c2pa_uuid" | "markdown_front_matter" | "gif_c2pa_application_extension" | "jxl_c2pa_jumb_box" | "svg_c2pa_manifest_text" | "avi_c2pa_chunk" | "flac_c2pa_geob";

export interface HardBindingPlan {
  "adapter_owns_exclusion_layout"?: true;
  "algorithm"?: "sha256";
  "assertion_label"?: "c2pa.hash.data" | "c2pa.hash.bmff";
  "compute_after_last_byte_change"?: true;
  "exclusion_target": HardBindingExclusionTarget;
  "existing_exclusion_ranges"?: ReadonlyArray<ByteRange>;
}

export interface HealthResponse {
  "service": string;
  "source_revision": string;
  "status": string;
}

export type HistoryMediaType = "image/jpeg" | "image/png" | "image/webp" | "image/tiff" | "image/avif" | "image/gif" | "image/jxl" | "image/svg+xml" | "image/x-adobe-dng" | "image/heic" | "image/heif" | "image/heic-sequence" | "image/heif-sequence" | "audio/wav" | "audio/mpeg" | "audio/mp4" | "audio/flac" | "video/mp4" | "video/quicktime" | "video/x-msvideo" | "text/markdown" | "font/otf" | "application/x-npy" | "application/onnx" | "application/x-pytorch" | "application/x-pickle" | "application/x-tensorflow" | "application/x-tensorflow-savedmodel" | "application/x-protobuf" | "application/x-keras" | "application/x-jax" | "application/x-mxnet" | "application/x-mlnet" | "application/x-openvino-ir+xml" | "application/x-openvino-weights" | "application/pdf" | "application/epub+zip" | "application/vnd.openxmlformats-officedocument.wordprocessingml.document" | "application/vnd.oasis.opendocument.text" | "application/oxps" | "application/x-zip-based" | "text/plain" | "text/html" | "text/xml" | "application/xml" | "application/xhtml+xml" | "audio/aac" | "audio/MPA" | "audio/x-riff-based" | "image/x-tiff-based" | "image/x-riff-based" | "video/x-bmff-based" | "video/x-riff-based" | "application/c2pa";

export interface HttpErrorResponse {
  "detail": string;
}

export interface HTTPValidationError {
  "detail"?: ReadonlyArray<ValidationError>;
}

export type IdentityCredentialKind = "individual" | "organisation";

export interface IdentityCredentialListResponse {
  "cawg_available": boolean;
  "data": ReadonlyArray<IdentityCredentialResponse>;
  "unavailable_reason": string | null;
}

export interface IdentityCredentialResponse {
  "credential_id": string;
  "enrolled_at": string;
  "kind": IdentityCredentialKind;
  "not_after": string;
  "not_before": string;
  "status": IdentityCredentialStatus;
  "subject_name": string;
}

export type IdentityCredentialStatus = "pending" | "active" | "suspended" | "revoked" | "expired";

export interface ImageProfileListResponse {
  "profiles": ReadonlyArray<ImageProfileResponse>;
}

export interface ImageProfileResponse {
  "accepted_auxiliaries": ReadonlyArray<string>;
  "accepted_bit_depths": ReadonlyArray<number>;
  "availability": "unreviewed" | "reviewed_unavailable" | "available";
  "color_class": "sdr" | "hdr";
  "limits_are_provisional": boolean;
  "max_compressed_bytes": number;
  "max_height": number;
  "max_pixels": number;
  "max_width": number;
  "media_format": string;
  "planned_auxiliaries": ReadonlyArray<string>;
  "planned_bit_depths": ReadonlyArray<number>;
  "profile_id": string;
  "profile_version": string;
  "recipes": ReadonlyArray<string>;
  "unavailable_reason": string;
}

export interface IssuedApiKeyResponse {
  "created_at": string;
  "display_hint": string;
  "expires_at": string | null;
  "id": string;
  "last_used_at": string | null;
  "name": string | null;
  "restrictions"?: ApiKeyRestrictionsView | null;
  "revoked_at": string | null;
  "rotated_from_id": string | null;
  "rotation"?: ApiKeyRotationResponse | null;
  "scopes": ReadonlyArray<string>;
  "secret": string;
  "status": ApiKeyStatus;
}

export interface IssuedWebhookEndpointResponse {
  "endpoint": WebhookEndpointResponse;
  "secret": string;
}

export interface JobHistoryPageResponse {
  "items": ReadonlyArray<JobHistoryResponse>;
  "next_cursor": string | null;
}

export interface JobHistoryResponse {
  "asset_id": string;
  "attempt_count": number;
  "canceled_steps": number;
  "created_at": string;
  "error_code": string | null;
  "failed_steps": number;
  "job_id": string;
  "job_url": string;
  "kind": JobKind;
  "progress_percent": number;
  "receipt_url": string | null;
  "recipe_id": string;
  "recipe_version": number;
  "state": JobState;
  "succeeded_steps": number;
  "total_steps": number;
  "updated_at": string;
  "verification_url": string | null;
}

export type JobKind = "sign" | "watermark" | "watermark_then_sign" | "capture";

export interface JobProgressResponse {
  "canceled_steps": number;
  "failed_steps": number;
  "percent": number;
  "succeeded_steps": number;
  "total_steps": number;
}

export interface JobResponse {
  "active_plan_revision": number;
  "asset_id": string;
  "cancel_requested_at": string | null;
  "error_code": string | null;
  "fingerprint"?: boolean | null;
  "job_id": string;
  "media_inspection": NormalizedInspectionFacts | null;
  "policy_version": string;
  "progress": JobProgressResponse;
  "recipe_id": string;
  "recipe_version": number;
  "result": JobResultResponse | null;
  "state": JobState;
  "steps": ReadonlyArray<JobStepResponse>;
  "terminal_at": string | null;
  "watermark"?: boolean | null;
}

export interface JobResultResponse {
  "asset_id": string;
  "publication_id": string;
  "receipt_id": string;
  "verification_id": string;
}

export type JobState = "accepted" | "queued" | "running" | "cancel_requested" | "completed" | "canceled" | "expired" | "rejected" | "failed";

export interface JobStepResponse {
  "attempt_count": number;
  "last_error_code": string | null;
  "max_attempts": number;
  "next_attempt_at": string | null;
  "plan_revision": number;
  "reconciliation_required"?: boolean;
  "state": JobStepState;
  "step_id": string;
  "step_key": string;
  "step_type": string;
}

export type JobStepState = "pending" | "ready" | "leased" | "running" | "succeeded" | "retry_wait" | "reconcile_wait" | "canceled" | "failed";

export interface LegacyReceiptValidationResponse {
  "outcome": "valid";
  "request_sha256": string;
  "result_sha256": string;
  "revocation_snapshot_id": string;
  "trust_snapshot_id": string;
  "validated_at": string;
  "verification_id": string;
}

export interface LegacySigningReceiptEvidenceResponse {
  "asset_id": string;
  "job_id": string;
  "manifest": ReceiptManifestResponse;
  "output": ReceiptOutputResponse;
  "prior_provenance": ReceiptPriorProvenanceResponse;
  "product": ReceiptProductResponse;
  "published_at": string;
  "schema_version": "op.signing-receipt.v1";
  "signing": ReceiptSigningResponse;
  "validation": LegacyReceiptValidationResponse;
}

export interface LegalHoldResponse {
  "created_at": string;
  "legal_hold_id": string;
  "reason": string | null;
  "released_at": string | null;
  "scope": string;
  "status": string;
  "target_id": string | null;
}

export interface LimitsCostGuidanceResponse {
  "text": string;
  "usage_path": string;
}

export interface MadeWith {
  "answer": MadeWithAnswer;
  "method": MadeWithMethod | null;
  "provider_name": string;
  "recovery_checked": boolean;
}

export type MadeWithAnswer = "yes" | "no_record";

export type MadeWithMethod = "c2pa_manifest" | "watermark" | "fingerprint";

export type ManifestContainer = "jpeg_app11" | "png_cabx" | "riff_c2pa_chunk" | "tiff_tag_52545" | "wav_c2pa_chunk" | "mp3_id3_geob" | "bmff_c2pa_uuid" | "markdown_front_matter" | "gif_c2pa_application_extension" | "jxl_jumb_box" | "svg_c2pa_metadata" | "avi_riff_c2pa_chunk" | "flac_id3_geob";

export type ManifestStoreState = "absent" | "present";

export interface MarkingCheckItemRequest {
  "asset_id"?: string | null;
  "object_id"?: string | null;
}

export interface MarkingCheckItemResult {
  "asset_id": string | null;
  "failure_reason": ReasonCode | null;
  "index": number;
  "object_id": string | null;
  "outcome": "pass" | "fail" | "pending" | "error";
  "requirements": ReadonlyArray<MarkingRequirementResult>;
  "verification_id": string | null;
}

export interface MarkingCheckRequest {
  "items": ReadonlyArray<MarkingCheckItemRequest>;
  "preset": "c2pa_baseline" | "eu_ai_act_art50" | "us_ca_sb942" | "cn_labeling_measures" | "kr_ai_framework_act" | "in_synthetic_information";
}

export interface MarkingCheckResponse {
  "completed_at": string | null;
  "created_at": string;
  "items": ReadonlyArray<MarkingCheckItemResult>;
  "marking_check_id": string;
  "preset": "c2pa_baseline" | "eu_ai_act_art50" | "us_ca_sb942" | "cn_labeling_measures" | "kr_ai_framework_act" | "in_synthetic_information";
  "state": "accepted" | "running" | "completed" | "failed";
  "statement": string;
  "summary": MarkingCheckSummary;
}

export interface MarkingCheckSummary {
  "errored": number;
  "failed": number;
  "passed": number;
  "pending": number;
}

export type MarkingRequirement = "c2pa_manifest" | "ai_declaration" | "recoverable_watermark" | "recoverable_fingerprint" | "machine_readable_ai_marking";

export interface MarkingRequirementResult {
  "detail": string;
  "evidence"?: "recovered" | "recorded" | null;
  "level": RequirementLevel;
  "outcome": "pass" | "fail" | "pending" | "not_checked";
  "requirement": MarkingRequirement;
}

export interface McpClientResponse {
  "configuration_template_id": string;
  "filename": string;
  "id": string;
  "label": string;
}

export interface McpFeatureGroupResponse {
  "id": string;
  "label": string;
  "read_only_scopes": ReadonlyArray<string>;
  "scopes": ReadonlyArray<string>;
}

export interface MediaAdapterPin {
  "contract_version": number;
  "name": string;
  "version": string;
}

export interface MediaCapabilityResponse {
  "availability": CapabilityAvailabilityResponse;
  "codec": string;
  "container": string;
  "fingerprint_algorithms"?: ReadonlyArray<FingerprintAlgorithmResponse>;
  "media_type": "application/epub+zip" | "application/onnx" | "application/oxps" | "application/pdf" | "application/vnd.oasis.opendocument.text" | "application/vnd.openxmlformats-officedocument.wordprocessingml.document" | "application/x-jax" | "application/x-keras" | "application/x-mlnet" | "application/x-mxnet" | "application/x-npy" | "application/x-openvino-ir+xml" | "application/x-openvino-weights" | "application/x-pickle" | "application/x-protobuf" | "application/x-pytorch" | "application/x-tensorflow" | "application/x-tensorflow-savedmodel" | "application/x-zip-based" | "application/xhtml+xml" | "application/xml" | "audio/MPA" | "audio/aac" | "audio/flac" | "audio/mp4" | "audio/mpeg" | "audio/wav" | "audio/x-riff-based" | "font/otf" | "image/avif" | "image/gif" | "image/heic" | "image/heic-sequence" | "image/heif" | "image/heif-sequence" | "image/jpeg" | "image/jxl" | "image/png" | "image/svg+xml" | "image/tiff" | "image/webp" | "image/x-adobe-dng" | "image/x-riff-based" | "image/x-tiff-based" | "text/html" | "text/plain" | "text/xml" | "video/mp4" | "video/quicktime" | "video/x-bmff-based" | "video/x-msvideo" | "video/x-riff-based";
  "processing": ProcessingLimitsResponse;
  "upload": UploadLimitsResponse;
  "watermark_algorithms"?: ReadonlyArray<WatermarkAlgorithmResponse>;
}

export interface MeResponse {
  "email": string;
  "public_id": string;
}

export interface MetadataFact {
  "byte_length": number;
  "count": number;
  "kind": MetadataKind;
}

export type MetadataKind = "exif" | "xmp" | "icc" | "text" | "comment" | "riff" | "id3" | "bmff" | "other";

export interface MeterQuotaResponse {
  "available": string;
  "carried_reserved": string;
  "hard_limit": string;
  "meter_type": string;
  "meter_version": number;
  "period_reserved": string;
  "reserved": string;
  "used": string;
}

export interface MultipartPartRequest {
  "byte_length": number;
  "part_number": number;
  "sha256": string;
}

export interface NormalizedAudioFacts {
  "adapter": MediaAdapterPin;
  "audio": AudioTrackFacts;
  "byte_length": number;
  "container_element_count": number;
  "decoder_components": ReadonlyArray<ComponentVersion>;
  "duration_microseconds": number;
  "embedding": EmbeddingPlan;
  "encrypted"?: false;
  "full_decode_succeeded"?: true;
  "hard_binding": HardBindingPlan;
  "manifest_store": OpaqueManifestStoreFacts;
  "maximum_box_depth"?: number | null;
  "media_format": "audio/mp4" | "audio/mpeg" | "audio/wav";
  "metadata"?: ReadonlyArray<MetadataFact>;
  "metadata_total_bytes": number;
  "schema_version"?: "op.media-inspection.audio.v1";
  "sha256": string;
  "source_reference": string;
  "track_count"?: 1;
}

export type NormalizedInspectionFacts = NormalizedMediaFacts | NormalizedAudioFacts | NormalizedVideoFacts;

export interface NormalizedMediaFacts {
  "adapter": MediaAdapterPin;
  "bits_per_channel": number;
  "byte_length": number;
  "channels": number;
  "color_mode": string;
  "color_profile"?: ColorProfileFacts | null;
  "container_element_count": number;
  "decoded_byte_length": number;
  "decoder": ComponentVersion;
  "embedding": EmbeddingPlan;
  "frame_count": number;
  "full_decode_succeeded"?: true;
  "hard_binding": HardBindingPlan;
  "height": number;
  "manifest_store": OpaqueManifestStoreFacts;
  "media_format": "image/avif" | "image/jpeg" | "image/png" | "image/tiff" | "image/webp";
  "metadata"?: ReadonlyArray<MetadataFact>;
  "metadata_total_bytes": number;
  "pixel_count": number;
  "schema_version"?: "op.media-inspection.v1";
  "sha256": string;
  "source_reference": string;
  "width": number;
}

export interface NormalizedVideoFacts {
  "adapter": MediaAdapterPin;
  "audio"?: AudioTrackFacts | null;
  "byte_length": number;
  "container_element_count": number;
  "decoder_components": ReadonlyArray<ComponentVersion>;
  "duration_microseconds": number;
  "embedding": EmbeddingPlan;
  "encrypted"?: false;
  "fragmented"?: false;
  "full_decode_succeeded"?: true;
  "hard_binding": HardBindingPlan;
  "manifest_store": OpaqueManifestStoreFacts;
  "maximum_box_depth": number;
  "media_format"?: "video/mp4";
  "metadata"?: ReadonlyArray<MetadataFact>;
  "metadata_total_bytes": number;
  "schema_version"?: "op.media-inspection.video.v1";
  "sha256": string;
  "source_reference": string;
  "track_count": number;
  "video": VideoTrackFacts;
}

export interface OnboardingApiKeysResponse {
  "active_count": number;
  "request_observation": RequestObservationResponse;
}

export interface OpaqueManifestStoreFacts {
  "byte_length"?: number;
  "container"?: ManifestContainer | null;
  "fragment_count"?: number;
  "jumbf_box_count"?: number;
  "maximum_depth"?: number;
  "ranges"?: ReadonlyArray<ByteRange>;
  "sha256"?: string | null;
  "state": ManifestStoreState;
  "trust_evaluated"?: false;
}

export interface OverviewActivityBucketResponse {
  "bucket_end": string;
  "bucket_start": string;
  "signing": number;
  "verifications": number;
}

export interface OverviewAttentionResponse {
  "count": number;
  "kind": "governance_deletions_active" | "governance_deletions_blocked" | "governance_exports_active" | "jobs_failed" | "jobs_rejected" | "queue_backlog_aging" | "quota_exhausted" | "webhook_deliveries_failing";
  "oldest_at"?: string | null;
  "severity": "critical" | "warning" | "info";
  "target_filters": Record<string, string>;
  "target_resource": "governance_deletions" | "governance_exports" | "jobs" | "quota" | "webhook_endpoints";
}

export interface OverviewComparisonResponse {
  "failed_jobs": number;
  "jobs_total": number;
  "range_end": string;
  "range_start": string;
  "signing": number;
  "terminal_latency_average_ms"?: number | null;
  "verifications": number;
}

export interface OverviewFreshnessResponse {
  "historical_rollups_as_of": string | null;
  "pending_rebuild_bucket_count": number;
  "recent_authoritative_as_of": string;
}

export interface OverviewGovernanceResponse {
  "current_deletion_requests": Record<string, number>;
  "current_exports": Record<string, number>;
  "range_deletion_requests": Record<string, number>;
  "range_exports": Record<string, number>;
}

export interface OverviewHealthResponse {
  "failed_jobs": number;
  "oldest_queued_at": string | null;
  "queue_by_state": Record<string, number>;
  "terminal_latency_average_ms": number | null;
  "terminal_latency_max_ms": number | null;
}

export interface OverviewJobMetricsResponse {
  "by_kind": Record<string, number>;
  "by_state": Record<string, number>;
  "signing": number;
  "total": number;
}

export interface OverviewQuotaMeterResponse {
  "available": string;
  "hard_limit": string;
  "meter_type": string;
  "meter_version": number;
  "reserved": string;
  "used": string;
}

export interface OverviewQuotaResponse {
  "meters": ReadonlyArray<OverviewQuotaMeterResponse>;
  "period": string | null;
}

export interface OverviewResponse {
  "activity": ReadonlyArray<OverviewActivityBucketResponse>;
  "as_of": string;
  "attention": ReadonlyArray<OverviewAttentionResponse>;
  "comparison": OverviewComparisonResponse | null;
  "freshness": OverviewFreshnessResponse;
  "governance": OverviewGovernanceResponse;
  "health": OverviewHealthResponse;
  "jobs": OverviewJobMetricsResponse;
  "media_kinds": Record<string, number>;
  "quota": OverviewQuotaResponse;
  "range": "7d" | "30d" | "12m";
  "range_end": string;
  "range_start": string;
  "unavailable": ReadonlyArray<OverviewUnavailableResponse>;
  "verification_outcomes": Record<string, number>;
  "webhooks": OverviewWebhookResponse;
}

export interface OverviewUnavailableResponse {
  "affected_from"?: string | null;
  "affected_to"?: string | null;
  "component": "historical_rollups" | "comparison" | "quota";
  "reason": "pending_rebuild" | "not_provisioned";
  "retryable": boolean;
}

export interface OverviewWebhookResponse {
  "deliveries_by_state": Record<string, number>;
  "endpoints_by_state": Record<string, number>;
}

export interface PortalIntentRequest {
  "return_url": string;
}

export interface PresignedPartResponse {
  "headers": Record<string, string>;
  "method": "PUT";
  "part_number": number;
  "url": string;
}

export interface PresignedRequestResponse {
  "headers": Record<string, string>;
  "method": "PUT";
  "url": string;
}

export interface PreviewResponse {
  "byte_length": number;
  "expires_at": string;
  "headers": Record<string, string>;
  "height": number;
  "media_type": "image/jpeg";
  "method": "GET";
  "sha256": string;
  "url": string;
  "width": number;
}

export interface PricingLineResponse {
  "action": string;
  "amount_usd": string;
  "quantity": string;
  "unit": string;
  "unit_price_usd": string;
}

export interface PricingQuoteRequest {
  "duration_seconds"?: number | string | null;
  "fingerprint"?: boolean | null;
  "frames_per_second"?: number | string | null;
  "height"?: number | null;
  "media_family": "image" | "audio" | "video" | "document" | "text" | "model" | "live";
  "operation": "sign" | "watermark" | "watermark_then_sign";
  "width"?: number | null;
}

export interface PricingQuoteResponse {
  "currency"?: "USD";
  "estimate_only"?: true;
  "excludes"?: ReadonlyArray<string>;
  "final_facts_source"?: "server_validated_media_inspection";
  "lines": ReadonlyArray<PricingLineResponse>;
  "pricing_version": string;
  "total_usd": string;
}

export interface PricingResponse {
  "activation"?: "requires_explicit_tenant_enrollment";
  "currency"?: "USD";
  "pricing_version": string;
  "processing_credits_included"?: false;
  "rates": Record<string, unknown>;
}

export interface ProcessingChargeResponse {
  "action": string;
  "amount_usd": string;
  "api_key_id": string | null;
  "created_at": string;
  "id": string;
  "job_id": string;
  "pricing_version": string;
  "quantity": string;
  "service_period_end": string;
  "service_period_start": string;
  "unit": string;
  "unit_price_usd": string;
}

export interface ProcessingChargesResponse {
  "currency"?: "USD";
  "items": ReadonlyArray<ProcessingChargeResponse>;
  "next_before": string | null;
  "provider_charge_created"?: false;
}

export interface ProcessingLimitsResponse {
  "maximum_duration_seconds"?: number | null;
  "maximum_height"?: number | null;
  "maximum_pixels"?: number | null;
  "maximum_width"?: number | null;
}

export interface PublicationResponse {
  "byte_length": number;
  "job_id": string;
  "media_type": "application/epub+zip" | "application/onnx" | "application/oxps" | "application/pdf" | "application/vnd.oasis.opendocument.text" | "application/vnd.openxmlformats-officedocument.wordprocessingml.document" | "application/x-jax" | "application/x-keras" | "application/x-mlnet" | "application/x-mxnet" | "application/x-npy" | "application/x-openvino-ir+xml" | "application/x-openvino-weights" | "application/x-pickle" | "application/x-protobuf" | "application/x-pytorch" | "application/x-tensorflow" | "application/x-tensorflow-savedmodel" | "application/x-zip-based" | "application/xhtml+xml" | "application/xml" | "audio/MPA" | "audio/aac" | "audio/flac" | "audio/mp4" | "audio/mpeg" | "audio/wav" | "audio/x-riff-based" | "font/otf" | "image/avif" | "image/gif" | "image/heic" | "image/heic-sequence" | "image/heif" | "image/heif-sequence" | "image/jpeg" | "image/jxl" | "image/png" | "image/svg+xml" | "image/tiff" | "image/webp" | "image/x-adobe-dng" | "image/x-riff-based" | "image/x-tiff-based" | "text/html" | "text/plain" | "text/xml" | "video/mp4" | "video/quicktime" | "video/x-bmff-based" | "video/x-msvideo" | "video/x-riff-based";
  "publication_id": string;
  "published_at": string;
  "receipt_id": string;
  "sha256": string;
  "verification_id": string;
}

export type PublicCaptureAdmissionReason = "passed" | "capture_identity_revoked" | "capture_identity_conflict" | "evidence_unavailable" | "evidence_invalid" | "app_identity_mismatch" | "app_downgrade" | "os_downgrade" | "security_level" | "boot_state" | "counter_replay" | "clock_rollback" | "reinstall_restore" | "request_mismatch" | "media_substitution" | "governance_rejected" | "asset_closed" | "commercial_rejected" | "capture_work_conflict" | "capture_work_unavailable";

export interface PublicCheckPage {
  "display_name": string;
  "slug": string;
}

export interface PublicCheckResponse {
  "check_id": string;
  "completed_at": string | null;
  "content_credentials": PublicContentCredentials | null;
  "created_at": string;
  "failure_reason": ReasonCode | null;
  "made_with": MadeWith | null;
  "media_type": string | null;
  "page": PublicCheckPage;
  "schema_version": "op.public-check.v1";
  "state": "running" | "completed" | "failed";
  "statement": string;
}

export interface PublicContentCredentials {
  "declared_origin": DeclaredOrigin | null;
  "status": DeclaredCredentialsStatus;
}

export type PublicRecipeCapability = "watermark" | "fingerprint" | "c2pa_signing";

export interface PublicVerifyPageResponse {
  "accepted_media_types"?: ReadonlyArray<string> | null;
  "check_url": string;
  "colours": VerifyPageColours;
  "display_name": string;
  "logo_url": string | null;
  "max_upload_bytes": number;
  "recover_own_assets": boolean;
  "schema_version": "op.public-verify-page.v1";
  "slug": string;
  "statement": string;
}

export interface ReadinessResponse {
  "status": string;
}

export type ReasonCode = "AI_DECLARATION_REQUIRES_SIGN_ONLY" | "API_KEY_IP_ALLOWLIST_UNAVAILABLE" | "API_KEY_IP_NOT_ALLOWED" | "API_KEY_ORIGIN_NOT_ALLOWED" | "API_KEY_PROFILE_FORBIDS" | "API_KEY_RATE_LIMITED" | "ASSET_DETAIL_UNAVAILABLE" | "ASSET_DOWNLOAD_UNAVAILABLE" | "ASSET_NOT_FOUND" | "ASSET_NOT_PUBLISHED" | "ASSET_PREVIEW_DERIVATIVE_MISSING" | "ASSET_PREVIEW_GENERATION_FAILED" | "ASSET_PREVIEW_PENDING" | "ASSET_PREVIEW_REDEMPTION_REFUSED" | "ASSET_PREVIEW_RESTRICTED" | "ASSET_PREVIEW_STORAGE_UNAVAILABLE" | "ASSET_PREVIEW_UNSUPPORTED_MEDIA" | "BILLING_ACCOUNT_SUSPENDED" | "BILLING_ACCOUNT_UNAVAILABLE" | "BILLING_INTENT_RATE_LIMITED" | "BILLING_QUOTA_EXCEEDED" | "BINDING_ACTIVATION_FAILED" | "BINDING_EVIDENCE_CONFLICT" | "BINDING_LOOKUP_AMBIGUOUS" | "BINDING_LOOKUP_FORBIDDEN" | "BINDING_LOOKUP_INDETERMINATE" | "BINDING_NOT_ACTIVE" | "CAPABILITY_COMPONENT_INCOMPATIBLE" | "CAPABILITY_COMPONENT_NOT_APPROVED" | "CAPABILITY_COMPONENT_NOT_REGISTERED" | "CAPABILITY_COMPONENT_RUNTIME_UNAVAILABLE" | "CAPABILITY_DETECTION_FAILED" | "CAPABILITY_FORMAT_AMBIGUOUS" | "CAPABILITY_FORMAT_UNDETECTED" | "CAPABILITY_RECIPE_INVALID" | "CAPABILITY_REGISTRATION_COLLISION" | "CAPABILITY_REGISTRY_NOT_SEALED" | "CAPABILITY_REGISTRY_SEALED" | "CREATOR_ASSERTION_REJECTED" | "CREATOR_BINDING_CONFLICT" | "CREATOR_DISCLOSURE_ERASED" | "CREATOR_DISCLOSURE_FORBIDDEN" | "CREATOR_IDENTITY_CONFLICT" | "CREATOR_IDENTITY_INVALID" | "CREATOR_IDENTITY_KEY_UNAVAILABLE" | "CREATOR_IDENTITY_NOT_FOUND" | "CREATOR_IDENTITY_REVOKED" | "DISCLOSURE_INVALID" | "DISCLOSURE_POLICY_NOT_FOUND" | "FINGERPRINT_ALGORITHM_UNSUPPORTED" | "FINGERPRINT_OUTPUT_INVALID" | "FINGERPRINT_RUNTIME_UNAVAILABLE" | "FOUNDATION_CANARY_OK" | "FOUNDATION_CANARY_UNCORRELATED" | "FOUNDATION_CONFIG_REJECTED" | "GENERATOR_ASSERTION_REJECTED" | "GENERATOR_CLAIM_CONFLICT" | "GENERATOR_ENGINE_UNAVAILABLE" | "GENERATOR_INGREDIENT_INVALID" | "GENERATOR_OUTPUT_INVALID" | "GENERATOR_SIGNING_FAILED" | "HISTORY_CURSOR_INVALID" | "HISTORY_QUERY_INVALID" | "HISTORY_READ_FORBIDDEN" | "HISTORY_RESOURCE_NOT_FOUND" | "IDENTITY_CREDENTIAL_NOT_ENROLLED" | "JOB_ASSET_NOT_READY" | "JOB_CANCEL_CONFLICT" | "JOB_CANCELED" | "JOB_COMPILE_CONFLICT" | "JOB_EFFECT_CONFLICT" | "JOB_IDEMPOTENCY_CONFLICT" | "JOB_LEASE_EXPIRED" | "JOB_LEASE_LOST" | "JOB_MESSAGE_INVALID" | "JOB_NOT_FOUND" | "JOB_OUTBOX_FAILED" | "JOB_PERMANENT_FAILURE" | "JOB_POLICY_REJECTED" | "JOB_RECIPE_INVALID" | "JOB_RECIPE_NOT_FOUND" | "JOB_REPLAY_FORBIDDEN" | "JOB_REPLAY_INVALID" | "JOB_RETRY_EXHAUSTED" | "JOB_RUNTIME_UNAVAILABLE" | "JOB_STEP_NOT_READY" | "JOB_TERMINAL" | "MARKING_CHECK_INVALID" | "MARKING_CHECK_NOT_FOUND" | "MEDIA_CODEC_UNSUPPORTED" | "MEDIA_COMPRESSED_SIZE_LIMIT" | "MEDIA_CONTAINER_LIMIT_EXCEEDED" | "MEDIA_CONTAINER_MALFORMED" | "MEDIA_DECODE_FAILED" | "MEDIA_DECODED_SIZE_LIMIT" | "MEDIA_DIMENSION_LIMIT_EXCEEDED" | "MEDIA_DURATION_LIMIT_EXCEEDED" | "MEDIA_ENCRYPTION_REJECTED" | "MEDIA_FORMAT_AMBIGUOUS" | "MEDIA_FORMAT_UNDETECTED" | "MEDIA_MANIFEST_LIMIT_EXCEEDED" | "MEDIA_MANIFEST_MALFORMED" | "MEDIA_METADATA_LIMIT_EXCEEDED" | "MEDIA_METADATA_MALFORMED" | "MEDIA_OUTPUT_CONTRACT_VIOLATION" | "MEDIA_PARSER_DIFFERENTIAL" | "MEDIA_POLYGLOT_REJECTED" | "MEDIA_PREVIEW_LIMIT_EXCEEDED" | "MEDIA_PREVIEW_UNSUPPORTED" | "MEDIA_PROFILE_INVALID" | "MEDIA_PROTOCOL_VERSION_UNSUPPORTED" | "MEDIA_RESOURCE_EXHAUSTED" | "MEDIA_SANDBOX_UNAVAILABLE" | "MEDIA_TIMEOUT" | "MEDIA_TIMESTAMP_LIMIT_EXCEEDED" | "MEDIA_TRACK_LIMIT_EXCEEDED" | "MODEL_ARTIFACT_INVALID" | "PUBLIC_CHECK_MEDIA_UNSUPPORTED" | "PUBLIC_CHECK_MONTHLY_LIMIT_REACHED" | "PUBLIC_CHECK_NOT_FOUND" | "PUBLIC_CHECK_RATE_LIMITED" | "PUBLICATION_EVIDENCE_INVALID" | "PUBLICATION_REQUEST_INVALID" | "SIGNING_ALGORITHM_REJECTED" | "SIGNING_AUDIT_UNAVAILABLE" | "SIGNING_AUTHORIZATION_EXPIRED" | "SIGNING_AUTHORIZATION_INVALID" | "SIGNING_AUTHORIZATION_REPLAYED" | "SIGNING_CERTIFICATE_MISMATCH" | "SIGNING_DIGEST_MISMATCH" | "SIGNING_FENCE_MISMATCH" | "SIGNING_KMS_DENIED" | "SIGNING_KMS_KEY_MISMATCH" | "SIGNING_PROFILE_UNAVAILABLE" | "SIGNING_SIGNATURE_INVALID" | "SIGNING_TIMESTAMP_FAILED" | "SIGNING_TIMESTAMP_REPLAYED" | "STORAGE_IMMUTABILITY_VIOLATION" | "STORAGE_OPERATION_FAILED" | "TENANT_WRITE_CONTENDED" | "UPLOAD_ABORTED" | "UPLOAD_ALREADY_COMPLETED" | "UPLOAD_CHECKSUM_MISMATCH" | "UPLOAD_EXPIRED" | "UPLOAD_IDEMPOTENCY_CONFLICT" | "UPLOAD_INCOMPLETE" | "UPLOAD_INVALID_PARTS" | "UPLOAD_NOT_FOUND" | "UPLOAD_POLICY_REJECTED" | "UPLOAD_SIZE_MISMATCH" | "VALIDATION_ACTIVE_MANIFEST_INVALID" | "VALIDATION_CERTIFICATE_EXPIRED" | "VALIDATION_CERTIFICATE_INVALID" | "VALIDATION_CERTIFICATE_NOT_YET_VALID" | "VALIDATION_CONFORMANCE_LIST_UNAVAILABLE" | "VALIDATION_CONFORMANCE_PRODUCT_NOT_LISTED" | "VALIDATION_EVIDENCE_UNAVAILABLE" | "VALIDATION_HARD_BINDING_MISMATCH" | "VALIDATION_INGREDIENT_CYCLE" | "VALIDATION_INGREDIENT_INVALID" | "VALIDATION_INGREDIENT_LIMIT_EXCEEDED" | "VALIDATION_INTEGRITY_MISMATCH" | "VALIDATION_LIMIT_EXCEEDED" | "VALIDATION_MANIFEST_ABSENT" | "VALIDATION_MANIFEST_MALFORMED" | "VALIDATION_MANIFEST_UNSUPPORTED" | "VALIDATION_OUTPUT_INVALID" | "VALIDATION_POLICY_INVALID" | "VALIDATION_RECOVERY_ONLY" | "VALIDATION_REVOCATION_MALFORMED" | "VALIDATION_REVOCATION_REVOKED" | "VALIDATION_REVOCATION_UNAVAILABLE" | "VALIDATION_REVOCATION_UNKNOWN" | "VALIDATION_RUNTIME_UNAVAILABLE" | "VALIDATION_SIGNATURE_ALGORITHM_UNSUPPORTED" | "VALIDATION_SIGNATURE_INVALID" | "VALIDATION_SIGNER_UNTRUSTED" | "VALIDATION_SOURCE_MISMATCH" | "VALIDATION_STATUS_UNRECOGNIZED" | "VALIDATION_STRUCTURE_INVALID" | "VALIDATION_TIMESTAMP_INVALID" | "VALIDATION_TIMESTAMP_MISSING" | "VALIDATION_TIMESTAMP_UNTRUSTED" | "VALIDATION_TRUST_SNAPSHOT_EXPIRED" | "VALIDATION_TRUST_SNAPSHOT_INVALID" | "VERIFY_EXECUTION_CONTRACT_VIOLATION" | "VERIFY_IDEMPOTENCY_CONFLICT" | "VERIFY_MANIFEST_INVALID" | "VERIFY_MANIFEST_NOT_APPLICABLE" | "VERIFY_NOT_FOUND" | "VERIFY_NOT_READY" | "VERIFY_PAGE_CONFLICT" | "VERIFY_PAGE_INVALID" | "VERIFY_PAGE_NOT_FOUND" | "VERIFY_REPORT_NOT_FOUND" | "VERIFY_SHARE_NOT_FOUND" | "WATERMARK_DETECTION_FAILED" | "WATERMARK_EMBED_FAILED" | "WATERMARK_MODEL_INVALID" | "WATERMARK_PAYLOAD_MISMATCH" | "WATERMARK_RUNTIME_UNAVAILABLE" | "WEBHOOK_DELIVERY_UNAVAILABLE" | "WEBHOOK_NOT_FOUND" | "WEBHOOK_REPLAY_FORBIDDEN" | "WEBHOOK_TEST_RATE_LIMITED" | "WORKFLOW_TEMPLATE_CONFLICT" | "WORKFLOW_TEMPLATE_INVALID" | "WORKFLOW_TEMPLATE_NOT_FOUND";

export interface ReceiptAiDeclarationResponse {
  "declaration_sha256": string;
  "digital_source_type": DigitalSourceType;
  "inception_action": "c2pa.created";
}

export interface ReceiptBindingSetResponse {
  "binding_set_sha256": string;
  "candidate_count": number;
  "schema_version": "op.publication-binding-set.v1";
  "types": ReadonlyArray<"hard_hash" | "iscc_fingerprint" | "sscd_descriptor" | "dinov2_descriptor" | "pdq_fingerprint" | "dinov2_lsh_fingerprint" | "audio_fingerprint" | "audfprint_fingerprint" | "iscc_audio_fingerprint" | "video_fingerprint" | "vpdq_fingerprint" | "watermark">;
}

export interface ReceiptHistoryPageResponse {
  "items": ReadonlyArray<ReceiptHistoryResponse>;
  "next_cursor": string | null;
}

export interface ReceiptHistoryResponse {
  "asset_id": string;
  "byte_length": number | null;
  "created_at": string;
  "job_id": string;
  "media_type": HistoryMediaType | null;
  "receipt_id": string;
  "receipt_url": string;
  "schema_version": string;
  "sha256": string | null;
}

export interface ReceiptManifestResponse {
  "active_label_sha256": string;
  "claim_plan_sha256": string;
  "manifest_id": string;
  "manifest_store_sha256": string;
}

export interface ReceiptOutputResponse {
  "byte_length": number;
  "media_type": "application/epub+zip" | "application/onnx" | "application/oxps" | "application/pdf" | "application/vnd.oasis.opendocument.text" | "application/vnd.openxmlformats-officedocument.wordprocessingml.document" | "application/x-jax" | "application/x-keras" | "application/x-mlnet" | "application/x-mxnet" | "application/x-npy" | "application/x-openvino-ir+xml" | "application/x-openvino-weights" | "application/x-pickle" | "application/x-protobuf" | "application/x-pytorch" | "application/x-tensorflow" | "application/x-tensorflow-savedmodel" | "application/x-zip-based" | "application/xhtml+xml" | "application/xml" | "audio/MPA" | "audio/aac" | "audio/flac" | "audio/mp4" | "audio/mpeg" | "audio/wav" | "audio/x-riff-based" | "font/otf" | "image/avif" | "image/gif" | "image/heic" | "image/heic-sequence" | "image/heif" | "image/heif-sequence" | "image/jpeg" | "image/jxl" | "image/png" | "image/svg+xml" | "image/tiff" | "image/webp" | "image/x-adobe-dng" | "image/x-riff-based" | "image/x-tiff-based" | "text/html" | "text/plain" | "text/xml" | "video/mp4" | "video/quicktime" | "video/x-bmff-based" | "video/x-msvideo" | "video/x-riff-based";
  "object_id": string;
  "sha256": string;
  "storage_version_sha256": string;
}

export interface ReceiptPriorProvenanceResponse {
  "disposition": "absent" | "valid_parent" | "untrusted_parent" | "invalid_parent";
  "validation_result_sha256"?: string | null;
  "warning"?: ReceiptPriorProvenanceWarningResponse | null;
}

export interface ReceiptPriorProvenanceWarningResponse {
  "c2pa_failure_codes": ReadonlyArray<string>;
  "code": "prior_credential_untrusted" | "prior_credential_invalid";
  "message": string;
  "reason_codes": ReadonlyArray<string>;
}

export interface ReceiptProductResponse {
  "id": string;
  "name": string;
  "release_id": string;
}

export interface ReceiptRecoveryResponse {
  "accepted_at": string;
  "observation_policy_sha256": string;
  "observation_sha256": string;
  "recovery_id": string;
  "result_sha256": string;
}

export interface ReceiptResponse {
  "asset_id": string;
  "created_at": string;
  "evidence": LegacySigningReceiptEvidenceResponse | SigningReceiptEvidenceResponse | SidecarSigningReceiptEvidenceResponse | AiDeclaredSigningReceiptEvidenceResponse | RecoveredSigningReceiptEvidenceResponse | BindingReceiptEvidenceResponse;
  "job_id": string;
  "receipt_id": string;
}

export interface ReceiptSigningResponse {
  "evidence_id": string;
  "evidence_sha256": string;
  "signature_sha256": string;
  "timestamp_evidence_sha256": string | null;
  "timestamp_omission_sha256"?: string | null;
}

export interface ReceiptValidationResponse {
  "outcome": "valid" | "recovered";
  "recovery_only": boolean;
  "request_sha256": string;
  "result_sha256": string;
  "revocation_snapshot_id": string | null;
  "trust_snapshot_id": string | null;
  "validated_at": string;
  "validation_path": "direct" | "recovery";
  "verification_id": string;
}

export type RecipeCatalogKind = "sign_only" | "watermark_only" | "watermark_then_sign";

export interface RecipeCatalogResponse {
  "available": boolean;
  "catalog_version"?: "op.recipe-catalog.v1";
  "definition_sha256": string;
  "kind": RecipeCatalogKind;
  "name": string;
  "recipe_id": string;
  "recipe_url": string;
  "required_capabilities": ReadonlyArray<string>;
  "required_steps": ReadonlyArray<string>;
  "schema_version": string;
  "supported_media_types": ReadonlyArray<"audio/mp4" | "audio/mpeg" | "audio/wav" | "image/avif" | "image/jpeg" | "image/png" | "image/tiff" | "image/webp" | "video/mp4">;
  "unavailable_reason": RecipeUnavailableReason | null;
  "version": number;
}

export interface RecipeListResponse {
  "recipes": ReadonlyArray<RecipeResponse>;
}

export interface RecipeResponse {
  "capabilities": ReadonlyArray<PublicRecipeCapability>;
  "display_name": string;
  "recipe_id": string;
  "summary": string;
  "supported_media_types": ReadonlyArray<"audio/flac" | "audio/mp4" | "audio/mpeg" | "audio/wav" | "image/avif" | "image/gif" | "image/heic" | "image/heic-sequence" | "image/heif" | "image/heif-sequence" | "image/jpeg" | "image/jxl" | "image/png" | "image/svg+xml" | "image/tiff" | "image/webp" | "image/x-adobe-dng" | "video/mp4" | "video/quicktime" | "video/x-msvideo">;
  "version": number;
}

export type RecipeUnavailableReason = "definition_shape_invalid" | "definition_hash_mismatch" | "step_contract_mismatch" | "no_enabled_media_format" | "runtime_unavailable";

export interface RecoveredReceiptSigningResponse {
  "evidence_id": string;
  "evidence_sha256": string;
  "signature_sha256": string;
  "timestamp_evidence_sha256": string | null;
  "timestamp_omission_sha256": null;
  "timestamp_policy_observation_sha256": string | null;
}

export interface RecoveredSigningReceiptEvidenceResponse {
  "asset_id": string;
  "bindings": ReceiptBindingSetResponse;
  "job_id": string;
  "manifest": ReceiptManifestResponse;
  "output": ReceiptOutputResponse;
  "prior_provenance": ReceiptPriorProvenanceResponse;
  "product": ReceiptProductResponse;
  "published_at": string;
  "recovery": ReceiptRecoveryResponse;
  "schema_version": "op.signing-receipt.v3";
  "signing": RecoveredReceiptSigningResponse;
  "validation": ReceiptValidationResponse;
}

export interface ReplayWebhookDeliveryResponse {
  "event_id": string;
}

export interface ReportContentResponse {
  "content_base64": string;
  "content_sha256": string;
  "content_type": string;
}

export type ReportFormat = "machine_json" | "human_pdf";

export interface ReportResponse {
  "byte_length"?: number | null;
  "content_sha256"?: string | null;
  "content_type"?: string | null;
  "format": string;
  "payload"?: Record<string, unknown> | null;
  "report_id": string;
  "state": string;
}

export interface RequestObservationResponse {
  "ever_used": boolean | null;
  "last_request_at": string | null;
  "retry_after_seconds": number | null;
  "retryable": boolean;
  "state": RequestObservationState;
}

export type RequestObservationState = "available" | "temporarily_unavailable";

export type RequirementLevel = "required" | "recommended";

export interface ReviewedRecipeAvailabilityResponse {
  "active": CapabilityRecipeResponse | null;
  "availability": CapabilityAvailabilityResponse;
  "recipe_id": string;
}

export interface RotatedWebhookSecretResponse {
  "endpoint": WebhookEndpointResponse;
  "secret": string;
}

export interface RotateWebhookSecretRequest {
  "overlap_seconds"?: number;
}

export interface SafetyStatementResponse {
  "id": string;
  "text": string;
}

export interface SecretNotReplayableResponse {
  "detail": "secret_not_replayable";
}

export interface SharedVerificationResponse {
  "creator"?: CreatorDisclosureResponse | null;
  "result": Record<string, unknown>;
  "schema_version": string;
  "verification_id": string;
}

export interface SidecarManifestResponse {
  "byte_length": number;
  "expires_at": string;
  "filename": string;
  "headers": Record<string, string>;
  "media_type": "application/c2pa";
  "method": "GET";
  "sha256": string;
  "storage_version_sha256": string;
  "url": string;
}

export interface SidecarReceiptBindingSetResponse {
  "binding_set_sha256": string;
  "candidate_count": 1;
  "schema_version": "op.publication-binding-set.v1";
  "types": ReadonlyArray<"hard_hash">;
}

export interface SidecarReceiptManifestResponse {
  "claim_plan_sha256": string;
  "manifest_id": string;
  "manifest_store_sha256": string;
  "sidecar_object_id": string;
  "sidecar_sha256": string;
}

export interface SidecarSigningReceiptEvidenceResponse {
  "asset_id": string;
  "bindings": SidecarReceiptBindingSetResponse;
  "job_id": string;
  "manifest": SidecarReceiptManifestResponse;
  "output": ReceiptOutputResponse;
  "prior_provenance"?: ReceiptPriorProvenanceResponse | null;
  "product": ReceiptProductResponse;
  "published_at": string;
  "schema_version": "op.signing-receipt.sidecar.v1";
  "signing": ReceiptSigningResponse;
  "validation": ReceiptValidationResponse;
}

export interface SignBatchItemResponse {
  "error": ErrorResponse | null;
  "index": number;
  "job": JobResponse | null;
  "status": number;
}

export interface SignBatchRequest {
  "items": ReadonlyArray<SignRequest>;
}

export interface SignBatchResponse {
  "items": ReadonlyArray<SignBatchItemResponse>;
}

export interface SignBlock {
  "creator_id"?: string | null;
  "mode"?: "standard" | "express" | null;
  "type": "sign";
}

export interface SignIdentityRequest {
  "credential_id": string;
}

export interface SigningReceiptEvidenceResponse {
  "asset_id": string;
  "bindings": ReceiptBindingSetResponse | SidecarReceiptBindingSetResponse;
  "job_id": string;
  "manifest": ReceiptManifestResponse;
  "output": ReceiptOutputResponse;
  "prior_provenance": ReceiptPriorProvenanceResponse;
  "product": ReceiptProductResponse;
  "published_at": string;
  "schema_version": "op.signing-receipt.v2";
  "signing": ReceiptSigningResponse;
  "validation": ReceiptValidationResponse;
}

export interface SignRequest {
  "ai_declaration"?: AiDeclarationRequest | null;
  "asset_id": string;
  "creator_id"?: string | null;
  "fingerprint"?: boolean | null;
  "fingerprint_algorithms"?: ReadonlyArray<"audfprint" | "chromaprint" | "dinov2" | "dinov2-lsh256" | "iscc-audio" | "iscc-image" | "pdq" | "tmk-pdqf" | "vpdq"> | null;
  "identity"?: SignIdentityRequest | null;
  "mode"?: "standard" | "express" | null;
  "recipe_id"?: string | null;
  "template_id"?: string | null;
  "watermark"?: boolean | null;
  "watermark_algorithm"?: "audioseal" | "audioseal-mm02-4" | "pixelseal" | "pixelseal-video" | "trustmark-b" | "trustmark-c" | "trustmark-p" | "trustmark-q" | "videoseal" | "videoseal-image" | null;
  "watermark_strength"?: "subtle" | "balanced" | "robust" | null;
}

export type StatusClass = "2xx" | "3xx" | "4xx" | "5xx";

export interface StripeInboxResponse {
  "duplicate": boolean;
  "event_id": string;
  "state": string;
}

export type SummaryWindow = "1h" | "24h" | "7d";

export interface UpdateWebhookEndpointAutoDisableRequest {
  "auto_disable_after_failures": number;
  "event_catalog_version"?: null;
  "events"?: null;
  "max_concurrency"?: number | null;
  "rate_limit_per_minute"?: number | null;
  "url"?: string | null;
}

export type UpdateWebhookEndpointCommand = UpdateWebhookEndpointEventsRequest | UpdateWebhookEndpointUrlRequest | UpdateWebhookEndpointConcurrencyRequest | UpdateWebhookEndpointRateRequest | UpdateWebhookEndpointAutoDisableRequest;

export interface UpdateWebhookEndpointConcurrencyRequest {
  "auto_disable_after_failures"?: number | null;
  "event_catalog_version"?: null;
  "events"?: null;
  "max_concurrency": number;
  "rate_limit_per_minute"?: number | null;
  "url"?: string | null;
}

export interface UpdateWebhookEndpointEventsRequest {
  "auto_disable_after_failures"?: number | null;
  "event_catalog_version"?: CustomerEventCatalogVersion | null;
  "events": ReadonlyArray<CustomerEventType>;
  "max_concurrency"?: number | null;
  "rate_limit_per_minute"?: number | null;
  "url"?: string | null;
}

export interface UpdateWebhookEndpointRateRequest {
  "auto_disable_after_failures"?: number | null;
  "event_catalog_version"?: null;
  "events"?: null;
  "max_concurrency"?: number | null;
  "rate_limit_per_minute": number;
  "url"?: string | null;
}

export type UpdateWebhookEndpointRequest = UpdateWebhookEndpointCommand;

export interface UpdateWebhookEndpointUrlRequest {
  "auto_disable_after_failures"?: number | null;
  "event_catalog_version"?: null;
  "events"?: null;
  "max_concurrency"?: number | null;
  "rate_limit_per_minute"?: number | null;
  "url": string;
}

export interface UploadBlock {
  "type": "upload";
}

export interface UploadLimitsResponse {
  "maximum_bytes": number;
  "modes": ReadonlyArray<"single" | "multipart">;
  "multipart_maximum_parts": number;
  "multipart_minimum_nonfinal_part_bytes": number;
  "multipart_minimum_parts": number;
}

export type UploadMode = "single" | "multipart";

export type UploadStatus = "initiated" | "completed" | "aborted" | "expired";

export interface UsageItemResponse {
  "meter_type": string;
  "meter_version": number;
  "metering_id": string;
  "occurred_at": string;
  "quantity": string;
}

export interface UsageResponse {
  "cost_estimate"?: null;
  "items": ReadonlyArray<UsageItemResponse>;
  "meters": ReadonlyArray<MeterQuotaResponse>;
  "period": string;
  "pricing_version"?: null;
}

export interface ValidationError {
  "ctx"?: Record<string, unknown>;
  "input"?: string;
  "loc": ReadonlyArray<string | number>;
  "msg": string;
  "type": string;
}

export type ValidationPath = "direct" | "recovery" | "none";

export interface VerificationBatchItemResponse {
  "error": ErrorResponse | null;
  "index": number;
  "status": number;
  "verification": VerificationResponse | null;
}

export interface VerificationBatchRequest {
  "items": ReadonlyArray<CreateVerificationRequest>;
}

export interface VerificationBatchResponse {
  "items": ReadonlyArray<VerificationBatchItemResponse>;
}

export interface VerificationEvidenceResponse {
  "asset_id": string | null;
  "created_at": string;
  "creator"?: CreatorDisclosureResponse | null;
  "evidence_id": string;
  "object_sha256": string;
  "overall": string;
  "policy_version": string | null;
  "publication_id": string | null;
  "receipt_id": string | null;
  "report_eligible": boolean;
  "result": Record<string, unknown>;
  "share_eligible": boolean;
  "signing_job_id": string | null;
  "storage_version_sha256": string;
  "subject_id": string;
  "subject_type": string;
  "trust_list_version": string | null;
  "validated_at": string;
  "validation_path": string | null;
  "verification_job_id": string | null;
}

export interface VerificationHistoryPageResponse {
  "items": ReadonlyArray<VerificationHistoryResponse>;
  "next_cursor": string | null;
}

export interface VerificationHistoryResponse {
  "created_at": string;
  "job_id": string | null;
  "overall": VerificationOverall;
  "policy_version": string | null;
  "source_byte_length": number | null;
  "source_media_type": HistoryMediaType | null;
  "status_vocabulary_version": C2PAStatusVocabularyVersion | null;
  "subject_type": VerificationSubjectType;
  "validated_at": string;
  "validation_path": ValidationPath | null;
  "verification_id": string;
  "verification_url": string;
}

export type VerificationOverall = "valid" | "invalid" | "indeterminate" | "recovered";

export interface VerificationResponse {
  "completed_at"?: string | null;
  "created_at": string;
  "evidence_id"?: string | null;
  "failure_reason"?: ReasonCode | null;
  "result"?: Record<string, unknown> | null;
  "state": VerifyState;
  "verification_id": string;
}

export interface VerificationShareMetadataResponse {
  "closed_at": string | null;
  "created_at": string;
  "expires_at": string | null;
  "share_id": string;
  "state": "active" | "revoked" | "unpublished";
}

export interface VerificationSharePageResponse {
  "items": ReadonlyArray<VerificationShareMetadataResponse>;
  "next_cursor": string | null;
}

export type VerificationSubjectType = "uploaded_object" | "stored_object" | "public_url" | "asset" | "manifest" | "receipt";

export interface VerifyBlock {
  "type": "verify";
}

export interface VerifyPageCheckUsage {
  "checks": number;
  "limit": number;
  "period_end": string;
  "period_start": string;
}

export interface VerifyPageColours {
  "accent"?: string | null;
  "background"?: string | null;
  "text"?: string | null;
}

export interface VerifyPageResponse {
  "check_usage"?: VerifyPageCheckUsage | null;
  "colours": VerifyPageColours;
  "created_at": string;
  "display_name": string;
  "enabled": boolean;
  "hosted_url": string;
  "logo_asset_id": string | null;
  "monthly_check_limit"?: number | null;
  "recover_own_assets": boolean;
  "slug": string;
  "updated_at": string;
  "version": number;
}

export interface VerifyPageUpdateRequest {
  "colours"?: VerifyPageColours | null;
  "display_name": string;
  "enabled"?: boolean;
  "expected_version": number;
  "logo_asset_id"?: string | null;
  "monthly_check_limit"?: number | null;
  "recover_own_assets"?: boolean;
  "slug": string;
}

export type VerifyState = "accepted" | "running" | "completed" | "failed";

export interface VideoTrackFacts {
  "codec"?: "h264";
  "codec_profile": string;
  "decoded_byte_length": number;
  "duration_microseconds": number;
  "fps_denominator": number;
  "fps_numerator": number;
  "frame_count": number;
  "height": number;
  "pixel_format": string;
  "stream_index": number;
  "time_base_denominator": number;
  "time_base_numerator": number;
  "width": number;
}

export interface WalletAutoRecharge {
  "amount_usd": string | null;
  "enabled": boolean;
  "threshold_usd": string | null;
}

export interface WalletAutoRechargeRequest {
  "amount_usd"?: number | string | null;
  "enabled": boolean;
  "threshold_usd"?: number | string | null;
}

export interface WalletResponse {
  "auto_recharge": WalletAutoRecharge;
  "balance_usd": string;
  "currency"?: "USD";
  "enabled": boolean;
  "month_to_date_spend_usd": string;
  "monthly_spend_limit_usd": string | null;
  "recharge_pending": boolean;
  "reserved_usd": string;
  "top_up_max_usd": string;
  "top_up_min_usd": string;
  "transactions": ReadonlyArray<WalletTransactionResponse>;
  "version": number;
}

export interface WalletSettingsRequest {
  "auto_recharge": WalletAutoRechargeRequest;
  "enabled"?: boolean;
  "expected_version": number;
  "monthly_spend_limit_usd"?: number | string | null;
}

export interface WalletTransactionResponse {
  "amount_usd": string;
  "balance_after_usd": string;
  "created_at": string;
  "id": string;
  "kind": "top_up" | "charge" | "refund" | "adjustment";
}

export interface WatermarkAlgorithmResponse {
  "algorithm_id": string;
  "default": boolean;
  "display_name": string;
  "false_match_rate_upper_bound"?: number | null;
  "payload_bits": number;
  "quality": Record<string, number>;
  "recommended": boolean;
  "robustness_attack"?: string | null;
  "robustness_bit_accuracy"?: number | null;
  "soft_binding": "registered" | "unregistered";
  "soft_binding_registry_id"?: number | null;
  "strength_levels": WatermarkStrengthLevelsResponse;
  "strengths": ReadonlyArray<number>;
}

export interface WatermarkBlock {
  "algorithm"?: "audioseal" | "audioseal-mm02-4" | "pixelseal" | "pixelseal-video" | "trustmark-b" | "trustmark-c" | "trustmark-p" | "trustmark-q" | "videoseal" | "videoseal-image" | null;
  "strength"?: "subtle" | "balanced" | "robust" | null;
  "type": "watermark";
}

export interface WatermarkStrengthLevelsResponse {
  "balanced": ReadonlyArray<number>;
  "robust": ReadonlyArray<number>;
  "subtle": ReadonlyArray<number>;
}

export interface WebhookAck {
  "duplicate"?: boolean;
  "result": string;
  "status": string;
}

export interface WebhookAttemptPageResponse {
  "data": ReadonlyArray<WebhookAttemptResponse>;
  "next_cursor"?: string | null;
}

export interface WebhookAttemptResponse {
  "attempt_no": number;
  "failure_class": string | null;
  "fencing_token": number;
  "occurred_at": string;
  "outcome": "dispatch_started" | "delivered" | "retrying" | "dead" | "stale_delivered" | "stale_failed";
  "phase": "dispatch_started" | "result";
  "replay_generation": number | null;
  "response_body_sha256": string | null;
  "response_code": number | null;
}

export interface WebhookBlock {
  "endpoint_id"?: string | null;
  "type": "webhook";
}

export interface WebhookDeliveryPageResponse {
  "data": ReadonlyArray<WebhookDeliveryResponse>;
  "next_cursor"?: string | null;
}

export interface WebhookDeliveryResponse {
  "attempt_count": number;
  "created_at": string;
  "delivery_id": string;
  "event_id": string;
  "event_type": CustomerEventType | "webhook.test";
  "next_attempt_at": string | null;
  "replay_count": number;
  "response_body_sha256": string | null;
  "response_code": number | null;
  "status": "pending" | "delivering" | "delivered" | "failed" | "dead";
  "terminal_reason": WebhookDeliveryTerminalReason | null;
}

export type WebhookDeliveryTerminalReason = "automatic_failure_threshold" | "customer_deleted" | "customer_disabled" | "payload_invalid" | "retryable_http" | "secret_invalid" | "terminal_http" | "transport_rejected" | "transport_unavailable";

export type WebhookDisabledReason = "manual" | "consecutive_failures";

export interface WebhookEndpointPageResponse {
  "data": ReadonlyArray<WebhookEndpointResponse>;
  "next_cursor"?: string | null;
}

export interface WebhookEndpointResponse {
  "auto_disable_after_failures": number;
  "consecutive_failures"?: number;
  "created_at": string;
  "deleted_at"?: string | null;
  "disabled_at"?: string | null;
  "disabled_reason"?: WebhookDisabledReason | null;
  "endpoint_id": string;
  "event_catalog_version": CustomerEventCatalogVersion;
  "events": ReadonlyArray<CustomerEventType>;
  "max_concurrency": number;
  "rate_limit_per_minute": number;
  "signing_secrets"?: ReadonlyArray<WebhookSecretLifecycleResponse>;
  "status": "active" | "disabled" | "deleted";
  "triggering_delivery_id"?: string | null;
  "updated_at": string;
  "url": string;
}

export interface WebhookReplayResponse {
  "delivery_count": number;
  "event_id": string;
}

export interface WebhookSecretLifecycleResponse {
  "created_at": string;
  "retire_at"?: string | null;
  "status": WebhookSecretLifecycleStatus;
  "version": number;
}

export type WebhookSecretLifecycleStatus = "active" | "retiring";

export interface WebhookTestEventResponse {
  "delivery_id": string;
  "event_id": string;
  "event_type": "webhook.test";
}

export interface WorkflowSignRequestFields {
  "ai_declaration"?: AiDeclarationRequest | null;
  "creator_id"?: string | null;
  "fingerprint": boolean;
  "fingerprint_algorithms"?: ReadonlyArray<string> | null;
  "identity"?: SignIdentityRequest | null;
  "mode"?: "standard" | "express" | null;
  "watermark": boolean;
  "watermark_algorithm"?: string | null;
  "watermark_strength"?: "subtle" | "balanced" | "robust" | null;
}

export interface WorkflowTemplateListResponse {
  "data": ReadonlyArray<WorkflowTemplateResponse>;
}

export interface WorkflowTemplateReplaceRequest {
  "blocks": ReadonlyArray<UploadBlock | WatermarkBlock | FingerprintBlock | AiMarkBlock | CawgIdentityBlock | SignBlock | VerifyBlock | WebhookBlock | DisclosureEventBlock>;
  "description"?: string | null;
  "expected_version": number;
  "name": string;
}

export interface WorkflowTemplateRequest {
  "blocks": ReadonlyArray<UploadBlock | WatermarkBlock | FingerprintBlock | AiMarkBlock | CawgIdentityBlock | SignBlock | VerifyBlock | WebhookBlock | DisclosureEventBlock>;
  "description"?: string | null;
  "name": string;
}

export interface WorkflowTemplateResponse {
  "blocks": ReadonlyArray<UploadBlock | WatermarkBlock | FingerprintBlock | AiMarkBlock | CawgIdentityBlock | SignBlock | VerifyBlock | WebhookBlock | DisclosureEventBlock>;
  "created_at": string;
  "description": string | null;
  "name": string;
  "schema_version": "op.workflow-template.v1";
  "sign_request": WorkflowSignRequestFields;
  "template_id": string;
  "updated_at": string;
  "version": number;
}

export interface WorkspaceGovernanceResponse {
  "deletion_state": AssetDeletionState | null;
  "legal_hold_active": boolean;
}

export type GetHealthzParameters = Record<string, never>;

export type GetHealthzHeaders = Record<string, never>;

export type GetHealthzRequestBody = null;
export type GetHealthzSuccessResponse = HealthResponse;

export interface GetHealthzResponses {
  "200": HealthResponse;
}

export interface GetHealthzSuccessResponses {
  "200": HealthResponse;
}

export type GetHealthzErrorResponses = Record<string, never>;

export type GetDatabaseHealthParameters = Record<string, never>;

export type GetDatabaseHealthHeaders = Record<string, never>;

export type GetDatabaseHealthRequestBody = null;
export type GetDatabaseHealthSuccessResponse = DbHealthResponse;

export interface GetDatabaseHealthResponses {
  "200": DbHealthResponse;
}

export interface GetDatabaseHealthSuccessResponses {
  "200": DbHealthResponse;
}

export type GetDatabaseHealthErrorResponses = Record<string, never>;

export type GetReadyzParameters = Record<string, never>;

export type GetReadyzHeaders = Record<string, never>;

export type GetReadyzRequestBody = null;
export type GetReadyzSuccessResponse = ReadinessResponse;

export interface GetReadyzResponses {
  "200": ReadinessResponse;
  "503": ReadinessResponse;
}

export interface GetReadyzSuccessResponses {
  "200": ReadinessResponse;
}

export interface GetReadyzErrorResponses {
  "503": ReadinessResponse;
}

export type GetGovernanceReadyzParameters = Record<string, never>;

export type GetGovernanceReadyzHeaders = Record<string, never>;

export type GetGovernanceReadyzRequestBody = null;
export type GetGovernanceReadyzSuccessResponse = GovernanceReadinessResponse;

export interface GetGovernanceReadyzResponses {
  "200": GovernanceReadinessResponse;
  "503": GovernanceReadinessResponse;
}

export interface GetGovernanceReadyzSuccessResponses {
  "200": GovernanceReadinessResponse;
}

export interface GetGovernanceReadyzErrorResponses {
  "503": GovernanceReadinessResponse;
}

export type ListApiKeysParameters = Record<string, never>;

export type ListApiKeysHeaders = Record<string, never>;

export type ListApiKeysRequestBody = null;
export type ListApiKeysSuccessResponse = ApiKeyListResponse;

export interface ListApiKeysResponses {
  "200": ApiKeyListResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface ListApiKeysSuccessResponses {
  "200": ApiKeyListResponse;
}

export interface ListApiKeysErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export type CreateApiKeyParameters = Record<string, never>;

export interface CreateApiKeyHeaders {
  "Idempotency-Key": string;
}

export type CreateApiKeyRequestBody = ApiKeyCreateRequest;
export type CreateApiKeySuccessResponse = IssuedApiKeyResponse;

export interface CreateApiKeyResponses {
  "201": IssuedApiKeyResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface CreateApiKeySuccessResponses {
  "201": IssuedApiKeyResponse;
}

export interface CreateApiKeyErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface RevokeApiKeyParameters {
  "api_key_id": string;
}

export interface RevokeApiKeyHeaders {
  "Idempotency-Key": string;
}

export type RevokeApiKeyRequestBody = null;
export type RevokeApiKeySuccessResponse = ApiKeyMetadataResponse;

export interface RevokeApiKeyResponses {
  "200": ApiKeyMetadataResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface RevokeApiKeySuccessResponses {
  "200": ApiKeyMetadataResponse;
}

export interface RevokeApiKeyErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetApiKeyParameters {
  "api_key_id": string;
}

export type GetApiKeyHeaders = Record<string, never>;

export type GetApiKeyRequestBody = null;
export type GetApiKeySuccessResponse = ApiKeyMetadataResponse;

export interface GetApiKeyResponses {
  "200": ApiKeyMetadataResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetApiKeySuccessResponses {
  "200": ApiKeyMetadataResponse;
}

export interface GetApiKeyErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetApiKeyRestrictionsParameters {
  "api_key_id": string;
}

export type GetApiKeyRestrictionsHeaders = Record<string, never>;

export type GetApiKeyRestrictionsRequestBody = null;
export type GetApiKeyRestrictionsSuccessResponse = ApiKeyRestrictionsResponse;

export interface GetApiKeyRestrictionsResponses {
  "200": ApiKeyRestrictionsResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetApiKeyRestrictionsSuccessResponses {
  "200": ApiKeyRestrictionsResponse;
}

export interface GetApiKeyRestrictionsErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface SetApiKeyRestrictionsParameters {
  "api_key_id": string;
}

export type SetApiKeyRestrictionsHeaders = Record<string, never>;

export type SetApiKeyRestrictionsRequestBody = ApiKeyRestrictionsUpdateRequest;
export type SetApiKeyRestrictionsSuccessResponse = ApiKeyRestrictionsResponse;

export interface SetApiKeyRestrictionsResponses {
  "200": ApiKeyRestrictionsResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface SetApiKeyRestrictionsSuccessResponses {
  "200": ApiKeyRestrictionsResponse;
}

export interface SetApiKeyRestrictionsErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetApiKeyRetentionParameters {
  "api_key_id": string;
}

export type GetApiKeyRetentionHeaders = Record<string, never>;

export type GetApiKeyRetentionRequestBody = null;
export type GetApiKeyRetentionSuccessResponse = ApiKeyRetentionResponse;

export interface GetApiKeyRetentionResponses {
  "200": ApiKeyRetentionResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetApiKeyRetentionSuccessResponses {
  "200": ApiKeyRetentionResponse;
}

export interface GetApiKeyRetentionErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface SetApiKeyRetentionParameters {
  "api_key_id": string;
}

export type SetApiKeyRetentionHeaders = Record<string, never>;

export type SetApiKeyRetentionRequestBody = ApiKeyRetentionRequest;
export type SetApiKeyRetentionSuccessResponse = ApiKeyRetentionResponse;

export interface SetApiKeyRetentionResponses {
  "200": ApiKeyRetentionResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface SetApiKeyRetentionSuccessResponses {
  "200": ApiKeyRetentionResponse;
}

export interface SetApiKeyRetentionErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface RotateApiKeyParameters {
  "api_key_id": string;
}

export interface RotateApiKeyHeaders {
  "Idempotency-Key": string;
}

export type RotateApiKeyRequestBody = ApiKeyRotateRequest;
export type RotateApiKeySuccessResponse = IssuedApiKeyResponse;

export interface RotateApiKeyResponses {
  "201": IssuedApiKeyResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface RotateApiKeySuccessResponses {
  "201": IssuedApiKeyResponse;
}

export interface RotateApiKeyErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface CancelApiKeyRotationParameters {
  "api_key_id": string;
}

export interface CancelApiKeyRotationHeaders {
  "Idempotency-Key": string;
}

export type CancelApiKeyRotationRequestBody = null;
export type CancelApiKeyRotationSuccessResponse = ApiKeyMetadataResponse;

export interface CancelApiKeyRotationResponses {
  "200": ApiKeyMetadataResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface CancelApiKeyRotationSuccessResponses {
  "200": ApiKeyMetadataResponse;
}

export interface CancelApiKeyRotationErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface CompleteApiKeyRotationParameters {
  "api_key_id": string;
}

export interface CompleteApiKeyRotationHeaders {
  "Idempotency-Key": string;
}

export type CompleteApiKeyRotationRequestBody = null;
export type CompleteApiKeyRotationSuccessResponse = ApiKeyMetadataResponse;

export interface CompleteApiKeyRotationResponses {
  "200": ApiKeyMetadataResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface CompleteApiKeyRotationSuccessResponses {
  "200": ApiKeyMetadataResponse;
}

export interface CompleteApiKeyRotationErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetApiKeySigningProfileParameters {
  "api_key_id": string;
}

export type GetApiKeySigningProfileHeaders = Record<string, never>;

export type GetApiKeySigningProfileRequestBody = null;
export type GetApiKeySigningProfileSuccessResponse = ApiKeySigningProfileResponse;

export interface GetApiKeySigningProfileResponses {
  "200": ApiKeySigningProfileResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetApiKeySigningProfileSuccessResponses {
  "200": ApiKeySigningProfileResponse;
}

export interface GetApiKeySigningProfileErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface SetApiKeySigningProfileParameters {
  "api_key_id": string;
}

export type SetApiKeySigningProfileHeaders = Record<string, never>;

export type SetApiKeySigningProfileRequestBody = ApiKeySigningProfileUpdateRequest;
export type SetApiKeySigningProfileSuccessResponse = ApiKeySigningProfileResponse;

export interface SetApiKeySigningProfileResponses {
  "200": ApiKeySigningProfileResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface SetApiKeySigningProfileSuccessResponses {
  "200": ApiKeySigningProfileResponse;
}

export interface SetApiKeySigningProfileErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export type ListApiKeyScopesParameters = Record<string, never>;

export type ListApiKeyScopesHeaders = Record<string, never>;

export type ListApiKeyScopesRequestBody = null;
export type ListApiKeyScopesSuccessResponse = ApiKeyScopeCatalogResponse;

export interface ListApiKeyScopesResponses {
  "200": ApiKeyScopeCatalogResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface ListApiKeyScopesSuccessResponses {
  "200": ApiKeyScopeCatalogResponse;
}

export interface ListApiKeyScopesErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface ListApiRequestLogsParameters {
  "api_key_id"?: string | null;
  "status_class"?: StatusClass | null;
  "route"?: string | null;
  "cursor"?: string | null;
  "limit"?: number;
}

export type ListApiRequestLogsHeaders = Record<string, never>;

export type ListApiRequestLogsRequestBody = null;
export type ListApiRequestLogsSuccessResponse = ApiRequestLogPageResponse;

export interface ListApiRequestLogsResponses {
  "200": ApiRequestLogPageResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface ListApiRequestLogsSuccessResponses {
  "200": ApiRequestLogPageResponse;
}

export interface ListApiRequestLogsErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface SummarizeApiRequestLogsParameters {
  "window"?: SummaryWindow;
}

export type SummarizeApiRequestLogsHeaders = Record<string, never>;

export type SummarizeApiRequestLogsRequestBody = null;
export type SummarizeApiRequestLogsSuccessResponse = ApiRequestLogSummaryResponse;

export interface SummarizeApiRequestLogsResponses {
  "200": ApiRequestLogSummaryResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface SummarizeApiRequestLogsSuccessResponses {
  "200": ApiRequestLogSummaryResponse;
}

export interface SummarizeApiRequestLogsErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface ListAssetsParameters {
  "kind"?: AssetHistoryKind | null;
  "status"?: AssetHistoryStatus | null;
  "media"?: AssetMediaFamily | null;
  "from"?: string | null;
  "recipe_id"?: string | null;
  "verification_outcome"?: VerificationOverall | null;
  "cursor"?: string | null;
  "limit"?: number;
}

export type ListAssetsHeaders = Record<string, never>;

export type ListAssetsRequestBody = null;
export type ListAssetsSuccessResponse = AssetHistoryPageResponse;

export interface ListAssetsResponses {
  "200": AssetHistoryPageResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface ListAssetsSuccessResponses {
  "200": AssetHistoryPageResponse;
}

export interface ListAssetsErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface GetAssetParameters {
  "asset_id": string;
}

export type GetAssetHeaders = Record<string, never>;

export type GetAssetRequestBody = null;
export type GetAssetSuccessResponse = AssetResponse;

export interface GetAssetResponses {
  "200": AssetResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface GetAssetSuccessResponses {
  "200": AssetResponse;
}

export interface GetAssetErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface GetAssetDetailParameters {
  "asset_id": string;
  "verification_cursor"?: string | null;
  "activity_cursor"?: string | null;
  "limit"?: number;
}

export type GetAssetDetailHeaders = Record<string, never>;

export type GetAssetDetailRequestBody = null;
export type GetAssetDetailSuccessResponse = AssetDetailResponse;

export interface GetAssetDetailResponses {
  "200": AssetDetailResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface GetAssetDetailSuccessResponses {
  "200": AssetDetailResponse;
}

export interface GetAssetDetailErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface CreateAssetDownloadParameters {
  "asset_id": string;
}

export type CreateAssetDownloadHeaders = Record<string, never>;

export type CreateAssetDownloadRequestBody = null;
export type CreateAssetDownloadSuccessResponse = DownloadResponse;

export interface CreateAssetDownloadResponses {
  "200": DownloadResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface CreateAssetDownloadSuccessResponses {
  "200": DownloadResponse;
}

export interface CreateAssetDownloadErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface CreateAssetPreviewParameters {
  "asset_id": string;
}

export type CreateAssetPreviewHeaders = Record<string, never>;

export type CreateAssetPreviewRequestBody = null;
export type CreateAssetPreviewSuccessResponse = PreviewResponse;

export interface CreateAssetPreviewResponses {
  "200": PreviewResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface CreateAssetPreviewSuccessResponses {
  "200": PreviewResponse;
}

export interface CreateAssetPreviewErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface RedeemAssetPreviewParameters {
  "asset_id": string;
  "capability": string;
}

export type RedeemAssetPreviewHeaders = Record<string, never>;

export type RedeemAssetPreviewRequestBody = null;
export type RedeemAssetPreviewSuccessResponse = null;

export interface RedeemAssetPreviewResponses {
  "200": null;
  "404": ErrorResponse;
}

export interface RedeemAssetPreviewSuccessResponses {
  "200": null;
}

export interface RedeemAssetPreviewErrorResponses {
  "404": ErrorResponse;
}

export type GetBillingAccountParameters = Record<string, never>;

export type GetBillingAccountHeaders = Record<string, never>;

export type GetBillingAccountRequestBody = null;
export type GetBillingAccountSuccessResponse = BillingAccountResponse;

export interface GetBillingAccountResponses {
  "200": BillingAccountResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetBillingAccountSuccessResponses {
  "200": BillingAccountResponse;
}

export interface GetBillingAccountErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface ListBillingChargesParameters {
  "limit"?: number;
  "before"?: string | null;
}

export type ListBillingChargesHeaders = Record<string, never>;

export type ListBillingChargesRequestBody = null;
export type ListBillingChargesSuccessResponse = ProcessingChargesResponse;

export interface ListBillingChargesResponses {
  "200": ProcessingChargesResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface ListBillingChargesSuccessResponses {
  "200": ProcessingChargesResponse;
}

export interface ListBillingChargesErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export type CreateBillingCheckoutIntentParameters = Record<string, never>;

export type CreateBillingCheckoutIntentHeaders = Record<string, never>;

export type CreateBillingCheckoutIntentRequestBody = CheckoutIntentRequest;
export type CreateBillingCheckoutIntentSuccessResponse = BillingIntentResponse;

export interface CreateBillingCheckoutIntentResponses {
  "201": BillingIntentResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "502": HttpErrorResponse;
  "503": HttpErrorResponse;
}

export interface CreateBillingCheckoutIntentSuccessResponses {
  "201": BillingIntentResponse;
}

export interface CreateBillingCheckoutIntentErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "502": HttpErrorResponse;
  "503": HttpErrorResponse;
}

export interface ListBillingInvoicesParameters {
  "limit"?: number;
  "before"?: string | null;
}

export type ListBillingInvoicesHeaders = Record<string, never>;

export type ListBillingInvoicesRequestBody = null;
export type ListBillingInvoicesSuccessResponse = BillingInvoicesResponse;

export interface ListBillingInvoicesResponses {
  "200": BillingInvoicesResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface ListBillingInvoicesSuccessResponses {
  "200": BillingInvoicesResponse;
}

export interface ListBillingInvoicesErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export type GetBillingPlansParameters = Record<string, never>;

export type GetBillingPlansHeaders = Record<string, never>;

export type GetBillingPlansRequestBody = null;
export type GetBillingPlansSuccessResponse = BillingPlansResponse;

export interface GetBillingPlansResponses {
  "200": BillingPlansResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetBillingPlansSuccessResponses {
  "200": BillingPlansResponse;
}

export interface GetBillingPlansErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export type CreateBillingPortalIntentParameters = Record<string, never>;

export type CreateBillingPortalIntentHeaders = Record<string, never>;

export type CreateBillingPortalIntentRequestBody = PortalIntentRequest;
export type CreateBillingPortalIntentSuccessResponse = BillingIntentResponse;

export interface CreateBillingPortalIntentResponses {
  "201": BillingIntentResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "502": HttpErrorResponse;
  "503": HttpErrorResponse;
}

export interface CreateBillingPortalIntentSuccessResponses {
  "201": BillingIntentResponse;
}

export interface CreateBillingPortalIntentErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "502": HttpErrorResponse;
  "503": HttpErrorResponse;
}

export type GetBillingPricingParameters = Record<string, never>;

export type GetBillingPricingHeaders = Record<string, never>;

export type GetBillingPricingRequestBody = null;
export type GetBillingPricingSuccessResponse = PricingResponse;

export interface GetBillingPricingResponses {
  "200": PricingResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetBillingPricingSuccessResponses {
  "200": PricingResponse;
}

export interface GetBillingPricingErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export type CreateBillingQuoteParameters = Record<string, never>;

export type CreateBillingQuoteHeaders = Record<string, never>;

export type CreateBillingQuoteRequestBody = PricingQuoteRequest;
export type CreateBillingQuoteSuccessResponse = PricingQuoteResponse;

export interface CreateBillingQuoteResponses {
  "200": PricingQuoteResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface CreateBillingQuoteSuccessResponses {
  "200": PricingQuoteResponse;
}

export interface CreateBillingQuoteErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export type GetBillingWalletParameters = Record<string, never>;

export type GetBillingWalletHeaders = Record<string, never>;

export type GetBillingWalletRequestBody = null;
export type GetBillingWalletSuccessResponse = WalletResponse;

export interface GetBillingWalletResponses {
  "200": WalletResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetBillingWalletSuccessResponses {
  "200": WalletResponse;
}

export interface GetBillingWalletErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export type SetBillingWalletSettingsParameters = Record<string, never>;

export type SetBillingWalletSettingsHeaders = Record<string, never>;

export type SetBillingWalletSettingsRequestBody = WalletSettingsRequest;
export type SetBillingWalletSettingsSuccessResponse = WalletResponse;

export interface SetBillingWalletSettingsResponses {
  "200": WalletResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface SetBillingWalletSettingsSuccessResponses {
  "200": WalletResponse;
}

export interface SetBillingWalletSettingsErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export type GetCapabilitiesParameters = Record<string, never>;

export type GetCapabilitiesHeaders = Record<string, never>;

export type GetCapabilitiesRequestBody = null;
export type GetCapabilitiesSuccessResponse = CapabilityDiscoveryResponse;

export interface GetCapabilitiesResponses {
  "200": CapabilityDiscoveryResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetCapabilitiesSuccessResponses {
  "200": CapabilityDiscoveryResponse;
}

export interface GetCapabilitiesErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export type CreateCaptureAdmissionChallengeParameters = Record<string, never>;

export interface CreateCaptureAdmissionChallengeHeaders {
  "Idempotency-Key": string;
}

export type CreateCaptureAdmissionChallengeRequestBody = CaptureAdmissionChallengeRequest;
export type CreateCaptureAdmissionChallengeSuccessResponse = CaptureAdmissionChallengeResponse;

export interface CreateCaptureAdmissionChallengeResponses {
  "201": CaptureAdmissionChallengeResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": CaptureManagementErrorResponse;
  "409": HttpErrorResponse | CaptureManagementErrorResponse;
  "422": HttpErrorResponse | CaptureManagementErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | CaptureManagementErrorResponse;
}

export interface CreateCaptureAdmissionChallengeSuccessResponses {
  "201": CaptureAdmissionChallengeResponse;
}

export interface CreateCaptureAdmissionChallengeErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": CaptureManagementErrorResponse;
  "409": HttpErrorResponse | CaptureManagementErrorResponse;
  "422": HttpErrorResponse | CaptureManagementErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | CaptureManagementErrorResponse;
}

export interface ListCaptureAdmissionsParameters {
  "decision"?: CaptureAdmissionDecision | null;
  "capture_identity_id"?: string | null;
  "decided_from"?: string | null;
  "decided_through"?: string | null;
  "cursor"?: string | null;
  "limit"?: number | null;
}

export type ListCaptureAdmissionsHeaders = Record<string, never>;

export type ListCaptureAdmissionsRequestBody = null;
export type ListCaptureAdmissionsSuccessResponse = CaptureAdmissionListResponse;

export interface ListCaptureAdmissionsResponses {
  "200": CaptureAdmissionListResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": CaptureManagementErrorResponse;
  "409": HttpErrorResponse | CaptureManagementErrorResponse;
  "422": HttpErrorResponse | CaptureManagementErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | CaptureManagementErrorResponse;
}

export interface ListCaptureAdmissionsSuccessResponses {
  "200": CaptureAdmissionListResponse;
}

export interface ListCaptureAdmissionsErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": CaptureManagementErrorResponse;
  "409": HttpErrorResponse | CaptureManagementErrorResponse;
  "422": HttpErrorResponse | CaptureManagementErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | CaptureManagementErrorResponse;
}

export type CreateCaptureAdmissionParameters = Record<string, never>;

export type CreateCaptureAdmissionHeaders = Record<string, never>;

export type CreateCaptureAdmissionRequestBody = CaptureAdmissionSubmissionRequest;
export type CreateCaptureAdmissionSuccessResponse = CaptureAdmissionSubmissionResponse;

export interface CreateCaptureAdmissionResponses {
  "200": CaptureAdmissionSubmissionResponse;
  "201": CaptureAdmissionSubmissionResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": CaptureManagementErrorResponse;
  "409": HttpErrorResponse | CaptureManagementErrorResponse;
  "422": HttpErrorResponse | CaptureManagementErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | CaptureManagementErrorResponse;
}

export interface CreateCaptureAdmissionSuccessResponses {
  "200": CaptureAdmissionSubmissionResponse;
  "201": CaptureAdmissionSubmissionResponse;
}

export interface CreateCaptureAdmissionErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": CaptureManagementErrorResponse;
  "409": HttpErrorResponse | CaptureManagementErrorResponse;
  "422": HttpErrorResponse | CaptureManagementErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | CaptureManagementErrorResponse;
}

export interface GetCaptureAdmissionParameters {
  "capture_admission_id": string;
}

export interface GetCaptureAdmissionHeaders {
  "If-None-Match"?: string | null;
}

export type GetCaptureAdmissionRequestBody = null;
export type GetCaptureAdmissionSuccessResponse = CaptureAdmissionDetail;

export interface GetCaptureAdmissionResponses {
  "200": CaptureAdmissionDetail;
  "304": null;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": CaptureManagementErrorResponse;
  "409": HttpErrorResponse | CaptureManagementErrorResponse;
  "422": HttpErrorResponse | CaptureManagementErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | CaptureManagementErrorResponse;
}

export interface GetCaptureAdmissionSuccessResponses {
  "200": CaptureAdmissionDetail;
}

export interface GetCaptureAdmissionErrorResponses {
  "304": null;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": CaptureManagementErrorResponse;
  "409": HttpErrorResponse | CaptureManagementErrorResponse;
  "422": HttpErrorResponse | CaptureManagementErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | CaptureManagementErrorResponse;
}

export interface ListCaptureIdentitiesParameters {
  "state"?: CaptureIdentityFilterState | null;
  "platform"?: CaptureIdentityPlatform | null;
  "provider_class"?: CaptureProviderClass | null;
  "cursor"?: string | null;
  "limit"?: number | null;
}

export type ListCaptureIdentitiesHeaders = Record<string, never>;

export type ListCaptureIdentitiesRequestBody = null;
export type ListCaptureIdentitiesSuccessResponse = CaptureIdentityListResponse;

export interface ListCaptureIdentitiesResponses {
  "200": CaptureIdentityListResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": CaptureManagementErrorResponse;
  "409": HttpErrorResponse | CaptureManagementErrorResponse;
  "422": HttpErrorResponse | CaptureManagementErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | CaptureManagementErrorResponse;
}

export interface ListCaptureIdentitiesSuccessResponses {
  "200": CaptureIdentityListResponse;
}

export interface ListCaptureIdentitiesErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": CaptureManagementErrorResponse;
  "409": HttpErrorResponse | CaptureManagementErrorResponse;
  "422": HttpErrorResponse | CaptureManagementErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | CaptureManagementErrorResponse;
}

export type CreateCaptureIdentityParameters = Record<string, never>;

export type CreateCaptureIdentityHeaders = Record<string, never>;

export type CreateCaptureIdentityRequestBody = CaptureIdentityCreationRequest;
export type CreateCaptureIdentitySuccessResponse = CaptureIdentityEnrollmentResult;

export interface CreateCaptureIdentityResponses {
  "200": CaptureIdentityEnrollmentResult;
  "201": CaptureIdentityEnrollmentResult;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": CaptureManagementErrorResponse;
  "409": HttpErrorResponse | CaptureManagementErrorResponse;
  "422": HttpErrorResponse | CaptureManagementErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | CaptureManagementErrorResponse;
}

export interface CreateCaptureIdentitySuccessResponses {
  "200": CaptureIdentityEnrollmentResult;
  "201": CaptureIdentityEnrollmentResult;
}

export interface CreateCaptureIdentityErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": CaptureManagementErrorResponse;
  "409": HttpErrorResponse | CaptureManagementErrorResponse;
  "422": HttpErrorResponse | CaptureManagementErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | CaptureManagementErrorResponse;
}

export interface GetCaptureIdentityParameters {
  "capture_identity_id": string;
}

export interface GetCaptureIdentityHeaders {
  "If-None-Match"?: string | null;
}

export type GetCaptureIdentityRequestBody = null;
export type GetCaptureIdentitySuccessResponse = CaptureIdentityDetail;

export interface GetCaptureIdentityResponses {
  "200": CaptureIdentityDetail;
  "304": null;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": CaptureManagementErrorResponse;
  "409": HttpErrorResponse | CaptureManagementErrorResponse;
  "422": HttpErrorResponse | CaptureManagementErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | CaptureManagementErrorResponse;
}

export interface GetCaptureIdentitySuccessResponses {
  "200": CaptureIdentityDetail;
}

export interface GetCaptureIdentityErrorResponses {
  "304": null;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": CaptureManagementErrorResponse;
  "409": HttpErrorResponse | CaptureManagementErrorResponse;
  "422": HttpErrorResponse | CaptureManagementErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | CaptureManagementErrorResponse;
}

export interface RevokeCaptureIdentityParameters {
  "capture_identity_id": string;
}

export type RevokeCaptureIdentityHeaders = Record<string, never>;

export type RevokeCaptureIdentityRequestBody = null;
export type RevokeCaptureIdentitySuccessResponse = CaptureIdentityRevocationResponse;

export interface RevokeCaptureIdentityResponses {
  "200": CaptureIdentityRevocationResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": CaptureManagementErrorResponse;
  "409": HttpErrorResponse | CaptureManagementErrorResponse;
  "422": HttpErrorResponse | CaptureManagementErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | CaptureManagementErrorResponse;
}

export interface RevokeCaptureIdentitySuccessResponses {
  "200": CaptureIdentityRevocationResponse;
}

export interface RevokeCaptureIdentityErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": CaptureManagementErrorResponse;
  "409": HttpErrorResponse | CaptureManagementErrorResponse;
  "422": HttpErrorResponse | CaptureManagementErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | CaptureManagementErrorResponse;
}

export type CreateCaptureIdentityEnrollmentParameters = Record<string, never>;

export interface CreateCaptureIdentityEnrollmentHeaders {
  "Idempotency-Key": string;
}

export type CreateCaptureIdentityEnrollmentRequestBody = CaptureIdentityEnrollmentRequest;
export type CreateCaptureIdentityEnrollmentSuccessResponse = CaptureIdentityEnrollmentResponse;

export interface CreateCaptureIdentityEnrollmentResponses {
  "201": CaptureIdentityEnrollmentResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": CaptureManagementErrorResponse;
  "409": HttpErrorResponse | CaptureManagementErrorResponse;
  "422": HttpErrorResponse | CaptureManagementErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | CaptureManagementErrorResponse;
}

export interface CreateCaptureIdentityEnrollmentSuccessResponses {
  "201": CaptureIdentityEnrollmentResponse;
}

export interface CreateCaptureIdentityEnrollmentErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": CaptureManagementErrorResponse;
  "409": HttpErrorResponse | CaptureManagementErrorResponse;
  "422": HttpErrorResponse | CaptureManagementErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | CaptureManagementErrorResponse;
}

export type GetConnectCatalogParameters = Record<string, never>;

export type GetConnectCatalogHeaders = Record<string, never>;

export type GetConnectCatalogRequestBody = null;
export type GetConnectCatalogSuccessResponse = ConnectCatalogResponse;

export interface GetConnectCatalogResponses {
  "200": ConnectCatalogResponse;
}

export interface GetConnectCatalogSuccessResponses {
  "200": ConnectCatalogResponse;
}

export type GetConnectCatalogErrorResponses = Record<string, never>;

export type GetCreatorDisclosurePolicyParameters = Record<string, never>;

export type GetCreatorDisclosurePolicyHeaders = Record<string, never>;

export type GetCreatorDisclosurePolicyRequestBody = null;
export type GetCreatorDisclosurePolicySuccessResponse = CreatorDisclosurePolicyResponse;

export interface GetCreatorDisclosurePolicyResponses {
  "200": CreatorDisclosurePolicyResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetCreatorDisclosurePolicySuccessResponses {
  "200": CreatorDisclosurePolicyResponse;
}

export interface GetCreatorDisclosurePolicyErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export type UpdateCreatorDisclosurePolicyParameters = Record<string, never>;

export type UpdateCreatorDisclosurePolicyHeaders = Record<string, never>;

export type UpdateCreatorDisclosurePolicyRequestBody = CreatorDisclosurePolicyRequest;
export type UpdateCreatorDisclosurePolicySuccessResponse = CreatorDisclosurePolicyResponse;

export interface UpdateCreatorDisclosurePolicyResponses {
  "200": CreatorDisclosurePolicyResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface UpdateCreatorDisclosurePolicySuccessResponses {
  "200": CreatorDisclosurePolicyResponse;
}

export interface UpdateCreatorDisclosurePolicyErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface ListCreatorIdentitiesParameters {
  "state"?: "active" | "withdrawn" | "erased" | null;
  "cursor"?: string | null;
  "limit"?: number | null;
}

export type ListCreatorIdentitiesHeaders = Record<string, never>;

export type ListCreatorIdentitiesRequestBody = null;
export type ListCreatorIdentitiesSuccessResponse = CreatorIdentityListResponse;

export interface ListCreatorIdentitiesResponses {
  "200": CreatorIdentityListResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface ListCreatorIdentitiesSuccessResponses {
  "200": CreatorIdentityListResponse;
}

export interface ListCreatorIdentitiesErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export type CreateCreatorIdentityParameters = Record<string, never>;

export interface CreateCreatorIdentityHeaders {
  "Idempotency-Key": string;
}

export type CreateCreatorIdentityRequestBody = CreatorIdentityCreateRequest;
export type CreateCreatorIdentitySuccessResponse = CreatorIdentityResponse;

export interface CreateCreatorIdentityResponses {
  "201": CreatorIdentityResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface CreateCreatorIdentitySuccessResponses {
  "201": CreatorIdentityResponse;
}

export interface CreateCreatorIdentityErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface GetCreatorIdentityParameters {
  "creator_identity_id": string;
}

export type GetCreatorIdentityHeaders = Record<string, never>;

export type GetCreatorIdentityRequestBody = null;
export type GetCreatorIdentitySuccessResponse = CreatorIdentityResponse;

export interface GetCreatorIdentityResponses {
  "200": CreatorIdentityResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetCreatorIdentitySuccessResponses {
  "200": CreatorIdentityResponse;
}

export interface GetCreatorIdentityErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface DiscloseCreatorIdentityParameters {
  "creator_identity_id": string;
}

export type DiscloseCreatorIdentityHeaders = Record<string, never>;

export type DiscloseCreatorIdentityRequestBody = null;
export type DiscloseCreatorIdentitySuccessResponse = CreatorDisclosureResponse;

export interface DiscloseCreatorIdentityResponses {
  "200": CreatorDisclosureResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface DiscloseCreatorIdentitySuccessResponses {
  "200": CreatorDisclosureResponse;
}

export interface DiscloseCreatorIdentityErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface WithdrawCreatorIdentityParameters {
  "creator_identity_id": string;
}

export type WithdrawCreatorIdentityHeaders = Record<string, never>;

export type WithdrawCreatorIdentityRequestBody = null;
export type WithdrawCreatorIdentitySuccessResponse = CreatorIdentityResponse;

export interface WithdrawCreatorIdentityResponses {
  "200": CreatorIdentityResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface WithdrawCreatorIdentitySuccessResponses {
  "200": CreatorIdentityResponse;
}

export interface WithdrawCreatorIdentityErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export type GetDeveloperOnboardingParameters = Record<string, never>;

export type GetDeveloperOnboardingHeaders = Record<string, never>;

export type GetDeveloperOnboardingRequestBody = null;
export type GetDeveloperOnboardingSuccessResponse = DeveloperOnboardingResponse;

export interface GetDeveloperOnboardingResponses {
  "200": DeveloperOnboardingResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetDeveloperOnboardingSuccessResponses {
  "200": DeveloperOnboardingResponse;
}

export interface GetDeveloperOnboardingErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface ListDisclosureEventsParameters {
  "cursor"?: string | null;
  "limit"?: number;
  "kind"?: DisclosureEventKind | null;
  "jurisdiction"?: string | null;
  "received_after"?: string | null;
  "received_before"?: string | null;
}

export type ListDisclosureEventsHeaders = Record<string, never>;

export type ListDisclosureEventsRequestBody = null;
export type ListDisclosureEventsSuccessResponse = DisclosureEventPage;

export interface ListDisclosureEventsResponses {
  "200": DisclosureEventPage;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface ListDisclosureEventsSuccessResponses {
  "200": DisclosureEventPage;
}

export interface ListDisclosureEventsErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export type CreateDisclosureEventParameters = Record<string, never>;

export interface CreateDisclosureEventHeaders {
  "Idempotency-Key": string;
}

export type CreateDisclosureEventRequestBody = DisclosureEventRequest;
export type CreateDisclosureEventSuccessResponse = DisclosureEventReceipt;

export interface CreateDisclosureEventResponses {
  "201": DisclosureEventReceipt;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface CreateDisclosureEventSuccessResponses {
  "201": DisclosureEventReceipt;
}

export interface CreateDisclosureEventErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface GetDisclosurePoliciesParameters {
  "version"?: string | null;
}

export type GetDisclosurePoliciesHeaders = Record<string, never>;

export type GetDisclosurePoliciesRequestBody = null;
export type GetDisclosurePoliciesSuccessResponse = DisclosurePolicyDocument;

export interface GetDisclosurePoliciesResponses {
  "200": DisclosurePolicyDocument;
  "404": ErrorResponse;
  "422": ErrorResponse;
}

export interface GetDisclosurePoliciesSuccessResponses {
  "200": DisclosurePolicyDocument;
}

export interface GetDisclosurePoliciesErrorResponses {
  "404": ErrorResponse;
  "422": ErrorResponse;
}

export type SubmitFeedbackParameters = Record<string, never>;

export type SubmitFeedbackHeaders = Record<string, never>;

export type SubmitFeedbackRequestBody = FeedbackBody;
export type SubmitFeedbackSuccessResponse = FeedbackResponse;

export interface SubmitFeedbackResponses {
  "201": FeedbackResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse;
  "404": GovernanceErrorResponse;
  "409": HttpErrorResponse | GovernanceErrorResponse;
  "422": HttpErrorResponse | GovernanceErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | GovernanceErrorResponse;
}

export interface SubmitFeedbackSuccessResponses {
  "201": FeedbackResponse;
}

export interface SubmitFeedbackErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse;
  "404": GovernanceErrorResponse;
  "409": HttpErrorResponse | GovernanceErrorResponse;
  "422": HttpErrorResponse | GovernanceErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | GovernanceErrorResponse;
}

export interface QueryGovernanceAuditParameters {
  "actor_id"?: string | null;
  "resource_type"?: string | null;
  "resource_id"?: string | null;
  "action"?: string | null;
  "request_id"?: string | null;
  "occurred_from"?: string | null;
  "occurred_to"?: string | null;
  "limit"?: number;
}

export type QueryGovernanceAuditHeaders = Record<string, never>;

export type QueryGovernanceAuditRequestBody = null;
export type QueryGovernanceAuditSuccessResponse = ReadonlyArray<AuditEventResponse>;

export interface QueryGovernanceAuditResponses {
  "200": ReadonlyArray<AuditEventResponse>;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse;
  "404": GovernanceErrorResponse;
  "409": HttpErrorResponse | GovernanceErrorResponse;
  "422": HttpErrorResponse | GovernanceErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | GovernanceErrorResponse;
}

export interface QueryGovernanceAuditSuccessResponses {
  "200": ReadonlyArray<AuditEventResponse>;
}

export interface QueryGovernanceAuditErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse;
  "404": GovernanceErrorResponse;
  "409": HttpErrorResponse | GovernanceErrorResponse;
  "422": HttpErrorResponse | GovernanceErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | GovernanceErrorResponse;
}

export interface ListGovernanceDeletionsParameters {
  "status"?: "requested" | "processing" | "completed" | "blocked_legal_hold" | "retry_wait" | "failed" | null;
  "cursor"?: string | null;
  "limit"?: number;
}

export type ListGovernanceDeletionsHeaders = Record<string, never>;

export type ListGovernanceDeletionsRequestBody = null;
export type ListGovernanceDeletionsSuccessResponse = DeletionPageResponse;

export interface ListGovernanceDeletionsResponses {
  "200": DeletionPageResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse;
  "404": GovernanceErrorResponse;
  "409": HttpErrorResponse | GovernanceErrorResponse;
  "422": HttpErrorResponse | GovernanceErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | GovernanceErrorResponse;
}

export interface ListGovernanceDeletionsSuccessResponses {
  "200": DeletionPageResponse;
}

export interface ListGovernanceDeletionsErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse;
  "404": GovernanceErrorResponse;
  "409": HttpErrorResponse | GovernanceErrorResponse;
  "422": HttpErrorResponse | GovernanceErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | GovernanceErrorResponse;
}

export type CreateGovernanceDeletionParameters = Record<string, never>;

export interface CreateGovernanceDeletionHeaders {
  "Idempotency-Key": string;
}

export type CreateGovernanceDeletionRequestBody = DeletionRequestBody;
export type CreateGovernanceDeletionSuccessResponse = DeletionResponse;

export interface CreateGovernanceDeletionResponses {
  "202": DeletionResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse;
  "404": GovernanceErrorResponse;
  "409": HttpErrorResponse | GovernanceErrorResponse;
  "422": HttpErrorResponse | GovernanceErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | GovernanceErrorResponse;
}

export interface CreateGovernanceDeletionSuccessResponses {
  "202": DeletionResponse;
}

export interface CreateGovernanceDeletionErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse;
  "404": GovernanceErrorResponse;
  "409": HttpErrorResponse | GovernanceErrorResponse;
  "422": HttpErrorResponse | GovernanceErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | GovernanceErrorResponse;
}

export interface GetGovernanceDeletionParameters {
  "deletion_id": string;
}

export type GetGovernanceDeletionHeaders = Record<string, never>;

export type GetGovernanceDeletionRequestBody = null;
export type GetGovernanceDeletionSuccessResponse = DeletionResponse;

export interface GetGovernanceDeletionResponses {
  "200": DeletionResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse;
  "404": GovernanceErrorResponse;
  "409": HttpErrorResponse | GovernanceErrorResponse;
  "422": HttpErrorResponse | GovernanceErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | GovernanceErrorResponse;
}

export interface GetGovernanceDeletionSuccessResponses {
  "200": DeletionResponse;
}

export interface GetGovernanceDeletionErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse;
  "404": GovernanceErrorResponse;
  "409": HttpErrorResponse | GovernanceErrorResponse;
  "422": HttpErrorResponse | GovernanceErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | GovernanceErrorResponse;
}

export interface ListGovernanceExportsParameters {
  "status"?: "requested" | "processing" | "ready" | "retry_wait" | "expired" | "failed" | null;
  "cursor"?: string | null;
  "limit"?: number;
}

export type ListGovernanceExportsHeaders = Record<string, never>;

export type ListGovernanceExportsRequestBody = null;
export type ListGovernanceExportsSuccessResponse = ExportPageResponse;

export interface ListGovernanceExportsResponses {
  "200": ExportPageResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse;
  "404": GovernanceErrorResponse;
  "409": HttpErrorResponse | GovernanceErrorResponse;
  "422": HttpErrorResponse | GovernanceErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | GovernanceErrorResponse;
}

export interface ListGovernanceExportsSuccessResponses {
  "200": ExportPageResponse;
}

export interface ListGovernanceExportsErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse;
  "404": GovernanceErrorResponse;
  "409": HttpErrorResponse | GovernanceErrorResponse;
  "422": HttpErrorResponse | GovernanceErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | GovernanceErrorResponse;
}

export type CreateGovernanceExportParameters = Record<string, never>;

export interface CreateGovernanceExportHeaders {
  "Idempotency-Key": string;
}

export type CreateGovernanceExportRequestBody = null;
export type CreateGovernanceExportSuccessResponse = ExportResponse;

export interface CreateGovernanceExportResponses {
  "202": ExportResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse;
  "404": GovernanceErrorResponse;
  "409": HttpErrorResponse | GovernanceErrorResponse;
  "422": HttpErrorResponse | GovernanceErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | GovernanceErrorResponse;
}

export interface CreateGovernanceExportSuccessResponses {
  "202": ExportResponse;
}

export interface CreateGovernanceExportErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse;
  "404": GovernanceErrorResponse;
  "409": HttpErrorResponse | GovernanceErrorResponse;
  "422": HttpErrorResponse | GovernanceErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | GovernanceErrorResponse;
}

export interface GetGovernanceExportParameters {
  "export_id": string;
}

export type GetGovernanceExportHeaders = Record<string, never>;

export type GetGovernanceExportRequestBody = null;
export type GetGovernanceExportSuccessResponse = ExportResponse;

export interface GetGovernanceExportResponses {
  "200": ExportResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse;
  "404": GovernanceErrorResponse;
  "409": HttpErrorResponse | GovernanceErrorResponse;
  "422": HttpErrorResponse | GovernanceErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | GovernanceErrorResponse;
}

export interface GetGovernanceExportSuccessResponses {
  "200": ExportResponse;
}

export interface GetGovernanceExportErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse;
  "404": GovernanceErrorResponse;
  "409": HttpErrorResponse | GovernanceErrorResponse;
  "422": HttpErrorResponse | GovernanceErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | GovernanceErrorResponse;
}

export type ListGovernanceLegalHoldsParameters = Record<string, never>;

export type ListGovernanceLegalHoldsHeaders = Record<string, never>;

export type ListGovernanceLegalHoldsRequestBody = null;
export type ListGovernanceLegalHoldsSuccessResponse = ReadonlyArray<LegalHoldResponse>;

export interface ListGovernanceLegalHoldsResponses {
  "200": ReadonlyArray<LegalHoldResponse>;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse;
  "404": GovernanceErrorResponse;
  "409": HttpErrorResponse | GovernanceErrorResponse;
  "422": HttpErrorResponse | GovernanceErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | GovernanceErrorResponse;
}

export interface ListGovernanceLegalHoldsSuccessResponses {
  "200": ReadonlyArray<LegalHoldResponse>;
}

export interface ListGovernanceLegalHoldsErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse;
  "404": GovernanceErrorResponse;
  "409": HttpErrorResponse | GovernanceErrorResponse;
  "422": HttpErrorResponse | GovernanceErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | GovernanceErrorResponse;
}

export interface ReleaseHistorySnapshotParameters {
  "cursor": string;
}

export type ReleaseHistorySnapshotHeaders = Record<string, never>;

export type ReleaseHistorySnapshotRequestBody = null;
export type ReleaseHistorySnapshotSuccessResponse = null;

export interface ReleaseHistorySnapshotResponses {
  "204": null;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface ReleaseHistorySnapshotSuccessResponses {
  "204": null;
}

export interface ReleaseHistorySnapshotErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export type ListIdentityCredentialsParameters = Record<string, never>;

export type ListIdentityCredentialsHeaders = Record<string, never>;

export type ListIdentityCredentialsRequestBody = null;
export type ListIdentityCredentialsSuccessResponse = IdentityCredentialListResponse;

export interface ListIdentityCredentialsResponses {
  "200": IdentityCredentialListResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface ListIdentityCredentialsSuccessResponses {
  "200": IdentityCredentialListResponse;
}

export interface ListIdentityCredentialsErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export type ListImageProfilesParameters = Record<string, never>;

export type ListImageProfilesHeaders = Record<string, never>;

export type ListImageProfilesRequestBody = null;
export type ListImageProfilesSuccessResponse = ImageProfileListResponse;

export interface ListImageProfilesResponses {
  "200": ImageProfileListResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface ListImageProfilesSuccessResponses {
  "200": ImageProfileListResponse;
}

export interface ListImageProfilesErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface ListJobsParameters {
  "kind"?: JobKind | null;
  "state"?: JobState | null;
  "cursor"?: string | null;
  "limit"?: number;
}

export type ListJobsHeaders = Record<string, never>;

export type ListJobsRequestBody = null;
export type ListJobsSuccessResponse = JobHistoryPageResponse;

export interface ListJobsResponses {
  "200": JobHistoryPageResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface ListJobsSuccessResponses {
  "200": JobHistoryPageResponse;
}

export interface ListJobsErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface GetJobParameters {
  "job_id": string;
}

export type GetJobHeaders = Record<string, never>;

export type GetJobRequestBody = null;
export type GetJobSuccessResponse = JobResponse;

export interface GetJobResponses {
  "200": JobResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface GetJobSuccessResponses {
  "200": JobResponse;
}

export interface GetJobErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface CancelJobParameters {
  "job_id": string;
}

export interface CancelJobHeaders {
  "Idempotency-Key": string;
}

export type CancelJobRequestBody = CancelJobRequest;
export type CancelJobSuccessResponse = JobResponse;

export interface CancelJobResponses {
  "200": JobResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface CancelJobSuccessResponses {
  "200": JobResponse;
}

export interface CancelJobErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export type CreateMarkingCheckParameters = Record<string, never>;

export interface CreateMarkingCheckHeaders {
  "Idempotency-Key": string;
}

export type CreateMarkingCheckRequestBody = MarkingCheckRequest;
export type CreateMarkingCheckSuccessResponse = MarkingCheckResponse;

export interface CreateMarkingCheckResponses {
  "202": MarkingCheckResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface CreateMarkingCheckSuccessResponses {
  "202": MarkingCheckResponse;
}

export interface CreateMarkingCheckErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface GetMarkingCheckParameters {
  "marking_check_id": string;
}

export type GetMarkingCheckHeaders = Record<string, never>;

export type GetMarkingCheckRequestBody = null;
export type GetMarkingCheckSuccessResponse = MarkingCheckResponse;

export interface GetMarkingCheckResponses {
  "200": MarkingCheckResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface GetMarkingCheckSuccessResponses {
  "200": MarkingCheckResponse;
}

export interface GetMarkingCheckErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export type GetCurrentUserParameters = Record<string, never>;

export type GetCurrentUserHeaders = Record<string, never>;

export type GetCurrentUserRequestBody = null;
export type GetCurrentUserSuccessResponse = MeResponse;

export interface GetCurrentUserResponses {
  "200": MeResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetCurrentUserSuccessResponses {
  "200": MeResponse;
}

export interface GetCurrentUserErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetOverviewParameters {
  "range"?: "7d" | "30d" | "12m";
}

export type GetOverviewHeaders = Record<string, never>;

export type GetOverviewRequestBody = null;
export type GetOverviewSuccessResponse = OverviewResponse;

export interface GetOverviewResponses {
  "200": OverviewResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetOverviewSuccessResponses {
  "200": OverviewResponse;
}

export interface GetOverviewErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetPublicVerifyPageParameters {
  "slug": string;
}

export type GetPublicVerifyPageHeaders = Record<string, never>;

export type GetPublicVerifyPageRequestBody = null;
export type GetPublicVerifyPageSuccessResponse = PublicVerifyPageResponse;

export interface GetPublicVerifyPageResponses {
  "200": PublicVerifyPageResponse;
  "404": ErrorResponse;
  "422": ErrorResponse;
  "503": ErrorResponse;
}

export interface GetPublicVerifyPageSuccessResponses {
  "200": PublicVerifyPageResponse;
}

export interface GetPublicVerifyPageErrorResponses {
  "404": ErrorResponse;
  "422": ErrorResponse;
  "503": ErrorResponse;
}

export interface CreatePublicCheckParameters {
  "slug": string;
}

export type CreatePublicCheckHeaders = Record<string, never>;

export type CreatePublicCheckRequestBody = null;
export type CreatePublicCheckSuccessResponse = PublicCheckResponse;

export interface CreatePublicCheckResponses {
  "200": PublicCheckResponse;
  "202": PublicCheckResponse;
  "404": ErrorResponse;
  "413": ErrorResponse;
  "415": ErrorResponse;
  "422": ErrorResponse;
  "429": ErrorResponse;
  "503": ErrorResponse;
}

export interface CreatePublicCheckSuccessResponses {
  "200": PublicCheckResponse;
  "202": PublicCheckResponse;
}

export interface CreatePublicCheckErrorResponses {
  "404": ErrorResponse;
  "413": ErrorResponse;
  "415": ErrorResponse;
  "422": ErrorResponse;
  "429": ErrorResponse;
  "503": ErrorResponse;
}

export interface GetPublicCheckParameters {
  "slug": string;
  "check_id": string;
}

export type GetPublicCheckHeaders = Record<string, never>;

export type GetPublicCheckRequestBody = null;
export type GetPublicCheckSuccessResponse = PublicCheckResponse;

export interface GetPublicCheckResponses {
  "200": PublicCheckResponse;
  "404": ErrorResponse;
  "422": ErrorResponse;
  "503": ErrorResponse;
}

export interface GetPublicCheckSuccessResponses {
  "200": PublicCheckResponse;
}

export interface GetPublicCheckErrorResponses {
  "404": ErrorResponse;
  "422": ErrorResponse;
  "503": ErrorResponse;
}

export interface GetPublicVerifyPageLogoParameters {
  "slug": string;
}

export type GetPublicVerifyPageLogoHeaders = Record<string, never>;

export type GetPublicVerifyPageLogoRequestBody = null;
export type GetPublicVerifyPageLogoSuccessResponse = null;

export interface GetPublicVerifyPageLogoResponses {
  "200": string;
  "404": ErrorResponse;
  "422": ErrorResponse;
  "503": ErrorResponse;
}

export interface GetPublicVerifyPageLogoSuccessResponses {
  "200": string;
}

export interface GetPublicVerifyPageLogoErrorResponses {
  "404": ErrorResponse;
  "422": ErrorResponse;
  "503": ErrorResponse;
}

export interface ListReceiptsParameters {
  "asset_id"?: string | null;
  "job_id"?: string | null;
  "cursor"?: string | null;
  "limit"?: number;
}

export type ListReceiptsHeaders = Record<string, never>;

export type ListReceiptsRequestBody = null;
export type ListReceiptsSuccessResponse = ReceiptHistoryPageResponse;

export interface ListReceiptsResponses {
  "200": ReceiptHistoryPageResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface ListReceiptsSuccessResponses {
  "200": ReceiptHistoryPageResponse;
}

export interface ListReceiptsErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface GetSigningReceiptParameters {
  "receipt_id": string;
}

export type GetSigningReceiptHeaders = Record<string, never>;

export type GetSigningReceiptRequestBody = null;
export type GetSigningReceiptSuccessResponse = ReceiptResponse;

export interface GetSigningReceiptResponses {
  "200": ReceiptResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface GetSigningReceiptSuccessResponses {
  "200": ReceiptResponse;
}

export interface GetSigningReceiptErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export type ListRecipesParameters = Record<string, never>;

export type ListRecipesHeaders = Record<string, never>;

export type ListRecipesRequestBody = null;
export type ListRecipesSuccessResponse = RecipeListResponse;

export interface ListRecipesResponses {
  "200": RecipeListResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface ListRecipesSuccessResponses {
  "200": RecipeListResponse;
}

export interface ListRecipesErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetRecipeParameters {
  "recipe_id": string;
}

export type GetRecipeHeaders = Record<string, never>;

export type GetRecipeRequestBody = null;
export type GetRecipeSuccessResponse = RecipeCatalogResponse;

export interface GetRecipeResponses {
  "200": RecipeCatalogResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface GetRecipeSuccessResponses {
  "200": RecipeCatalogResponse;
}

export interface GetRecipeErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface GetSharedVerificationParameters {
  "token": string;
}

export type GetSharedVerificationHeaders = Record<string, never>;

export type GetSharedVerificationRequestBody = null;
export type GetSharedVerificationSuccessResponse = SharedVerificationResponse;

export interface GetSharedVerificationResponses {
  "200": SharedVerificationResponse;
  "404": ErrorResponse;
  "422": HTTPValidationError;
}

export interface GetSharedVerificationSuccessResponses {
  "200": SharedVerificationResponse;
}

export interface GetSharedVerificationErrorResponses {
  "404": ErrorResponse;
  "422": HTTPValidationError;
}

export type AcceptSigningJobParameters = Record<string, never>;

export interface AcceptSigningJobHeaders {
  "Idempotency-Key": string;
}

export type AcceptSigningJobRequestBody = SignRequest;
export type AcceptSigningJobSuccessResponse = ExpressSignResponse;

export interface AcceptSigningJobResponses {
  "200": ExpressSignResponse;
  "202": JobResponse;
  "401": HttpErrorResponse;
  "402": ErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface AcceptSigningJobSuccessResponses {
  "200": ExpressSignResponse;
  "202": JobResponse;
}

export interface AcceptSigningJobErrorResponses {
  "401": HttpErrorResponse;
  "402": ErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export type AcceptSigningJobBatchParameters = Record<string, never>;

export interface AcceptSigningJobBatchHeaders {
  "Idempotency-Key": string;
}

export type AcceptSigningJobBatchRequestBody = SignBatchRequest;
export type AcceptSigningJobBatchSuccessResponse = SignBatchResponse;

export interface AcceptSigningJobBatchResponses {
  "202": SignBatchResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface AcceptSigningJobBatchSuccessResponses {
  "202": SignBatchResponse;
}

export interface AcceptSigningJobBatchErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export type CreateUploadParameters = Record<string, never>;

export type CreateUploadHeaders = Record<string, never>;

export type CreateUploadRequestBody = CreateUploadRequest;
export type CreateUploadSuccessResponse = CreateUploadResponse;

export interface CreateUploadResponses {
  "201": CreateUploadResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface CreateUploadSuccessResponses {
  "201": CreateUploadResponse;
}

export interface CreateUploadErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface AbortUploadParameters {
  "upload_id": string;
}

export type AbortUploadHeaders = Record<string, never>;

export type AbortUploadRequestBody = null;
export type AbortUploadSuccessResponse = AbortUploadResponse;

export interface AbortUploadResponses {
  "200": AbortUploadResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface AbortUploadSuccessResponses {
  "200": AbortUploadResponse;
}

export interface AbortUploadErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface CompleteUploadParameters {
  "upload_id": string;
}

export interface CompleteUploadHeaders {
  "Idempotency-Key": string;
}

export type CompleteUploadRequestBody = CompleteUploadRequest;
export type CompleteUploadSuccessResponse = CompleteUploadResponse;

export interface CompleteUploadResponses {
  "200": CompleteUploadResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "410": ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface CompleteUploadSuccessResponses {
  "200": CompleteUploadResponse;
}

export interface CompleteUploadErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "410": ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface GetUsageParameters {
  "period"?: string | null;
  "item_limit"?: number;
}

export type GetUsageHeaders = Record<string, never>;

export type GetUsageRequestBody = null;
export type GetUsageSuccessResponse = UsageResponse;

export interface GetUsageResponses {
  "200": UsageResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetUsageSuccessResponses {
  "200": UsageResponse;
}

export interface GetUsageErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetVerificationEvidenceParameters {
  "verification_id": string;
}

export type GetVerificationEvidenceHeaders = Record<string, never>;

export type GetVerificationEvidenceRequestBody = null;
export type GetVerificationEvidenceSuccessResponse = VerificationEvidenceResponse;

export interface GetVerificationEvidenceResponses {
  "200": VerificationEvidenceResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface GetVerificationEvidenceSuccessResponses {
  "200": VerificationEvidenceResponse;
}

export interface GetVerificationEvidenceErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface CreateVerificationReportParameters {
  "verification_id": string;
}

export type CreateVerificationReportHeaders = Record<string, never>;

export type CreateVerificationReportRequestBody = CreateReportRequest;
export type CreateVerificationReportSuccessResponse = ReportResponse;

export interface CreateVerificationReportResponses {
  "202": ReportResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface CreateVerificationReportSuccessResponses {
  "202": ReportResponse;
}

export interface CreateVerificationReportErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface ListVerificationSharesParameters {
  "verification_id": string;
  "cursor"?: string | null;
  "limit"?: number;
}

export type ListVerificationSharesHeaders = Record<string, never>;

export type ListVerificationSharesRequestBody = null;
export type ListVerificationSharesSuccessResponse = VerificationSharePageResponse;

export interface ListVerificationSharesResponses {
  "200": VerificationSharePageResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface ListVerificationSharesSuccessResponses {
  "200": VerificationSharePageResponse;
}

export interface ListVerificationSharesErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface CreateVerificationShareParameters {
  "verification_id": string;
}

export interface CreateVerificationShareHeaders {
  "Idempotency-Key": string;
}

export type CreateVerificationShareRequestBody = CreateShareRequest;
export type CreateVerificationShareSuccessResponse = CreateShareResponse;

export interface CreateVerificationShareResponses {
  "201": CreateShareResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface CreateVerificationShareSuccessResponses {
  "201": CreateShareResponse;
}

export interface CreateVerificationShareErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface GetVerificationHistoryParameters {
  "verification_id": string;
}

export type GetVerificationHistoryHeaders = Record<string, never>;

export type GetVerificationHistoryRequestBody = null;
export type GetVerificationHistorySuccessResponse = VerificationHistoryResponse;

export interface GetVerificationHistoryResponses {
  "200": VerificationHistoryResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface GetVerificationHistorySuccessResponses {
  "200": VerificationHistoryResponse;
}

export interface GetVerificationHistoryErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface GetVerificationReportParameters {
  "report_id": string;
}

export type GetVerificationReportHeaders = Record<string, never>;

export type GetVerificationReportRequestBody = null;
export type GetVerificationReportSuccessResponse = ReportContentResponse;

export interface GetVerificationReportResponses {
  "200": ReportContentResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface GetVerificationReportSuccessResponses {
  "200": ReportContentResponse;
}

export interface GetVerificationReportErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface CloseVerificationShareParameters {
  "share_id": string;
}

export type CloseVerificationShareHeaders = Record<string, never>;

export type CloseVerificationShareRequestBody = CloseShareRequest;
export type CloseVerificationShareSuccessResponse = CloseShareResponse;

export interface CloseVerificationShareResponses {
  "200": CloseShareResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface CloseVerificationShareSuccessResponses {
  "200": CloseShareResponse;
}

export interface CloseVerificationShareErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface ListVerificationsParameters {
  "overall"?: VerificationOverall | null;
  "subject_type"?: VerificationSubjectType | null;
  "cursor"?: string | null;
  "limit"?: number;
}

export type ListVerificationsHeaders = Record<string, never>;

export type ListVerificationsRequestBody = null;
export type ListVerificationsSuccessResponse = VerificationHistoryPageResponse;

export interface ListVerificationsResponses {
  "200": VerificationHistoryPageResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface ListVerificationsSuccessResponses {
  "200": VerificationHistoryPageResponse;
}

export interface ListVerificationsErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export type CreateVerificationParameters = Record<string, never>;

export interface CreateVerificationHeaders {
  "Idempotency-Key": string;
}

export type CreateVerificationRequestBody = CreateVerificationRequest;
export type CreateVerificationSuccessResponse = VerificationResponse;

export interface CreateVerificationResponses {
  "202": VerificationResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface CreateVerificationSuccessResponses {
  "202": VerificationResponse;
}

export interface CreateVerificationErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface GetVerificationParameters {
  "verification_id": string;
}

export type GetVerificationHeaders = Record<string, never>;

export type GetVerificationRequestBody = null;
export type GetVerificationSuccessResponse = VerificationResponse;

export interface GetVerificationResponses {
  "200": VerificationResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface GetVerificationSuccessResponses {
  "200": VerificationResponse;
}

export interface GetVerificationErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export type CreateVerificationBatchParameters = Record<string, never>;

export interface CreateVerificationBatchHeaders {
  "Idempotency-Key": string;
}

export type CreateVerificationBatchRequestBody = VerificationBatchRequest;
export type CreateVerificationBatchSuccessResponse = VerificationBatchResponse;

export interface CreateVerificationBatchResponses {
  "202": VerificationBatchResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface CreateVerificationBatchSuccessResponses {
  "202": VerificationBatchResponse;
}

export interface CreateVerificationBatchErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export type GetVerifyPageParameters = Record<string, never>;

export type GetVerifyPageHeaders = Record<string, never>;

export type GetVerifyPageRequestBody = null;
export type GetVerifyPageSuccessResponse = VerifyPageResponse;

export interface GetVerifyPageResponses {
  "200": VerifyPageResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface GetVerifyPageSuccessResponses {
  "200": VerifyPageResponse;
}

export interface GetVerifyPageErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export type PutVerifyPageParameters = Record<string, never>;

export type PutVerifyPageHeaders = Record<string, never>;

export type PutVerifyPageRequestBody = VerifyPageUpdateRequest;
export type PutVerifyPageSuccessResponse = VerifyPageResponse;

export interface PutVerifyPageResponses {
  "200": VerifyPageResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface PutVerifyPageSuccessResponses {
  "200": VerifyPageResponse;
}

export interface PutVerifyPageErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface ListWebhookEndpointsParameters {
  "limit"?: number;
  "cursor"?: string | null;
  "include_deleted"?: boolean;
}

export type ListWebhookEndpointsHeaders = Record<string, never>;

export type ListWebhookEndpointsRequestBody = null;
export type ListWebhookEndpointsSuccessResponse = WebhookEndpointPageResponse;

export interface ListWebhookEndpointsResponses {
  "200": WebhookEndpointPageResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface ListWebhookEndpointsSuccessResponses {
  "200": WebhookEndpointPageResponse;
}

export interface ListWebhookEndpointsErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export type CreateWebhookEndpointParameters = Record<string, never>;

export interface CreateWebhookEndpointHeaders {
  "Idempotency-Key": string;
}

export type CreateWebhookEndpointRequestBody = CreateWebhookEndpointRequest;
export type CreateWebhookEndpointSuccessResponse = IssuedWebhookEndpointResponse;

export interface CreateWebhookEndpointResponses {
  "201": IssuedWebhookEndpointResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse | SecretNotReplayableResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface CreateWebhookEndpointSuccessResponses {
  "201": IssuedWebhookEndpointResponse;
}

export interface CreateWebhookEndpointErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse | SecretNotReplayableResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface DeleteWebhookEndpointParameters {
  "endpoint_id": string;
}

export type DeleteWebhookEndpointHeaders = Record<string, never>;

export type DeleteWebhookEndpointRequestBody = null;
export type DeleteWebhookEndpointSuccessResponse = null;

export interface DeleteWebhookEndpointResponses {
  "204": null;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface DeleteWebhookEndpointSuccessResponses {
  "204": null;
}

export interface DeleteWebhookEndpointErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetWebhookEndpointParameters {
  "endpoint_id": string;
}

export type GetWebhookEndpointHeaders = Record<string, never>;

export type GetWebhookEndpointRequestBody = null;
export type GetWebhookEndpointSuccessResponse = WebhookEndpointResponse;

export interface GetWebhookEndpointResponses {
  "200": WebhookEndpointResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetWebhookEndpointSuccessResponses {
  "200": WebhookEndpointResponse;
}

export interface GetWebhookEndpointErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface UpdateWebhookEndpointParameters {
  "endpoint_id": string;
}

export type UpdateWebhookEndpointHeaders = Record<string, never>;

export type UpdateWebhookEndpointRequestBody = UpdateWebhookEndpointRequest;
export type UpdateWebhookEndpointSuccessResponse = WebhookEndpointResponse;

export interface UpdateWebhookEndpointResponses {
  "200": WebhookEndpointResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface UpdateWebhookEndpointSuccessResponses {
  "200": WebhookEndpointResponse;
}

export interface UpdateWebhookEndpointErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface ListWebhookDeliveriesParameters {
  "endpoint_id": string;
  "limit"?: number;
  "cursor"?: string | null;
}

export type ListWebhookDeliveriesHeaders = Record<string, never>;

export type ListWebhookDeliveriesRequestBody = null;
export type ListWebhookDeliveriesSuccessResponse = WebhookDeliveryPageResponse;

export interface ListWebhookDeliveriesResponses {
  "200": WebhookDeliveryPageResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface ListWebhookDeliveriesSuccessResponses {
  "200": WebhookDeliveryPageResponse;
}

export interface ListWebhookDeliveriesErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface DisableWebhookEndpointParameters {
  "endpoint_id": string;
}

export type DisableWebhookEndpointHeaders = Record<string, never>;

export type DisableWebhookEndpointRequestBody = null;
export type DisableWebhookEndpointSuccessResponse = null;

export interface DisableWebhookEndpointResponses {
  "204": null;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface DisableWebhookEndpointSuccessResponses {
  "204": null;
}

export interface DisableWebhookEndpointErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface EnableWebhookEndpointParameters {
  "endpoint_id": string;
}

export type EnableWebhookEndpointHeaders = Record<string, never>;

export type EnableWebhookEndpointRequestBody = null;
export type EnableWebhookEndpointSuccessResponse = WebhookEndpointResponse;

export interface EnableWebhookEndpointResponses {
  "200": WebhookEndpointResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface EnableWebhookEndpointSuccessResponses {
  "200": WebhookEndpointResponse;
}

export interface EnableWebhookEndpointErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface RotateWebhookEndpointSecretParameters {
  "endpoint_id": string;
}

export interface RotateWebhookEndpointSecretHeaders {
  "Idempotency-Key": string;
}

export type RotateWebhookEndpointSecretRequestBody = RotateWebhookSecretRequest | null;
export type RotateWebhookEndpointSecretSuccessResponse = RotatedWebhookSecretResponse;

export interface RotateWebhookEndpointSecretResponses {
  "200": RotatedWebhookSecretResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse | SecretNotReplayableResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface RotateWebhookEndpointSecretSuccessResponses {
  "200": RotatedWebhookSecretResponse;
}

export interface RotateWebhookEndpointSecretErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse | SecretNotReplayableResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface CompleteWebhookEndpointSecretOverlapParameters {
  "endpoint_id": string;
}

export type CompleteWebhookEndpointSecretOverlapHeaders = Record<string, never>;

export type CompleteWebhookEndpointSecretOverlapRequestBody = null;
export type CompleteWebhookEndpointSecretOverlapSuccessResponse = WebhookEndpointResponse;

export interface CompleteWebhookEndpointSecretOverlapResponses {
  "200": WebhookEndpointResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface CompleteWebhookEndpointSecretOverlapSuccessResponses {
  "200": WebhookEndpointResponse;
}

export interface CompleteWebhookEndpointSecretOverlapErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface SendWebhookTestEventParameters {
  "endpoint_id": string;
}

export type SendWebhookTestEventHeaders = Record<string, never>;

export type SendWebhookTestEventRequestBody = null;
export type SendWebhookTestEventSuccessResponse = WebhookTestEventResponse;

export interface SendWebhookTestEventResponses {
  "202": WebhookTestEventResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface SendWebhookTestEventSuccessResponses {
  "202": WebhookTestEventResponse;
}

export interface SendWebhookTestEventErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetWebhookDeliveryParameters {
  "delivery_id": string;
}

export type GetWebhookDeliveryHeaders = Record<string, never>;

export type GetWebhookDeliveryRequestBody = null;
export type GetWebhookDeliverySuccessResponse = WebhookDeliveryResponse;

export interface GetWebhookDeliveryResponses {
  "200": WebhookDeliveryResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetWebhookDeliverySuccessResponses {
  "200": WebhookDeliveryResponse;
}

export interface GetWebhookDeliveryErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface ListWebhookDeliveryAttemptsParameters {
  "delivery_id": string;
  "limit"?: number;
  "cursor"?: string | null;
}

export type ListWebhookDeliveryAttemptsHeaders = Record<string, never>;

export type ListWebhookDeliveryAttemptsRequestBody = null;
export type ListWebhookDeliveryAttemptsSuccessResponse = WebhookAttemptPageResponse;

export interface ListWebhookDeliveryAttemptsResponses {
  "200": WebhookAttemptPageResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface ListWebhookDeliveryAttemptsSuccessResponses {
  "200": WebhookAttemptPageResponse;
}

export interface ListWebhookDeliveryAttemptsErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface ReplayWebhookDeliveryParameters {
  "delivery_id": string;
}

export interface ReplayWebhookDeliveryHeaders {
  "Idempotency-Key": string;
}

export type ReplayWebhookDeliveryRequestBody = null;
export type ReplayWebhookDeliverySuccessResponse = ReplayWebhookDeliveryResponse;

export interface ReplayWebhookDeliveryResponses {
  "200": ReplayWebhookDeliveryResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface ReplayWebhookDeliverySuccessResponses {
  "200": ReplayWebhookDeliveryResponse;
}

export interface ReplayWebhookDeliveryErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": HttpErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export type GetWebhookEventCatalogParameters = Record<string, never>;

export type GetWebhookEventCatalogHeaders = Record<string, never>;

export type GetWebhookEventCatalogRequestBody = null;
export type GetWebhookEventCatalogSuccessResponse = CustomerEventCatalogResponse;

export interface GetWebhookEventCatalogResponses {
  "200": CustomerEventCatalogResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface GetWebhookEventCatalogSuccessResponses {
  "200": CustomerEventCatalogResponse;
}

export interface GetWebhookEventCatalogErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse;
}

export interface ReplayWebhookEventParameters {
  "event_id": string;
}

export interface ReplayWebhookEventHeaders {
  "Idempotency-Key": string;
}

export type ReplayWebhookEventRequestBody = null;
export type ReplayWebhookEventSuccessResponse = WebhookReplayResponse;

export interface ReplayWebhookEventResponses {
  "200": WebhookReplayResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface ReplayWebhookEventSuccessResponses {
  "200": WebhookReplayResponse;
}

export interface ReplayWebhookEventErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export type ListWorkflowTemplatesParameters = Record<string, never>;

export type ListWorkflowTemplatesHeaders = Record<string, never>;

export type ListWorkflowTemplatesRequestBody = null;
export type ListWorkflowTemplatesSuccessResponse = WorkflowTemplateListResponse;

export interface ListWorkflowTemplatesResponses {
  "200": WorkflowTemplateListResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface ListWorkflowTemplatesSuccessResponses {
  "200": WorkflowTemplateListResponse;
}

export interface ListWorkflowTemplatesErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "409": HttpErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export type CreateWorkflowTemplateParameters = Record<string, never>;

export interface CreateWorkflowTemplateHeaders {
  "Idempotency-Key": string;
}

export type CreateWorkflowTemplateRequestBody = WorkflowTemplateRequest;
export type CreateWorkflowTemplateSuccessResponse = WorkflowTemplateResponse;

export interface CreateWorkflowTemplateResponses {
  "201": WorkflowTemplateResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface CreateWorkflowTemplateSuccessResponses {
  "201": WorkflowTemplateResponse;
}

export interface CreateWorkflowTemplateErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface DeleteWorkflowTemplateParameters {
  "template_id": string;
}

export type DeleteWorkflowTemplateHeaders = Record<string, never>;

export type DeleteWorkflowTemplateRequestBody = null;
export type DeleteWorkflowTemplateSuccessResponse = null;

export interface DeleteWorkflowTemplateResponses {
  "204": null;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface DeleteWorkflowTemplateSuccessResponses {
  "204": null;
}

export interface DeleteWorkflowTemplateErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface GetWorkflowTemplateParameters {
  "template_id": string;
}

export type GetWorkflowTemplateHeaders = Record<string, never>;

export type GetWorkflowTemplateRequestBody = null;
export type GetWorkflowTemplateSuccessResponse = WorkflowTemplateResponse;

export interface GetWorkflowTemplateResponses {
  "200": WorkflowTemplateResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface GetWorkflowTemplateSuccessResponses {
  "200": WorkflowTemplateResponse;
}

export interface GetWorkflowTemplateErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface ReplaceWorkflowTemplateParameters {
  "template_id": string;
}

export type ReplaceWorkflowTemplateHeaders = Record<string, never>;

export type ReplaceWorkflowTemplateRequestBody = WorkflowTemplateReplaceRequest;
export type ReplaceWorkflowTemplateSuccessResponse = WorkflowTemplateResponse;

export interface ReplaceWorkflowTemplateResponses {
  "200": WorkflowTemplateResponse;
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export interface ReplaceWorkflowTemplateSuccessResponses {
  "200": WorkflowTemplateResponse;
}

export interface ReplaceWorkflowTemplateErrorResponses {
  "401": HttpErrorResponse;
  "403": HttpErrorResponse | ErrorResponse;
  "404": ErrorResponse;
  "409": HttpErrorResponse | ErrorResponse;
  "422": HttpErrorResponse | ErrorResponse;
  "429": ErrorResponse;
  "503": HttpErrorResponse | ErrorResponse;
}

export type ReceiveClerkWebhookParameters = Record<string, never>;

export interface ReceiveClerkWebhookHeaders {
  "svix-id": string;
  "svix-timestamp": string;
}

export type ReceiveClerkWebhookRequestBody = Record<string, unknown>;
export type ReceiveClerkWebhookSuccessResponse = WebhookAck;

export interface ReceiveClerkWebhookResponses {
  "200": WebhookAck;
  "400": HttpErrorResponse;
  "409": HttpErrorResponse;
  "413": HttpErrorResponse;
  "422": HTTPValidationError;
  "503": HttpErrorResponse;
}

export interface ReceiveClerkWebhookSuccessResponses {
  "200": WebhookAck;
}

export interface ReceiveClerkWebhookErrorResponses {
  "400": HttpErrorResponse;
  "409": HttpErrorResponse;
  "413": HttpErrorResponse;
  "422": HTTPValidationError;
  "503": HttpErrorResponse;
}

export type ReceiveStripeWebhookParameters = Record<string, never>;

export type ReceiveStripeWebhookHeaders = Record<string, never>;

export type ReceiveStripeWebhookRequestBody = Record<string, unknown>;
export type ReceiveStripeWebhookSuccessResponse = StripeInboxResponse;

export interface ReceiveStripeWebhookResponses {
  "202": StripeInboxResponse;
  "400": HttpErrorResponse;
  "409": HttpErrorResponse;
  "413": HttpErrorResponse;
  "503": HttpErrorResponse;
}

export interface ReceiveStripeWebhookSuccessResponses {
  "202": StripeInboxResponse;
}

export interface ReceiveStripeWebhookErrorResponses {
  "400": HttpErrorResponse;
  "409": HttpErrorResponse;
  "413": HttpErrorResponse;
  "503": HttpErrorResponse;
}

export interface PublicApiOperationModels {
  "getHealthz": {
    request: GetHealthzRequestBody;
    response: GetHealthzSuccessResponse;
    responses: GetHealthzResponses;
    successes: GetHealthzSuccessResponses;
    errors: GetHealthzErrorResponses;
    parameters: GetHealthzParameters;
    headers: GetHealthzHeaders;
  };
  "getDatabaseHealth": {
    request: GetDatabaseHealthRequestBody;
    response: GetDatabaseHealthSuccessResponse;
    responses: GetDatabaseHealthResponses;
    successes: GetDatabaseHealthSuccessResponses;
    errors: GetDatabaseHealthErrorResponses;
    parameters: GetDatabaseHealthParameters;
    headers: GetDatabaseHealthHeaders;
  };
  "getReadyz": {
    request: GetReadyzRequestBody;
    response: GetReadyzSuccessResponse;
    responses: GetReadyzResponses;
    successes: GetReadyzSuccessResponses;
    errors: GetReadyzErrorResponses;
    parameters: GetReadyzParameters;
    headers: GetReadyzHeaders;
  };
  "getGovernanceReadyz": {
    request: GetGovernanceReadyzRequestBody;
    response: GetGovernanceReadyzSuccessResponse;
    responses: GetGovernanceReadyzResponses;
    successes: GetGovernanceReadyzSuccessResponses;
    errors: GetGovernanceReadyzErrorResponses;
    parameters: GetGovernanceReadyzParameters;
    headers: GetGovernanceReadyzHeaders;
  };
  "listApiKeys": {
    request: ListApiKeysRequestBody;
    response: ListApiKeysSuccessResponse;
    responses: ListApiKeysResponses;
    successes: ListApiKeysSuccessResponses;
    errors: ListApiKeysErrorResponses;
    parameters: ListApiKeysParameters;
    headers: ListApiKeysHeaders;
  };
  "createApiKey": {
    request: CreateApiKeyRequestBody;
    response: CreateApiKeySuccessResponse;
    responses: CreateApiKeyResponses;
    successes: CreateApiKeySuccessResponses;
    errors: CreateApiKeyErrorResponses;
    parameters: CreateApiKeyParameters;
    headers: CreateApiKeyHeaders;
  };
  "revokeApiKey": {
    request: RevokeApiKeyRequestBody;
    response: RevokeApiKeySuccessResponse;
    responses: RevokeApiKeyResponses;
    successes: RevokeApiKeySuccessResponses;
    errors: RevokeApiKeyErrorResponses;
    parameters: RevokeApiKeyParameters;
    headers: RevokeApiKeyHeaders;
  };
  "getApiKey": {
    request: GetApiKeyRequestBody;
    response: GetApiKeySuccessResponse;
    responses: GetApiKeyResponses;
    successes: GetApiKeySuccessResponses;
    errors: GetApiKeyErrorResponses;
    parameters: GetApiKeyParameters;
    headers: GetApiKeyHeaders;
  };
  "getApiKeyRestrictions": {
    request: GetApiKeyRestrictionsRequestBody;
    response: GetApiKeyRestrictionsSuccessResponse;
    responses: GetApiKeyRestrictionsResponses;
    successes: GetApiKeyRestrictionsSuccessResponses;
    errors: GetApiKeyRestrictionsErrorResponses;
    parameters: GetApiKeyRestrictionsParameters;
    headers: GetApiKeyRestrictionsHeaders;
  };
  "setApiKeyRestrictions": {
    request: SetApiKeyRestrictionsRequestBody;
    response: SetApiKeyRestrictionsSuccessResponse;
    responses: SetApiKeyRestrictionsResponses;
    successes: SetApiKeyRestrictionsSuccessResponses;
    errors: SetApiKeyRestrictionsErrorResponses;
    parameters: SetApiKeyRestrictionsParameters;
    headers: SetApiKeyRestrictionsHeaders;
  };
  "getApiKeyRetention": {
    request: GetApiKeyRetentionRequestBody;
    response: GetApiKeyRetentionSuccessResponse;
    responses: GetApiKeyRetentionResponses;
    successes: GetApiKeyRetentionSuccessResponses;
    errors: GetApiKeyRetentionErrorResponses;
    parameters: GetApiKeyRetentionParameters;
    headers: GetApiKeyRetentionHeaders;
  };
  "setApiKeyRetention": {
    request: SetApiKeyRetentionRequestBody;
    response: SetApiKeyRetentionSuccessResponse;
    responses: SetApiKeyRetentionResponses;
    successes: SetApiKeyRetentionSuccessResponses;
    errors: SetApiKeyRetentionErrorResponses;
    parameters: SetApiKeyRetentionParameters;
    headers: SetApiKeyRetentionHeaders;
  };
  "rotateApiKey": {
    request: RotateApiKeyRequestBody;
    response: RotateApiKeySuccessResponse;
    responses: RotateApiKeyResponses;
    successes: RotateApiKeySuccessResponses;
    errors: RotateApiKeyErrorResponses;
    parameters: RotateApiKeyParameters;
    headers: RotateApiKeyHeaders;
  };
  "cancelApiKeyRotation": {
    request: CancelApiKeyRotationRequestBody;
    response: CancelApiKeyRotationSuccessResponse;
    responses: CancelApiKeyRotationResponses;
    successes: CancelApiKeyRotationSuccessResponses;
    errors: CancelApiKeyRotationErrorResponses;
    parameters: CancelApiKeyRotationParameters;
    headers: CancelApiKeyRotationHeaders;
  };
  "completeApiKeyRotation": {
    request: CompleteApiKeyRotationRequestBody;
    response: CompleteApiKeyRotationSuccessResponse;
    responses: CompleteApiKeyRotationResponses;
    successes: CompleteApiKeyRotationSuccessResponses;
    errors: CompleteApiKeyRotationErrorResponses;
    parameters: CompleteApiKeyRotationParameters;
    headers: CompleteApiKeyRotationHeaders;
  };
  "getApiKeySigningProfile": {
    request: GetApiKeySigningProfileRequestBody;
    response: GetApiKeySigningProfileSuccessResponse;
    responses: GetApiKeySigningProfileResponses;
    successes: GetApiKeySigningProfileSuccessResponses;
    errors: GetApiKeySigningProfileErrorResponses;
    parameters: GetApiKeySigningProfileParameters;
    headers: GetApiKeySigningProfileHeaders;
  };
  "setApiKeySigningProfile": {
    request: SetApiKeySigningProfileRequestBody;
    response: SetApiKeySigningProfileSuccessResponse;
    responses: SetApiKeySigningProfileResponses;
    successes: SetApiKeySigningProfileSuccessResponses;
    errors: SetApiKeySigningProfileErrorResponses;
    parameters: SetApiKeySigningProfileParameters;
    headers: SetApiKeySigningProfileHeaders;
  };
  "listApiKeyScopes": {
    request: ListApiKeyScopesRequestBody;
    response: ListApiKeyScopesSuccessResponse;
    responses: ListApiKeyScopesResponses;
    successes: ListApiKeyScopesSuccessResponses;
    errors: ListApiKeyScopesErrorResponses;
    parameters: ListApiKeyScopesParameters;
    headers: ListApiKeyScopesHeaders;
  };
  "listApiRequestLogs": {
    request: ListApiRequestLogsRequestBody;
    response: ListApiRequestLogsSuccessResponse;
    responses: ListApiRequestLogsResponses;
    successes: ListApiRequestLogsSuccessResponses;
    errors: ListApiRequestLogsErrorResponses;
    parameters: ListApiRequestLogsParameters;
    headers: ListApiRequestLogsHeaders;
  };
  "summarizeApiRequestLogs": {
    request: SummarizeApiRequestLogsRequestBody;
    response: SummarizeApiRequestLogsSuccessResponse;
    responses: SummarizeApiRequestLogsResponses;
    successes: SummarizeApiRequestLogsSuccessResponses;
    errors: SummarizeApiRequestLogsErrorResponses;
    parameters: SummarizeApiRequestLogsParameters;
    headers: SummarizeApiRequestLogsHeaders;
  };
  "listAssets": {
    request: ListAssetsRequestBody;
    response: ListAssetsSuccessResponse;
    responses: ListAssetsResponses;
    successes: ListAssetsSuccessResponses;
    errors: ListAssetsErrorResponses;
    parameters: ListAssetsParameters;
    headers: ListAssetsHeaders;
  };
  "getAsset": {
    request: GetAssetRequestBody;
    response: GetAssetSuccessResponse;
    responses: GetAssetResponses;
    successes: GetAssetSuccessResponses;
    errors: GetAssetErrorResponses;
    parameters: GetAssetParameters;
    headers: GetAssetHeaders;
  };
  "getAssetDetail": {
    request: GetAssetDetailRequestBody;
    response: GetAssetDetailSuccessResponse;
    responses: GetAssetDetailResponses;
    successes: GetAssetDetailSuccessResponses;
    errors: GetAssetDetailErrorResponses;
    parameters: GetAssetDetailParameters;
    headers: GetAssetDetailHeaders;
  };
  "createAssetDownload": {
    request: CreateAssetDownloadRequestBody;
    response: CreateAssetDownloadSuccessResponse;
    responses: CreateAssetDownloadResponses;
    successes: CreateAssetDownloadSuccessResponses;
    errors: CreateAssetDownloadErrorResponses;
    parameters: CreateAssetDownloadParameters;
    headers: CreateAssetDownloadHeaders;
  };
  "createAssetPreview": {
    request: CreateAssetPreviewRequestBody;
    response: CreateAssetPreviewSuccessResponse;
    responses: CreateAssetPreviewResponses;
    successes: CreateAssetPreviewSuccessResponses;
    errors: CreateAssetPreviewErrorResponses;
    parameters: CreateAssetPreviewParameters;
    headers: CreateAssetPreviewHeaders;
  };
  "redeemAssetPreview": {
    request: RedeemAssetPreviewRequestBody;
    response: RedeemAssetPreviewSuccessResponse;
    responses: RedeemAssetPreviewResponses;
    successes: RedeemAssetPreviewSuccessResponses;
    errors: RedeemAssetPreviewErrorResponses;
    parameters: RedeemAssetPreviewParameters;
    headers: RedeemAssetPreviewHeaders;
  };
  "getBillingAccount": {
    request: GetBillingAccountRequestBody;
    response: GetBillingAccountSuccessResponse;
    responses: GetBillingAccountResponses;
    successes: GetBillingAccountSuccessResponses;
    errors: GetBillingAccountErrorResponses;
    parameters: GetBillingAccountParameters;
    headers: GetBillingAccountHeaders;
  };
  "listBillingCharges": {
    request: ListBillingChargesRequestBody;
    response: ListBillingChargesSuccessResponse;
    responses: ListBillingChargesResponses;
    successes: ListBillingChargesSuccessResponses;
    errors: ListBillingChargesErrorResponses;
    parameters: ListBillingChargesParameters;
    headers: ListBillingChargesHeaders;
  };
  "createBillingCheckoutIntent": {
    request: CreateBillingCheckoutIntentRequestBody;
    response: CreateBillingCheckoutIntentSuccessResponse;
    responses: CreateBillingCheckoutIntentResponses;
    successes: CreateBillingCheckoutIntentSuccessResponses;
    errors: CreateBillingCheckoutIntentErrorResponses;
    parameters: CreateBillingCheckoutIntentParameters;
    headers: CreateBillingCheckoutIntentHeaders;
  };
  "listBillingInvoices": {
    request: ListBillingInvoicesRequestBody;
    response: ListBillingInvoicesSuccessResponse;
    responses: ListBillingInvoicesResponses;
    successes: ListBillingInvoicesSuccessResponses;
    errors: ListBillingInvoicesErrorResponses;
    parameters: ListBillingInvoicesParameters;
    headers: ListBillingInvoicesHeaders;
  };
  "getBillingPlans": {
    request: GetBillingPlansRequestBody;
    response: GetBillingPlansSuccessResponse;
    responses: GetBillingPlansResponses;
    successes: GetBillingPlansSuccessResponses;
    errors: GetBillingPlansErrorResponses;
    parameters: GetBillingPlansParameters;
    headers: GetBillingPlansHeaders;
  };
  "createBillingPortalIntent": {
    request: CreateBillingPortalIntentRequestBody;
    response: CreateBillingPortalIntentSuccessResponse;
    responses: CreateBillingPortalIntentResponses;
    successes: CreateBillingPortalIntentSuccessResponses;
    errors: CreateBillingPortalIntentErrorResponses;
    parameters: CreateBillingPortalIntentParameters;
    headers: CreateBillingPortalIntentHeaders;
  };
  "getBillingPricing": {
    request: GetBillingPricingRequestBody;
    response: GetBillingPricingSuccessResponse;
    responses: GetBillingPricingResponses;
    successes: GetBillingPricingSuccessResponses;
    errors: GetBillingPricingErrorResponses;
    parameters: GetBillingPricingParameters;
    headers: GetBillingPricingHeaders;
  };
  "createBillingQuote": {
    request: CreateBillingQuoteRequestBody;
    response: CreateBillingQuoteSuccessResponse;
    responses: CreateBillingQuoteResponses;
    successes: CreateBillingQuoteSuccessResponses;
    errors: CreateBillingQuoteErrorResponses;
    parameters: CreateBillingQuoteParameters;
    headers: CreateBillingQuoteHeaders;
  };
  "getBillingWallet": {
    request: GetBillingWalletRequestBody;
    response: GetBillingWalletSuccessResponse;
    responses: GetBillingWalletResponses;
    successes: GetBillingWalletSuccessResponses;
    errors: GetBillingWalletErrorResponses;
    parameters: GetBillingWalletParameters;
    headers: GetBillingWalletHeaders;
  };
  "setBillingWalletSettings": {
    request: SetBillingWalletSettingsRequestBody;
    response: SetBillingWalletSettingsSuccessResponse;
    responses: SetBillingWalletSettingsResponses;
    successes: SetBillingWalletSettingsSuccessResponses;
    errors: SetBillingWalletSettingsErrorResponses;
    parameters: SetBillingWalletSettingsParameters;
    headers: SetBillingWalletSettingsHeaders;
  };
  "getCapabilities": {
    request: GetCapabilitiesRequestBody;
    response: GetCapabilitiesSuccessResponse;
    responses: GetCapabilitiesResponses;
    successes: GetCapabilitiesSuccessResponses;
    errors: GetCapabilitiesErrorResponses;
    parameters: GetCapabilitiesParameters;
    headers: GetCapabilitiesHeaders;
  };
  "createCaptureAdmissionChallenge": {
    request: CreateCaptureAdmissionChallengeRequestBody;
    response: CreateCaptureAdmissionChallengeSuccessResponse;
    responses: CreateCaptureAdmissionChallengeResponses;
    successes: CreateCaptureAdmissionChallengeSuccessResponses;
    errors: CreateCaptureAdmissionChallengeErrorResponses;
    parameters: CreateCaptureAdmissionChallengeParameters;
    headers: CreateCaptureAdmissionChallengeHeaders;
  };
  "listCaptureAdmissions": {
    request: ListCaptureAdmissionsRequestBody;
    response: ListCaptureAdmissionsSuccessResponse;
    responses: ListCaptureAdmissionsResponses;
    successes: ListCaptureAdmissionsSuccessResponses;
    errors: ListCaptureAdmissionsErrorResponses;
    parameters: ListCaptureAdmissionsParameters;
    headers: ListCaptureAdmissionsHeaders;
  };
  "createCaptureAdmission": {
    request: CreateCaptureAdmissionRequestBody;
    response: CreateCaptureAdmissionSuccessResponse;
    responses: CreateCaptureAdmissionResponses;
    successes: CreateCaptureAdmissionSuccessResponses;
    errors: CreateCaptureAdmissionErrorResponses;
    parameters: CreateCaptureAdmissionParameters;
    headers: CreateCaptureAdmissionHeaders;
  };
  "getCaptureAdmission": {
    request: GetCaptureAdmissionRequestBody;
    response: GetCaptureAdmissionSuccessResponse;
    responses: GetCaptureAdmissionResponses;
    successes: GetCaptureAdmissionSuccessResponses;
    errors: GetCaptureAdmissionErrorResponses;
    parameters: GetCaptureAdmissionParameters;
    headers: GetCaptureAdmissionHeaders;
  };
  "listCaptureIdentities": {
    request: ListCaptureIdentitiesRequestBody;
    response: ListCaptureIdentitiesSuccessResponse;
    responses: ListCaptureIdentitiesResponses;
    successes: ListCaptureIdentitiesSuccessResponses;
    errors: ListCaptureIdentitiesErrorResponses;
    parameters: ListCaptureIdentitiesParameters;
    headers: ListCaptureIdentitiesHeaders;
  };
  "createCaptureIdentity": {
    request: CreateCaptureIdentityRequestBody;
    response: CreateCaptureIdentitySuccessResponse;
    responses: CreateCaptureIdentityResponses;
    successes: CreateCaptureIdentitySuccessResponses;
    errors: CreateCaptureIdentityErrorResponses;
    parameters: CreateCaptureIdentityParameters;
    headers: CreateCaptureIdentityHeaders;
  };
  "getCaptureIdentity": {
    request: GetCaptureIdentityRequestBody;
    response: GetCaptureIdentitySuccessResponse;
    responses: GetCaptureIdentityResponses;
    successes: GetCaptureIdentitySuccessResponses;
    errors: GetCaptureIdentityErrorResponses;
    parameters: GetCaptureIdentityParameters;
    headers: GetCaptureIdentityHeaders;
  };
  "revokeCaptureIdentity": {
    request: RevokeCaptureIdentityRequestBody;
    response: RevokeCaptureIdentitySuccessResponse;
    responses: RevokeCaptureIdentityResponses;
    successes: RevokeCaptureIdentitySuccessResponses;
    errors: RevokeCaptureIdentityErrorResponses;
    parameters: RevokeCaptureIdentityParameters;
    headers: RevokeCaptureIdentityHeaders;
  };
  "createCaptureIdentityEnrollment": {
    request: CreateCaptureIdentityEnrollmentRequestBody;
    response: CreateCaptureIdentityEnrollmentSuccessResponse;
    responses: CreateCaptureIdentityEnrollmentResponses;
    successes: CreateCaptureIdentityEnrollmentSuccessResponses;
    errors: CreateCaptureIdentityEnrollmentErrorResponses;
    parameters: CreateCaptureIdentityEnrollmentParameters;
    headers: CreateCaptureIdentityEnrollmentHeaders;
  };
  "getConnectCatalog": {
    request: GetConnectCatalogRequestBody;
    response: GetConnectCatalogSuccessResponse;
    responses: GetConnectCatalogResponses;
    successes: GetConnectCatalogSuccessResponses;
    errors: GetConnectCatalogErrorResponses;
    parameters: GetConnectCatalogParameters;
    headers: GetConnectCatalogHeaders;
  };
  "getCreatorDisclosurePolicy": {
    request: GetCreatorDisclosurePolicyRequestBody;
    response: GetCreatorDisclosurePolicySuccessResponse;
    responses: GetCreatorDisclosurePolicyResponses;
    successes: GetCreatorDisclosurePolicySuccessResponses;
    errors: GetCreatorDisclosurePolicyErrorResponses;
    parameters: GetCreatorDisclosurePolicyParameters;
    headers: GetCreatorDisclosurePolicyHeaders;
  };
  "updateCreatorDisclosurePolicy": {
    request: UpdateCreatorDisclosurePolicyRequestBody;
    response: UpdateCreatorDisclosurePolicySuccessResponse;
    responses: UpdateCreatorDisclosurePolicyResponses;
    successes: UpdateCreatorDisclosurePolicySuccessResponses;
    errors: UpdateCreatorDisclosurePolicyErrorResponses;
    parameters: UpdateCreatorDisclosurePolicyParameters;
    headers: UpdateCreatorDisclosurePolicyHeaders;
  };
  "listCreatorIdentities": {
    request: ListCreatorIdentitiesRequestBody;
    response: ListCreatorIdentitiesSuccessResponse;
    responses: ListCreatorIdentitiesResponses;
    successes: ListCreatorIdentitiesSuccessResponses;
    errors: ListCreatorIdentitiesErrorResponses;
    parameters: ListCreatorIdentitiesParameters;
    headers: ListCreatorIdentitiesHeaders;
  };
  "createCreatorIdentity": {
    request: CreateCreatorIdentityRequestBody;
    response: CreateCreatorIdentitySuccessResponse;
    responses: CreateCreatorIdentityResponses;
    successes: CreateCreatorIdentitySuccessResponses;
    errors: CreateCreatorIdentityErrorResponses;
    parameters: CreateCreatorIdentityParameters;
    headers: CreateCreatorIdentityHeaders;
  };
  "getCreatorIdentity": {
    request: GetCreatorIdentityRequestBody;
    response: GetCreatorIdentitySuccessResponse;
    responses: GetCreatorIdentityResponses;
    successes: GetCreatorIdentitySuccessResponses;
    errors: GetCreatorIdentityErrorResponses;
    parameters: GetCreatorIdentityParameters;
    headers: GetCreatorIdentityHeaders;
  };
  "discloseCreatorIdentity": {
    request: DiscloseCreatorIdentityRequestBody;
    response: DiscloseCreatorIdentitySuccessResponse;
    responses: DiscloseCreatorIdentityResponses;
    successes: DiscloseCreatorIdentitySuccessResponses;
    errors: DiscloseCreatorIdentityErrorResponses;
    parameters: DiscloseCreatorIdentityParameters;
    headers: DiscloseCreatorIdentityHeaders;
  };
  "withdrawCreatorIdentity": {
    request: WithdrawCreatorIdentityRequestBody;
    response: WithdrawCreatorIdentitySuccessResponse;
    responses: WithdrawCreatorIdentityResponses;
    successes: WithdrawCreatorIdentitySuccessResponses;
    errors: WithdrawCreatorIdentityErrorResponses;
    parameters: WithdrawCreatorIdentityParameters;
    headers: WithdrawCreatorIdentityHeaders;
  };
  "getDeveloperOnboarding": {
    request: GetDeveloperOnboardingRequestBody;
    response: GetDeveloperOnboardingSuccessResponse;
    responses: GetDeveloperOnboardingResponses;
    successes: GetDeveloperOnboardingSuccessResponses;
    errors: GetDeveloperOnboardingErrorResponses;
    parameters: GetDeveloperOnboardingParameters;
    headers: GetDeveloperOnboardingHeaders;
  };
  "listDisclosureEvents": {
    request: ListDisclosureEventsRequestBody;
    response: ListDisclosureEventsSuccessResponse;
    responses: ListDisclosureEventsResponses;
    successes: ListDisclosureEventsSuccessResponses;
    errors: ListDisclosureEventsErrorResponses;
    parameters: ListDisclosureEventsParameters;
    headers: ListDisclosureEventsHeaders;
  };
  "createDisclosureEvent": {
    request: CreateDisclosureEventRequestBody;
    response: CreateDisclosureEventSuccessResponse;
    responses: CreateDisclosureEventResponses;
    successes: CreateDisclosureEventSuccessResponses;
    errors: CreateDisclosureEventErrorResponses;
    parameters: CreateDisclosureEventParameters;
    headers: CreateDisclosureEventHeaders;
  };
  "getDisclosurePolicies": {
    request: GetDisclosurePoliciesRequestBody;
    response: GetDisclosurePoliciesSuccessResponse;
    responses: GetDisclosurePoliciesResponses;
    successes: GetDisclosurePoliciesSuccessResponses;
    errors: GetDisclosurePoliciesErrorResponses;
    parameters: GetDisclosurePoliciesParameters;
    headers: GetDisclosurePoliciesHeaders;
  };
  "submitFeedback": {
    request: SubmitFeedbackRequestBody;
    response: SubmitFeedbackSuccessResponse;
    responses: SubmitFeedbackResponses;
    successes: SubmitFeedbackSuccessResponses;
    errors: SubmitFeedbackErrorResponses;
    parameters: SubmitFeedbackParameters;
    headers: SubmitFeedbackHeaders;
  };
  "queryGovernanceAudit": {
    request: QueryGovernanceAuditRequestBody;
    response: QueryGovernanceAuditSuccessResponse;
    responses: QueryGovernanceAuditResponses;
    successes: QueryGovernanceAuditSuccessResponses;
    errors: QueryGovernanceAuditErrorResponses;
    parameters: QueryGovernanceAuditParameters;
    headers: QueryGovernanceAuditHeaders;
  };
  "listGovernanceDeletions": {
    request: ListGovernanceDeletionsRequestBody;
    response: ListGovernanceDeletionsSuccessResponse;
    responses: ListGovernanceDeletionsResponses;
    successes: ListGovernanceDeletionsSuccessResponses;
    errors: ListGovernanceDeletionsErrorResponses;
    parameters: ListGovernanceDeletionsParameters;
    headers: ListGovernanceDeletionsHeaders;
  };
  "createGovernanceDeletion": {
    request: CreateGovernanceDeletionRequestBody;
    response: CreateGovernanceDeletionSuccessResponse;
    responses: CreateGovernanceDeletionResponses;
    successes: CreateGovernanceDeletionSuccessResponses;
    errors: CreateGovernanceDeletionErrorResponses;
    parameters: CreateGovernanceDeletionParameters;
    headers: CreateGovernanceDeletionHeaders;
  };
  "getGovernanceDeletion": {
    request: GetGovernanceDeletionRequestBody;
    response: GetGovernanceDeletionSuccessResponse;
    responses: GetGovernanceDeletionResponses;
    successes: GetGovernanceDeletionSuccessResponses;
    errors: GetGovernanceDeletionErrorResponses;
    parameters: GetGovernanceDeletionParameters;
    headers: GetGovernanceDeletionHeaders;
  };
  "listGovernanceExports": {
    request: ListGovernanceExportsRequestBody;
    response: ListGovernanceExportsSuccessResponse;
    responses: ListGovernanceExportsResponses;
    successes: ListGovernanceExportsSuccessResponses;
    errors: ListGovernanceExportsErrorResponses;
    parameters: ListGovernanceExportsParameters;
    headers: ListGovernanceExportsHeaders;
  };
  "createGovernanceExport": {
    request: CreateGovernanceExportRequestBody;
    response: CreateGovernanceExportSuccessResponse;
    responses: CreateGovernanceExportResponses;
    successes: CreateGovernanceExportSuccessResponses;
    errors: CreateGovernanceExportErrorResponses;
    parameters: CreateGovernanceExportParameters;
    headers: CreateGovernanceExportHeaders;
  };
  "getGovernanceExport": {
    request: GetGovernanceExportRequestBody;
    response: GetGovernanceExportSuccessResponse;
    responses: GetGovernanceExportResponses;
    successes: GetGovernanceExportSuccessResponses;
    errors: GetGovernanceExportErrorResponses;
    parameters: GetGovernanceExportParameters;
    headers: GetGovernanceExportHeaders;
  };
  "listGovernanceLegalHolds": {
    request: ListGovernanceLegalHoldsRequestBody;
    response: ListGovernanceLegalHoldsSuccessResponse;
    responses: ListGovernanceLegalHoldsResponses;
    successes: ListGovernanceLegalHoldsSuccessResponses;
    errors: ListGovernanceLegalHoldsErrorResponses;
    parameters: ListGovernanceLegalHoldsParameters;
    headers: ListGovernanceLegalHoldsHeaders;
  };
  "releaseHistorySnapshot": {
    request: ReleaseHistorySnapshotRequestBody;
    response: ReleaseHistorySnapshotSuccessResponse;
    responses: ReleaseHistorySnapshotResponses;
    successes: ReleaseHistorySnapshotSuccessResponses;
    errors: ReleaseHistorySnapshotErrorResponses;
    parameters: ReleaseHistorySnapshotParameters;
    headers: ReleaseHistorySnapshotHeaders;
  };
  "listIdentityCredentials": {
    request: ListIdentityCredentialsRequestBody;
    response: ListIdentityCredentialsSuccessResponse;
    responses: ListIdentityCredentialsResponses;
    successes: ListIdentityCredentialsSuccessResponses;
    errors: ListIdentityCredentialsErrorResponses;
    parameters: ListIdentityCredentialsParameters;
    headers: ListIdentityCredentialsHeaders;
  };
  "listImageProfiles": {
    request: ListImageProfilesRequestBody;
    response: ListImageProfilesSuccessResponse;
    responses: ListImageProfilesResponses;
    successes: ListImageProfilesSuccessResponses;
    errors: ListImageProfilesErrorResponses;
    parameters: ListImageProfilesParameters;
    headers: ListImageProfilesHeaders;
  };
  "listJobs": {
    request: ListJobsRequestBody;
    response: ListJobsSuccessResponse;
    responses: ListJobsResponses;
    successes: ListJobsSuccessResponses;
    errors: ListJobsErrorResponses;
    parameters: ListJobsParameters;
    headers: ListJobsHeaders;
  };
  "getJob": {
    request: GetJobRequestBody;
    response: GetJobSuccessResponse;
    responses: GetJobResponses;
    successes: GetJobSuccessResponses;
    errors: GetJobErrorResponses;
    parameters: GetJobParameters;
    headers: GetJobHeaders;
  };
  "cancelJob": {
    request: CancelJobRequestBody;
    response: CancelJobSuccessResponse;
    responses: CancelJobResponses;
    successes: CancelJobSuccessResponses;
    errors: CancelJobErrorResponses;
    parameters: CancelJobParameters;
    headers: CancelJobHeaders;
  };
  "createMarkingCheck": {
    request: CreateMarkingCheckRequestBody;
    response: CreateMarkingCheckSuccessResponse;
    responses: CreateMarkingCheckResponses;
    successes: CreateMarkingCheckSuccessResponses;
    errors: CreateMarkingCheckErrorResponses;
    parameters: CreateMarkingCheckParameters;
    headers: CreateMarkingCheckHeaders;
  };
  "getMarkingCheck": {
    request: GetMarkingCheckRequestBody;
    response: GetMarkingCheckSuccessResponse;
    responses: GetMarkingCheckResponses;
    successes: GetMarkingCheckSuccessResponses;
    errors: GetMarkingCheckErrorResponses;
    parameters: GetMarkingCheckParameters;
    headers: GetMarkingCheckHeaders;
  };
  "getCurrentUser": {
    request: GetCurrentUserRequestBody;
    response: GetCurrentUserSuccessResponse;
    responses: GetCurrentUserResponses;
    successes: GetCurrentUserSuccessResponses;
    errors: GetCurrentUserErrorResponses;
    parameters: GetCurrentUserParameters;
    headers: GetCurrentUserHeaders;
  };
  "getOverview": {
    request: GetOverviewRequestBody;
    response: GetOverviewSuccessResponse;
    responses: GetOverviewResponses;
    successes: GetOverviewSuccessResponses;
    errors: GetOverviewErrorResponses;
    parameters: GetOverviewParameters;
    headers: GetOverviewHeaders;
  };
  "getPublicVerifyPage": {
    request: GetPublicVerifyPageRequestBody;
    response: GetPublicVerifyPageSuccessResponse;
    responses: GetPublicVerifyPageResponses;
    successes: GetPublicVerifyPageSuccessResponses;
    errors: GetPublicVerifyPageErrorResponses;
    parameters: GetPublicVerifyPageParameters;
    headers: GetPublicVerifyPageHeaders;
  };
  "createPublicCheck": {
    request: CreatePublicCheckRequestBody;
    response: CreatePublicCheckSuccessResponse;
    responses: CreatePublicCheckResponses;
    successes: CreatePublicCheckSuccessResponses;
    errors: CreatePublicCheckErrorResponses;
    parameters: CreatePublicCheckParameters;
    headers: CreatePublicCheckHeaders;
  };
  "getPublicCheck": {
    request: GetPublicCheckRequestBody;
    response: GetPublicCheckSuccessResponse;
    responses: GetPublicCheckResponses;
    successes: GetPublicCheckSuccessResponses;
    errors: GetPublicCheckErrorResponses;
    parameters: GetPublicCheckParameters;
    headers: GetPublicCheckHeaders;
  };
  "getPublicVerifyPageLogo": {
    request: GetPublicVerifyPageLogoRequestBody;
    response: GetPublicVerifyPageLogoSuccessResponse;
    responses: GetPublicVerifyPageLogoResponses;
    successes: GetPublicVerifyPageLogoSuccessResponses;
    errors: GetPublicVerifyPageLogoErrorResponses;
    parameters: GetPublicVerifyPageLogoParameters;
    headers: GetPublicVerifyPageLogoHeaders;
  };
  "listReceipts": {
    request: ListReceiptsRequestBody;
    response: ListReceiptsSuccessResponse;
    responses: ListReceiptsResponses;
    successes: ListReceiptsSuccessResponses;
    errors: ListReceiptsErrorResponses;
    parameters: ListReceiptsParameters;
    headers: ListReceiptsHeaders;
  };
  "getSigningReceipt": {
    request: GetSigningReceiptRequestBody;
    response: GetSigningReceiptSuccessResponse;
    responses: GetSigningReceiptResponses;
    successes: GetSigningReceiptSuccessResponses;
    errors: GetSigningReceiptErrorResponses;
    parameters: GetSigningReceiptParameters;
    headers: GetSigningReceiptHeaders;
  };
  "listRecipes": {
    request: ListRecipesRequestBody;
    response: ListRecipesSuccessResponse;
    responses: ListRecipesResponses;
    successes: ListRecipesSuccessResponses;
    errors: ListRecipesErrorResponses;
    parameters: ListRecipesParameters;
    headers: ListRecipesHeaders;
  };
  "getRecipe": {
    request: GetRecipeRequestBody;
    response: GetRecipeSuccessResponse;
    responses: GetRecipeResponses;
    successes: GetRecipeSuccessResponses;
    errors: GetRecipeErrorResponses;
    parameters: GetRecipeParameters;
    headers: GetRecipeHeaders;
  };
  "getSharedVerification": {
    request: GetSharedVerificationRequestBody;
    response: GetSharedVerificationSuccessResponse;
    responses: GetSharedVerificationResponses;
    successes: GetSharedVerificationSuccessResponses;
    errors: GetSharedVerificationErrorResponses;
    parameters: GetSharedVerificationParameters;
    headers: GetSharedVerificationHeaders;
  };
  "acceptSigningJob": {
    request: AcceptSigningJobRequestBody;
    response: AcceptSigningJobSuccessResponse;
    responses: AcceptSigningJobResponses;
    successes: AcceptSigningJobSuccessResponses;
    errors: AcceptSigningJobErrorResponses;
    parameters: AcceptSigningJobParameters;
    headers: AcceptSigningJobHeaders;
  };
  "acceptSigningJobBatch": {
    request: AcceptSigningJobBatchRequestBody;
    response: AcceptSigningJobBatchSuccessResponse;
    responses: AcceptSigningJobBatchResponses;
    successes: AcceptSigningJobBatchSuccessResponses;
    errors: AcceptSigningJobBatchErrorResponses;
    parameters: AcceptSigningJobBatchParameters;
    headers: AcceptSigningJobBatchHeaders;
  };
  "createUpload": {
    request: CreateUploadRequestBody;
    response: CreateUploadSuccessResponse;
    responses: CreateUploadResponses;
    successes: CreateUploadSuccessResponses;
    errors: CreateUploadErrorResponses;
    parameters: CreateUploadParameters;
    headers: CreateUploadHeaders;
  };
  "abortUpload": {
    request: AbortUploadRequestBody;
    response: AbortUploadSuccessResponse;
    responses: AbortUploadResponses;
    successes: AbortUploadSuccessResponses;
    errors: AbortUploadErrorResponses;
    parameters: AbortUploadParameters;
    headers: AbortUploadHeaders;
  };
  "completeUpload": {
    request: CompleteUploadRequestBody;
    response: CompleteUploadSuccessResponse;
    responses: CompleteUploadResponses;
    successes: CompleteUploadSuccessResponses;
    errors: CompleteUploadErrorResponses;
    parameters: CompleteUploadParameters;
    headers: CompleteUploadHeaders;
  };
  "getUsage": {
    request: GetUsageRequestBody;
    response: GetUsageSuccessResponse;
    responses: GetUsageResponses;
    successes: GetUsageSuccessResponses;
    errors: GetUsageErrorResponses;
    parameters: GetUsageParameters;
    headers: GetUsageHeaders;
  };
  "getVerificationEvidence": {
    request: GetVerificationEvidenceRequestBody;
    response: GetVerificationEvidenceSuccessResponse;
    responses: GetVerificationEvidenceResponses;
    successes: GetVerificationEvidenceSuccessResponses;
    errors: GetVerificationEvidenceErrorResponses;
    parameters: GetVerificationEvidenceParameters;
    headers: GetVerificationEvidenceHeaders;
  };
  "createVerificationReport": {
    request: CreateVerificationReportRequestBody;
    response: CreateVerificationReportSuccessResponse;
    responses: CreateVerificationReportResponses;
    successes: CreateVerificationReportSuccessResponses;
    errors: CreateVerificationReportErrorResponses;
    parameters: CreateVerificationReportParameters;
    headers: CreateVerificationReportHeaders;
  };
  "listVerificationShares": {
    request: ListVerificationSharesRequestBody;
    response: ListVerificationSharesSuccessResponse;
    responses: ListVerificationSharesResponses;
    successes: ListVerificationSharesSuccessResponses;
    errors: ListVerificationSharesErrorResponses;
    parameters: ListVerificationSharesParameters;
    headers: ListVerificationSharesHeaders;
  };
  "createVerificationShare": {
    request: CreateVerificationShareRequestBody;
    response: CreateVerificationShareSuccessResponse;
    responses: CreateVerificationShareResponses;
    successes: CreateVerificationShareSuccessResponses;
    errors: CreateVerificationShareErrorResponses;
    parameters: CreateVerificationShareParameters;
    headers: CreateVerificationShareHeaders;
  };
  "getVerificationHistory": {
    request: GetVerificationHistoryRequestBody;
    response: GetVerificationHistorySuccessResponse;
    responses: GetVerificationHistoryResponses;
    successes: GetVerificationHistorySuccessResponses;
    errors: GetVerificationHistoryErrorResponses;
    parameters: GetVerificationHistoryParameters;
    headers: GetVerificationHistoryHeaders;
  };
  "getVerificationReport": {
    request: GetVerificationReportRequestBody;
    response: GetVerificationReportSuccessResponse;
    responses: GetVerificationReportResponses;
    successes: GetVerificationReportSuccessResponses;
    errors: GetVerificationReportErrorResponses;
    parameters: GetVerificationReportParameters;
    headers: GetVerificationReportHeaders;
  };
  "closeVerificationShare": {
    request: CloseVerificationShareRequestBody;
    response: CloseVerificationShareSuccessResponse;
    responses: CloseVerificationShareResponses;
    successes: CloseVerificationShareSuccessResponses;
    errors: CloseVerificationShareErrorResponses;
    parameters: CloseVerificationShareParameters;
    headers: CloseVerificationShareHeaders;
  };
  "listVerifications": {
    request: ListVerificationsRequestBody;
    response: ListVerificationsSuccessResponse;
    responses: ListVerificationsResponses;
    successes: ListVerificationsSuccessResponses;
    errors: ListVerificationsErrorResponses;
    parameters: ListVerificationsParameters;
    headers: ListVerificationsHeaders;
  };
  "createVerification": {
    request: CreateVerificationRequestBody;
    response: CreateVerificationSuccessResponse;
    responses: CreateVerificationResponses;
    successes: CreateVerificationSuccessResponses;
    errors: CreateVerificationErrorResponses;
    parameters: CreateVerificationParameters;
    headers: CreateVerificationHeaders;
  };
  "getVerification": {
    request: GetVerificationRequestBody;
    response: GetVerificationSuccessResponse;
    responses: GetVerificationResponses;
    successes: GetVerificationSuccessResponses;
    errors: GetVerificationErrorResponses;
    parameters: GetVerificationParameters;
    headers: GetVerificationHeaders;
  };
  "createVerificationBatch": {
    request: CreateVerificationBatchRequestBody;
    response: CreateVerificationBatchSuccessResponse;
    responses: CreateVerificationBatchResponses;
    successes: CreateVerificationBatchSuccessResponses;
    errors: CreateVerificationBatchErrorResponses;
    parameters: CreateVerificationBatchParameters;
    headers: CreateVerificationBatchHeaders;
  };
  "getVerifyPage": {
    request: GetVerifyPageRequestBody;
    response: GetVerifyPageSuccessResponse;
    responses: GetVerifyPageResponses;
    successes: GetVerifyPageSuccessResponses;
    errors: GetVerifyPageErrorResponses;
    parameters: GetVerifyPageParameters;
    headers: GetVerifyPageHeaders;
  };
  "putVerifyPage": {
    request: PutVerifyPageRequestBody;
    response: PutVerifyPageSuccessResponse;
    responses: PutVerifyPageResponses;
    successes: PutVerifyPageSuccessResponses;
    errors: PutVerifyPageErrorResponses;
    parameters: PutVerifyPageParameters;
    headers: PutVerifyPageHeaders;
  };
  "listWebhookEndpoints": {
    request: ListWebhookEndpointsRequestBody;
    response: ListWebhookEndpointsSuccessResponse;
    responses: ListWebhookEndpointsResponses;
    successes: ListWebhookEndpointsSuccessResponses;
    errors: ListWebhookEndpointsErrorResponses;
    parameters: ListWebhookEndpointsParameters;
    headers: ListWebhookEndpointsHeaders;
  };
  "createWebhookEndpoint": {
    request: CreateWebhookEndpointRequestBody;
    response: CreateWebhookEndpointSuccessResponse;
    responses: CreateWebhookEndpointResponses;
    successes: CreateWebhookEndpointSuccessResponses;
    errors: CreateWebhookEndpointErrorResponses;
    parameters: CreateWebhookEndpointParameters;
    headers: CreateWebhookEndpointHeaders;
  };
  "deleteWebhookEndpoint": {
    request: DeleteWebhookEndpointRequestBody;
    response: DeleteWebhookEndpointSuccessResponse;
    responses: DeleteWebhookEndpointResponses;
    successes: DeleteWebhookEndpointSuccessResponses;
    errors: DeleteWebhookEndpointErrorResponses;
    parameters: DeleteWebhookEndpointParameters;
    headers: DeleteWebhookEndpointHeaders;
  };
  "getWebhookEndpoint": {
    request: GetWebhookEndpointRequestBody;
    response: GetWebhookEndpointSuccessResponse;
    responses: GetWebhookEndpointResponses;
    successes: GetWebhookEndpointSuccessResponses;
    errors: GetWebhookEndpointErrorResponses;
    parameters: GetWebhookEndpointParameters;
    headers: GetWebhookEndpointHeaders;
  };
  "updateWebhookEndpoint": {
    request: UpdateWebhookEndpointRequestBody;
    response: UpdateWebhookEndpointSuccessResponse;
    responses: UpdateWebhookEndpointResponses;
    successes: UpdateWebhookEndpointSuccessResponses;
    errors: UpdateWebhookEndpointErrorResponses;
    parameters: UpdateWebhookEndpointParameters;
    headers: UpdateWebhookEndpointHeaders;
  };
  "listWebhookDeliveries": {
    request: ListWebhookDeliveriesRequestBody;
    response: ListWebhookDeliveriesSuccessResponse;
    responses: ListWebhookDeliveriesResponses;
    successes: ListWebhookDeliveriesSuccessResponses;
    errors: ListWebhookDeliveriesErrorResponses;
    parameters: ListWebhookDeliveriesParameters;
    headers: ListWebhookDeliveriesHeaders;
  };
  "disableWebhookEndpoint": {
    request: DisableWebhookEndpointRequestBody;
    response: DisableWebhookEndpointSuccessResponse;
    responses: DisableWebhookEndpointResponses;
    successes: DisableWebhookEndpointSuccessResponses;
    errors: DisableWebhookEndpointErrorResponses;
    parameters: DisableWebhookEndpointParameters;
    headers: DisableWebhookEndpointHeaders;
  };
  "enableWebhookEndpoint": {
    request: EnableWebhookEndpointRequestBody;
    response: EnableWebhookEndpointSuccessResponse;
    responses: EnableWebhookEndpointResponses;
    successes: EnableWebhookEndpointSuccessResponses;
    errors: EnableWebhookEndpointErrorResponses;
    parameters: EnableWebhookEndpointParameters;
    headers: EnableWebhookEndpointHeaders;
  };
  "rotateWebhookEndpointSecret": {
    request: RotateWebhookEndpointSecretRequestBody;
    response: RotateWebhookEndpointSecretSuccessResponse;
    responses: RotateWebhookEndpointSecretResponses;
    successes: RotateWebhookEndpointSecretSuccessResponses;
    errors: RotateWebhookEndpointSecretErrorResponses;
    parameters: RotateWebhookEndpointSecretParameters;
    headers: RotateWebhookEndpointSecretHeaders;
  };
  "completeWebhookEndpointSecretOverlap": {
    request: CompleteWebhookEndpointSecretOverlapRequestBody;
    response: CompleteWebhookEndpointSecretOverlapSuccessResponse;
    responses: CompleteWebhookEndpointSecretOverlapResponses;
    successes: CompleteWebhookEndpointSecretOverlapSuccessResponses;
    errors: CompleteWebhookEndpointSecretOverlapErrorResponses;
    parameters: CompleteWebhookEndpointSecretOverlapParameters;
    headers: CompleteWebhookEndpointSecretOverlapHeaders;
  };
  "sendWebhookTestEvent": {
    request: SendWebhookTestEventRequestBody;
    response: SendWebhookTestEventSuccessResponse;
    responses: SendWebhookTestEventResponses;
    successes: SendWebhookTestEventSuccessResponses;
    errors: SendWebhookTestEventErrorResponses;
    parameters: SendWebhookTestEventParameters;
    headers: SendWebhookTestEventHeaders;
  };
  "getWebhookDelivery": {
    request: GetWebhookDeliveryRequestBody;
    response: GetWebhookDeliverySuccessResponse;
    responses: GetWebhookDeliveryResponses;
    successes: GetWebhookDeliverySuccessResponses;
    errors: GetWebhookDeliveryErrorResponses;
    parameters: GetWebhookDeliveryParameters;
    headers: GetWebhookDeliveryHeaders;
  };
  "listWebhookDeliveryAttempts": {
    request: ListWebhookDeliveryAttemptsRequestBody;
    response: ListWebhookDeliveryAttemptsSuccessResponse;
    responses: ListWebhookDeliveryAttemptsResponses;
    successes: ListWebhookDeliveryAttemptsSuccessResponses;
    errors: ListWebhookDeliveryAttemptsErrorResponses;
    parameters: ListWebhookDeliveryAttemptsParameters;
    headers: ListWebhookDeliveryAttemptsHeaders;
  };
  "replayWebhookDelivery": {
    request: ReplayWebhookDeliveryRequestBody;
    response: ReplayWebhookDeliverySuccessResponse;
    responses: ReplayWebhookDeliveryResponses;
    successes: ReplayWebhookDeliverySuccessResponses;
    errors: ReplayWebhookDeliveryErrorResponses;
    parameters: ReplayWebhookDeliveryParameters;
    headers: ReplayWebhookDeliveryHeaders;
  };
  "getWebhookEventCatalog": {
    request: GetWebhookEventCatalogRequestBody;
    response: GetWebhookEventCatalogSuccessResponse;
    responses: GetWebhookEventCatalogResponses;
    successes: GetWebhookEventCatalogSuccessResponses;
    errors: GetWebhookEventCatalogErrorResponses;
    parameters: GetWebhookEventCatalogParameters;
    headers: GetWebhookEventCatalogHeaders;
  };
  "replayWebhookEvent": {
    request: ReplayWebhookEventRequestBody;
    response: ReplayWebhookEventSuccessResponse;
    responses: ReplayWebhookEventResponses;
    successes: ReplayWebhookEventSuccessResponses;
    errors: ReplayWebhookEventErrorResponses;
    parameters: ReplayWebhookEventParameters;
    headers: ReplayWebhookEventHeaders;
  };
  "listWorkflowTemplates": {
    request: ListWorkflowTemplatesRequestBody;
    response: ListWorkflowTemplatesSuccessResponse;
    responses: ListWorkflowTemplatesResponses;
    successes: ListWorkflowTemplatesSuccessResponses;
    errors: ListWorkflowTemplatesErrorResponses;
    parameters: ListWorkflowTemplatesParameters;
    headers: ListWorkflowTemplatesHeaders;
  };
  "createWorkflowTemplate": {
    request: CreateWorkflowTemplateRequestBody;
    response: CreateWorkflowTemplateSuccessResponse;
    responses: CreateWorkflowTemplateResponses;
    successes: CreateWorkflowTemplateSuccessResponses;
    errors: CreateWorkflowTemplateErrorResponses;
    parameters: CreateWorkflowTemplateParameters;
    headers: CreateWorkflowTemplateHeaders;
  };
  "deleteWorkflowTemplate": {
    request: DeleteWorkflowTemplateRequestBody;
    response: DeleteWorkflowTemplateSuccessResponse;
    responses: DeleteWorkflowTemplateResponses;
    successes: DeleteWorkflowTemplateSuccessResponses;
    errors: DeleteWorkflowTemplateErrorResponses;
    parameters: DeleteWorkflowTemplateParameters;
    headers: DeleteWorkflowTemplateHeaders;
  };
  "getWorkflowTemplate": {
    request: GetWorkflowTemplateRequestBody;
    response: GetWorkflowTemplateSuccessResponse;
    responses: GetWorkflowTemplateResponses;
    successes: GetWorkflowTemplateSuccessResponses;
    errors: GetWorkflowTemplateErrorResponses;
    parameters: GetWorkflowTemplateParameters;
    headers: GetWorkflowTemplateHeaders;
  };
  "replaceWorkflowTemplate": {
    request: ReplaceWorkflowTemplateRequestBody;
    response: ReplaceWorkflowTemplateSuccessResponse;
    responses: ReplaceWorkflowTemplateResponses;
    successes: ReplaceWorkflowTemplateSuccessResponses;
    errors: ReplaceWorkflowTemplateErrorResponses;
    parameters: ReplaceWorkflowTemplateParameters;
    headers: ReplaceWorkflowTemplateHeaders;
  };
  "receiveClerkWebhook": {
    request: ReceiveClerkWebhookRequestBody;
    response: ReceiveClerkWebhookSuccessResponse;
    responses: ReceiveClerkWebhookResponses;
    successes: ReceiveClerkWebhookSuccessResponses;
    errors: ReceiveClerkWebhookErrorResponses;
    parameters: ReceiveClerkWebhookParameters;
    headers: ReceiveClerkWebhookHeaders;
  };
  "receiveStripeWebhook": {
    request: ReceiveStripeWebhookRequestBody;
    response: ReceiveStripeWebhookSuccessResponse;
    responses: ReceiveStripeWebhookResponses;
    successes: ReceiveStripeWebhookSuccessResponses;
    errors: ReceiveStripeWebhookErrorResponses;
    parameters: ReceiveStripeWebhookParameters;
    headers: ReceiveStripeWebhookHeaders;
  };
}

export interface WebhookOperationModels {
  "listWebhookEndpoints": PublicApiOperationModels["listWebhookEndpoints"];
  "createWebhookEndpoint": PublicApiOperationModels["createWebhookEndpoint"];
  "deleteWebhookEndpoint": PublicApiOperationModels["deleteWebhookEndpoint"];
  "getWebhookEndpoint": PublicApiOperationModels["getWebhookEndpoint"];
  "updateWebhookEndpoint": PublicApiOperationModels["updateWebhookEndpoint"];
  "listWebhookDeliveries": PublicApiOperationModels["listWebhookDeliveries"];
  "disableWebhookEndpoint": PublicApiOperationModels["disableWebhookEndpoint"];
  "enableWebhookEndpoint": PublicApiOperationModels["enableWebhookEndpoint"];
  "rotateWebhookEndpointSecret": PublicApiOperationModels["rotateWebhookEndpointSecret"];
  "completeWebhookEndpointSecretOverlap": PublicApiOperationModels["completeWebhookEndpointSecretOverlap"];
  "sendWebhookTestEvent": PublicApiOperationModels["sendWebhookTestEvent"];
  "getWebhookDelivery": PublicApiOperationModels["getWebhookDelivery"];
  "listWebhookDeliveryAttempts": PublicApiOperationModels["listWebhookDeliveryAttempts"];
  "replayWebhookDelivery": PublicApiOperationModels["replayWebhookDelivery"];
  "getWebhookEventCatalog": PublicApiOperationModels["getWebhookEventCatalog"];
}

export interface HistorySuccessByOperationId {
  "getAssetDetail": AssetDetailResponse;
  "getCapabilities": CapabilityDiscoveryResponse;
  "getRecipe": RecipeCatalogResponse;
  "getVerificationHistory": VerificationHistoryResponse;
  "listAssets": AssetHistoryPageResponse;
  "listImageProfiles": ImageProfileListResponse;
  "listJobs": JobHistoryPageResponse;
  "listReceipts": ReceiptHistoryPageResponse;
  "listRecipes": RecipeListResponse;
  "listVerifications": VerificationHistoryPageResponse;
  "releaseHistorySnapshot": undefined;
}

export type HistorySuccess<OperationId extends keyof HistorySuccessByOperationId> =
  HistorySuccessByOperationId[OperationId];

export interface PublicApiModels {
  webhooks: WebhookOperationModels;
  history: HistorySuccessByOperationId;
}
