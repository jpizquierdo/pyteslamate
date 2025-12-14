"""Unit tests for the pyteslamate exceptions module."""

from pyteslamate.exceptions import (
    TeslamateAuthenticationError,
    TeslamateError,
    TeslamateNotFoundError,
    TeslamateRateLimitError,
    TeslamateServerError,
)


def test_exception_hierarchy() -> None:
    """Ensure custom exceptions inherit from the base TeslamateError."""
    assert issubclass(TeslamateAuthenticationError, TeslamateError)
    assert issubclass(TeslamateNotFoundError, TeslamateError)
    assert issubclass(TeslamateRateLimitError, TeslamateError)
    assert issubclass(TeslamateServerError, TeslamateError)


def test_exception_str() -> None:
    """Verify the string representation contains the provided message."""
    err = TeslamateAuthenticationError("auth failed")
    assert "auth failed" in str(err)
