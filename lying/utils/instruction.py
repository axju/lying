"""The instructions for the terminal"""
from lying.utils.misc import ClassLogger


class Instruction(ClassLogger):
    """docstring for Instruction."""

    def __init__(self, chiefs):
        super(Instruction, self).__init__()
        self.chiefs = chiefs
        self.data = []

    def __iter__(self):
        for name, kwargs in self.data:
            yield name, kwargs

    def load_tuple(self, data):
        """Load data in default format"""
        if isinstance(data, list):
            for item in data:
                self.load_tuple(data=item)

        elif isinstance(data, tuple) and len(data) == 2 and isinstance(data[0], str):
            if isinstance(data[1], dict):
                self.data.append(data)
            elif data[0] in self.chiefs and isinstance(data[1], self.chiefs[data[0]][1]):
                self.data.append((data[0], {self.chiefs[data[0]][0]: data[1]}))
            else:
                raise TypeError('You can only load a tuple or list')
        else:
            raise TypeError('You can only load a tuple or list')

    def load_list(self, data):
        """load datawith list format, usful for json"""
        if not isinstance(data, list):
            raise TypeError('Th data must be a list')

        for item in data:
            if isinstance(item, list):
                self.load_tuple(tuple(item))

    def load(self, data, kind='tuple'):
        """Load function with format for list or tuple"""
        self.logger.debug('Load data="%s"', data)
        if kind == 'tuple':
            self.load_tuple(data)
        elif kind == 'list':
            self.load_list(data)
        else:
            raise Exception('Wrong format')
