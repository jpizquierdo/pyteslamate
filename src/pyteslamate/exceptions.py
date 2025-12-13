"""Custom exceptions for TeslaMate API client."""


class TeslamateError(Exception):
    """Base exception for all API client errors."""

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


class TeslamateAuthenticationError(TeslamateError):
    """Raised when authentication fails (401)."""

    def __init__(self, message: str = "Authentication failed") -> None:
        super().__init__(message)


class TeslamateNotFoundError(TeslamateError):
    """Raised when a resource is not found (404)."""

    def __init__(self, message: str = "Resource not found") -> None:
        super().__init__(message)


class TeslamateRateLimitError(TeslamateError):
    """Raised when rate limit is exceeded (429)."""

    def __init__(self, message: str = "Rate limit exceeded") -> None:
        super().__init__(message)


class TeslamateValidationError(TeslamateError):
    """Raised when request or response validation fails."""

    def __init__(self, message: str) -> None:
        super().__init__(message)


class TeslamateServerError(TeslamateError):
    """Raised when server returns 5xx error."""

    def __init__(self, message: str = "Server error occurred") -> None:
        super().__init__(message)


class TeslamateTimeoutError(TeslamateError):
    """Raised when a request times out."""

    def __init__(self, message: str = "Request timed out") -> None:
        super().__init__(message)
