import logging
import typing

from concord.sentinel import Sentinel

__all__ = ("setup_logger",)


def setup_logger(
    log_level: int = logging.INFO,
    handler: (
        logging.Handler | None | typing.Literal[Sentinel.NOT_GIVEN]
    ) = Sentinel.NOT_GIVEN,
) -> None:
    """
    Setup the logger for Concord.

    :param log_level: The log level to set the logger to.
    :param handler: The handler to use for the logger. If `None` is passed,
                    this function will do nothing. If nothing is passed, a
                    default handler will be used.
    """
    if handler is None:
        return

    if handler is Sentinel.NOT_GIVEN:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter("[%(name)s] [%(asctime)s] [%(levelname)s] %(message)s")
        )

    logger = logging.getLogger("concord")
    logger.setLevel(log_level)
    logger.addHandler(handler)
