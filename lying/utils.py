"""Some tools"""
import os
import sys
from shutil import get_terminal_size
from time import sleep
from random import random
from logging import getLogger
from pyfiglet import Figlet, DEFAULT_FONT


class BasicCommand():

    def __init__(self, stdout):
        self.stdout = stdout

    def render(self):
        pass


class TextCommand(BasicCommand):

    def render(self, **kwargs):
        text = kwargs.get('text', 'ERROR')
        self.stdout.write(text)


class CmdCommand(BasicCommand):

    def redner(self, **kwargs):
        cmd = kwargs.get('cmd', 'pwd')
        os.system(cmd)



class Terminal():
    """docstring for Terminal."""

    DEFAULT_PROMPT = '>>> '
    DEFAULT_WIDTH = 130

    def __init__(self, prompt=None, width=None, stdout=sys.stdout, wait=2000):
        super(Terminal, self).__init__()
        self.logger = getLogger(self.__class__.__name__)
        self.logger.debug('Create a Terminal object')

        self.prompt = prompt
        self.width = width
        self.stdout = stdout
        self.wait = wait
        self.setup = []
        self.cls = {
            'txt': TextCommand(stdout=self.stdout),
            'cmd': CmdCommand(stdout=self.stdout),
        }

    def print_str(self, mes=''):
        """a print function to customiz the stdout"""
        self.stdout.write(mes)
        self.stdout.flush()

    def print_input(self, command, end='\n'):
        """Animate the input with the prompt."""
        self.print_str('\n' + self.prompt)
        for char in command + end:
            sleep(self.wait*random()/1000)
            self.print_str(char)

    def load(self, data=None, filename=None):
        if data:
            self.setup += data
        if filename:
            with open(filename) as file:
                self.setup += json.load(file)

    def run(self, clear=True, auto_exit=False):
        """Run everything"""
        if clear:
            os.system('cls' if os.name == 'nt' else 'clear')

        for item in self.setup:
            kwargs = item.get('kwargs', {})
            self.print_input(item.get('cmd', 'run main'))
            self.cls[item.get('cls', 'txt')].render(**kwargs)

        if not auto_exit:
            self.print_input('', end='')
            input()
