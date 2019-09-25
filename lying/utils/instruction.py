
class Instruction(object):
    """docstring for Instruction."""

    def __init__(self, defaults={}):
        super(Instruction, self).__init__()
        self.defaults = defaults
        self.data = []

    def __iter__(self):
        for name, kwargs in self.data:
            yield name, kwargs

    def load(self, data=None, filename=None):
        if isinstance(data, list):
            for item in data:
                return self.load(data=item)
                
        elif isinstance(data, tuple) and len(data) == 2 and isinstance(data[0], str):
            if isinstance(data[1], dict):
                return self.data.append(data)
            elif data[0] in self.defaults and isinstance(data[1], self.defaults[data[0]][1]):
                return self.data.append((data[0], {self.defaults[data[0]][0]: data[1]}))

        raise TypeError('You can only load a tuple or list')
