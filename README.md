# Vocode Python Library

[![pypi](https://img.shields.io/pypi/v/vocode-api.svg)](https://pypi.python.org/pypi/vocode-api)
[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)

## Documentation

API documentation is available at [here](https://docs.vocode.dev/).

## Installation

Add this dependency to your project's build file:

```bash
pip install vocode-api
# or
poetry add vocode-api
```

## Usage

```python
from vocode.client import Vocode

vocode_client = Vocode(
  token="YOUR_API_KEY"
)

action_response = vocode_client.actions.get_action(
  id="action_id"
);

print(action_response)
```

## Async Client

```python
from vocode.client import AsyncVocode

import asyncio

vocode_client = AsyncVocode(
  token="YOUR_API_KEY"
)

async def get_action() -> None:
    action_response = vocode_client.actions.get_action(
      id="action_id"
    );
    print(token_response)

asyncio.run(action_response())
```

## Timeouts

By default, the client is configured to have a timeout of 60 seconds. You can customize this value at client instantiation.

```python
from vocode.client import Vocode

vocode_client = Vocode(
  token="YOUR_API_KEY",
  timeout=15
)
```

## Handling Exceptions

All exceptions thrown by the SDK will sublcass [vocode.ApiError](./src/vocode/core/api_error.py).

```python
from vocode.core import ApiError
from vocode import UnprocessableEntityError

try:
  vocode_client.actions.get_action(id="action_id");
except UnprocessableEntityError as e:
  # handle specific error
except APIError as e:
  # handle any api related error
```

Error codes are as followed:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 422         | `UnprocessableEntityError` |

## Beta status

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning the package version to a specific version in your pyproject.toml file. This way, you can install the same version each time without breaking changes unless you are intentionally looking for the latest version.

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically. Additions made directly to this library would have to be moved over to our generation code, otherwise they would be overwritten upon the next generated release. Feel free to open a PR as a proof of concept, but know that we will not be able to merge it as-is. We suggest opening an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
