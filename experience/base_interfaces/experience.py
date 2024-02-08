import logging

# from experience.experience.cat_logger import create_logger
from experience.cat_logger import create_logger

class Experience():
    """ base class for 3Dx application """

    def __init__(self):
        pass

    def logger(self) -> logging.Logger:
        """
        :rtype: logging.Logger
        """
        return create_logger()

    def __repr__(self):
        return 'Experience()'
