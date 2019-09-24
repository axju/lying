"""Some tools"""
from lying.utils.misc import ClassLogger


class BasicRender(ClassLogger):
    """The basic render class"""

    def __init__(self, conf):
        super(BasicRender, self).__init__()
        self.conf = conf

    def render(self, **kwargs):
        """Override this feature in your class"""
        self.logger.debug(
            'Call render %s with %s', self.__class__.__name__, kwargs)
