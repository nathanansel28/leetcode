import logging
import sys


def load_logger(DEBUG: bool):
    # Configure logging to mimic print()
    logging.basicConfig(
        level=logging.DEBUG,  
        format='%(message)s',
        stream=sys.stdout
    )
    logger = logging.getLogger(__name__)

    if not DEBUG:
        logger.setLevel(logging.WARNING)

    return logger