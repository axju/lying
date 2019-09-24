"""Some tools"""
import os
import json
from lying.utils.misc import ClassLogger
from lying.utils.settings import Settings
from lying.utils.dispatch import Dispatchers


class Terminal(ClassLogger):
    """docstring for Terminal."""

    def __init__(self, **kwargs):
        """prompt=None, width=None, stdout=sys.stdout, wait=2000"""
        super(Terminal, self).__init__()
        self.dispatchers = Dispatchers()
        self.settings = Settings(**kwargs)
        self.instruction = []

    def clean(self, data):
        for render, kwargs in data.items():
            if render not in self.dispatchers:
                raise Exception('No render for "%s"', render)

            if isinstance(kwargs, dict):
                self.instruction.append((render, kwargs))

            elif len(self.dispatchers[render, 'kwargs']) == 1:
                name, kind = next(iter(self.dispatchers[render, 'kwargs'].items()))
                if isinstance(kwargs, kind):
                    self.instruction.append((render, {name: kwargs}))
                else:
                    raise Exception()
            else:
                raise Exception()

    def load(self, data=None, filename=None):
        """Load data from file, list or dict"""
        if filename:
            with open(filename) as file:
                data = json.load(file)
        if isinstance(data, list):
            for item in data:
                self.load(item)
        elif isinstance(data, dict):
            self.clean(data)
        else:
            raise TabError('You can only load a dict or list')

    def run_inst(self, item):
        """Recursive call to render"""
        self.logger.debug('Run item "%s"', item)
        if isinstance(item, dict):
            for name, kwargs in item.items():
                self.render[name].render(**kwargs)
        elif isinstance(item, list):
            for sub_item in item:
                self.run_item(sub_item)

    def run(self, clear=True, auto_exit=False):
        """Run everything"""
        if clear:
            os.system('cls' if os.name == 'nt' else 'clear')

        for name, kwargs in self.instruction:
            render = self.dispatchers[name, 'obj', self.settings]
            render.render(**kwargs)

        if not auto_exit:
            self.settings.stdout.write(self.settings.prompt)
            input()
