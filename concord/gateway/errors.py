from concord.errors import ConcordException

__all__ = (
    "GatewayException",
    "GatewayConnectionException",
    "GatewayFatalException",
    "GatewayReconnectException",
)


class GatewayException(ConcordException):
    """Base class for all gateway errors."""


class GatewayConnectionException(GatewayException):
    """Raised when the gateway connection fails."""


class GatewayFatalException(GatewayException):
    """Raised when the gateway cannot recover from an error."""


class GatewayReconnectException(GatewayException):
    """Raised when the gateway needs to reconnect."""
