"""The settings for the terminal"""
import os
import sys
from shutil import get_terminal_size
from lying.utils.misc import ClassLogger


def get_prompt(default='>>> '):
    """get prompt"""
    return os.environ.get('PS1', default)


def get_width(default=130):
    """get the terminal width"""
    width, _ = get_terminal_size(fallback=(default, 24))
    return width


class Settings(ClassLogger):
    """docstring for Settings."""

    DEFAULTS = {
        'prompt': get_prompt(),
        'width': get_width(),
        'stdout': sys.stdout,
        'fast': False,
    }

    def __init__(self, **kwargs):
        super(Settings, self).__init__()
        self.kwargs = kwargs
        for key, default in self.DEFAULTS.items():
            self.kwargs[key] = kwargs.get(key, default)

    def __str__(self):
        return ' '.join(
            ['{}="{}"'.format(key, val) for key, val in self.kwargs.items()])

    def __getitem__(self, key):
        self.logger.debug('Call __getitem__ key="%s"', key)
        return self.kwargs.get(key)

    def __getattr__(self, attr):
        self.logger.debug('Call __getattr__ "%s"', attr)
        if attr in self.kwargs:
            return self.kwargs.get(attr)
        raise AttributeError

    def load(self, **kwargs):
        """load some settings"""
        self.kwargs.update(kwargs)
