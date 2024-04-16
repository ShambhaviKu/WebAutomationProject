import logging


def test_print_logs():
    Logger = logging.getLogger(__name__)

    Logger.info("Info log")
    Logger.warning("Warning log")
    Logger.error("Error log")
    Logger.critical("Critical log")
