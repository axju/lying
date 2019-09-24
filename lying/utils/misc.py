"""Some tools"""
from logging import getLogger, basicConfig


def setup_root_logger(level=10):
    """Setup the gloabl logger"""
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    basicConfig(level=level, format=log_format)


class ClassLogger():
    """docstring for ClassLogger."""

    def __init__(self):
        self.logger = getLogger(self.__class__.__name__)
        self.logger.debug('Create a "%s" object', self.__class__.__name__)
