from collections.abc import AsyncGenerator

import pytest

from pyteslamate.pyteslamate import Teslamate


@pytest.fixture
def base_url() -> str:
    return "https://api.example.com"


@pytest.fixture
def api_key() -> str:
    return "test-api-key"


@pytest.fixture
async def teslamate_client(base_url: str, api_key: str) -> AsyncGenerator[Teslamate, None]:
    async with Teslamate(base_url=base_url, api_key=api_key) as teslamate_client:
        yield teslamate_client
