#logger.py

import logging
import datetime as dt

#Create and configure logger
def setup_logger():  # pylint: disable=missing-class-docstring

    log_file_name = dt.datetime.now().strftime("%d-%m-%Y_%H-%M-%S.log")
    logger = logging.getLogger("scraper_logger")
    logger.setLevel(logging.DEBUG)

    # Create a file handler and set the logging level
    file_handler = logging.FileHandler(log_file_name)
    file_handler.setLevel(logging.DEBUG)
    
    # Create a console handler and set the logging level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Create a formatter and attach it to the handlers
    formatter = logging.Formatter("%(asctime)s %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


logger = setup_logger()
