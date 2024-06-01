import logging


def configure_logging():
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        filename="backend.log",
        filemode="a",
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    return logger
