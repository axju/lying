"""The Terminal"""
import os
import json
import time
from lying.utils.misc import ClassLogger
from lying.utils.settings import Settings
from lying.utils.dispatch import Dispatchers
from lying.utils.instruction import Instruction


class Terminal(ClassLogger):
    """docstring for Terminal."""

    def __init__(self, **kwargs):
        """prompt=None, width=None, stdout=sys.stdout, wait=2000"""
        super(Terminal, self).__init__()
        self.dispatchers = Dispatchers()
        self.settings = Settings(**kwargs)
        self.instruction = Instruction(self.dispatchers.chiefs())

    def load(self, filename):
        """Load data from file a file"""
        with open(filename) as file:
            data = json.load(file)
        self.instruction.load(data.get('instructions', []), kind='list')
        self.settings.load(**data.get('settings', {}))

    def run(self, clear=True, auto_exit=False, delay=0):
        """Run everything"""
        if clear:
            os.system('cls' if os.name == 'nt' else 'clear')

        self.settings.stdout.flush()
        time.sleep(delay)

        for name, kwargs in self.instruction:
            render = self.dispatchers[name](self.settings)
            render.render(**kwargs)

        if not auto_exit:
            self.dispatchers['input'](self.settings).render(cmd='', execute=False)
            input()
