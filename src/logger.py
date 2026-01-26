import logging


def setup_logger() -> logging.Logger:
    logging.basicConfig(
        encoding='utf-8',
        format='[%(asctime)s] (%(levelname)s): %(message)s',
        datefmt='%m-%d-%Y %I:%M:%S %p',
        level=logging.INFO,
        # handlers=[
        #     logging.StreamHandler()
        # ]
    )
    return logging.getLogger(__name__)

logger = setup_logger()
