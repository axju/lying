"""Some tools"""
from types import SimpleNamespace
from lying.utils.misc import ClassLogger


class BasicRender(ClassLogger):
    """The basic render class"""

    __kwargs__ = {}
    __chief__ = ''

    def __init__(self, conf):
        super(BasicRender, self).__init__()
        self.conf = conf
        self.kwargs = SimpleNamespace()

    def get_kwargs(self, kwargs):
        dummy = kwargs
        for name, kind in self.__kwargs__.items():
            if isinstance(kind, (tuple, list)):
                dummy[name] = kind[0](kwargs.get(name, kind[1]))
            elif isinstance(kind, type):
                dummy[name] = kwargs.get(name, kind())
        self.kwargs = SimpleNamespace(**dummy)

    def render(self, **kwargs):
        """Override this feature in your class"""
        self.logger.debug('Call render %s with %s', self.__class__.__name__, kwargs)
        self.get_kwargs(kwargs)
