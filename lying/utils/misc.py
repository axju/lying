"""Some tools"""
from logging import getLogger


class ClassLogger():
    """docstring for ClassLogger."""

    def __init__(self):
        self.logger = getLogger(self.__class__.__name__)
        self.logger.debug('Create a "%s" object', self.__class__.__name__)


class Output(ClassLogger):
    """docstring for Color."""

    COLORS = {
        'yellow': '\033[93m',
        'red': '\033[91m',
        'blue': '\033[94m',
        'green': '\033[92m',
    }
    DECORS = {
        'header': '\033[95m',
        'blod': '\033[1m',
        'underline': '\033[4m',
    }
    ENDC = '\033[0m'

    def __init__(self, stdout):
        super(Output, self).__init__()
        self.stdout = stdout

    def write(self, mes='', color='', decors=[], endl='\n'):
        begin = self.COLORS.get(color, '')
        begin += ''.join([self.DECORS.get(decor, '') for decor in decors])
        ende = self.ENDC if begin else ''
        self.stdout.write(begin + mes + ende + endl)
        self.stdout.flush()

    def red(self, mes, decors=[], endl='\n'):
        self.write(mes, 'red', decors=decors, endl=endl)
