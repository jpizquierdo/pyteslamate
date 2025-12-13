from pyteslamate.exceptions import (
    TeslamateAuthenticationError,
    TeslamateError,
    TeslamateNotFoundError,
    TeslamateRateLimitError,
    TeslamateServerError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(TeslamateAuthenticationError, TeslamateError)
    assert issubclass(TeslamateNotFoundError, TeslamateError)
    assert issubclass(TeslamateRateLimitError, TeslamateError)
    assert issubclass(TeslamateServerError, TeslamateError)


def test_exception_str() -> None:
    err = TeslamateAuthenticationError("auth failed")
    assert "auth failed" in str(err)
