from concord.errors import ConcordException

__all__ = (
    "GatewayException",
    "GatewayConnectionException",
)


class GatewayException(ConcordException):
    """Base class for all gateway errors."""


class GatewayConnectionException(GatewayException):
    """Raised when the gateway connection fails."""
