"""Load all entry poins"""
from pkg_resources import iter_entry_points
from lying.utils.misc import ClassLogger


class Dispatchers(ClassLogger):
    """docstring for Dispatcher."""

    def __init__(self):
        super(Dispatchers, self).__init__()
        self.renders = {}
        self.load()

    def __str__(self):
        return ' '.join(['{}={}'.format(key, val) for key, val in self.renders.items()])

    def __getitem__(self, key):
        return self.renders.get(key)

    def __iter__(self):
        for key, value in self.renders.items():
            yield key, value

    def __contains__(self, name):
        return name in self.renders

    def chiefs(self):
        """Return a dictate with the defaults for any render if it exists"""
        result = {}
        for key, value in self.renders.items():
            kwargs = getattr(value, '__kwargs__', {})
            if len(kwargs) == 1:
                result[key] = tuple(next(iter(kwargs.items())))
            elif hasattr(value, '__chief__'):
                result[key] = tuple([value.__chief__, kwargs[value.__chief__]])
        return result

    def load(self):
        """loadthe render from the entry points"""
        self.logger.debug('Register cls')
        for enp in iter_entry_points(group='lying.register'):
            self.logger.debug('Found class "%s"', enp.name)
            cls = enp.load()
            self.renders[enp.name] = cls
