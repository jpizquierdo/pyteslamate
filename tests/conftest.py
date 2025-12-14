"""Pytest fixtures for the test suite."""

# Allow pytest fixtures to share names (pylint flags them as redefined).
# pylint: disable=redefined-outer-name

from collections.abc import AsyncGenerator

import pytest

from pyteslamate.pyteslamate import Teslamate


@pytest.fixture
def base_url() -> str:
    """Return the base API URL used by tests."""
    return "https://api.example.com"


@pytest.fixture
def api_key() -> str:
    """Return a dummy API key for tests."""
    return "test-api-key"


@pytest.fixture
async def teslamate_client(base_url: str, api_key: str) -> AsyncGenerator[Teslamate, None]:
    """Provide an async Teslamate client instance for tests.

    Uses the base_url and api_key fixtures and yields a client wrapped in the
    client's async context manager so the session is properly initialized/closed.
    """
    async with Teslamate(base_url=base_url, api_key=api_key) as teslamate_client:
        yield teslamate_client
