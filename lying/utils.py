"""Some tools"""
import os
import sys
from shutil import get_terminal_size
from time import sleep
from random import random
from logging import getLogger
from pyfiglet import Figlet, DEFAULT_FONT


class Terminal():
    """docstring for Terminal."""

    DEFAULT_PROMPT = '>>> '
    DEFAULT_WIDTH = 130

    def __init__(self, cmds, prompt=None, width=None,
                 stdout=sys.stdout, wait=2, setup=True):
        super(Terminal, self).__init__()
        self.logger = getLogger('Terminal')
        self.logger.debug('Create a Terminal object')

        if not isinstance(cmds, list):
            raise Exception('"cmds" must be a list!')

        self.cmds = cmds
        self.prompt = prompt
        self.width = width
        self.stdout = stdout
        self.wait = wait

        if setup:
            self.setup()

    def setup(self):
        """Set prompt and width"""
        if not self.prompt:
            self.prompt = os.environ.get('PS1', self.DEFAULT_PROMPT)

        if not self.width:
            self.width, _ = get_terminal_size(
                                fallback=(self.DEFAULT_WIDTH, 24))

    def check_cmd(self, cmd):
        """Verify the command structure. No Exception, only a message"""
        if not isinstance(cmd, dict):
            self.logger.info('Every command must be a dict.')
            return False

        if 'input' not in cmd:
            self.logger.info('Wrong command format. No "input" key.')
            return False

        if not isinstance(cmd['input'], str):
            self.logger.info('The input value must be a string.')
            return False

        return True

    def progressbar(self, step=0.2):
        """Animate a progress bar"""
        for i in range(self.width-8+1):
            format_string = '{}{} {:6.2f}%'.format(
                '#' * i, '.' * (self.width-8-i), 100 * i / (self.width - 8)
            )
            self.print_str(format_string, end='\r')
            sleep(random()*step)
        self.print_str()

    def print_str(self, mes='', end='\n'):
        """a print function to customiz the stdout"""
        self.stdout.write(mes+end)
        self.stdout.flush()

    def print_input(self, command, end='\n'):
        """Animate the input with the prompt."""
        self.print_str(self.prompt, end='')
        for char in command + end:
            sleep(self.wait*random())
            self.print_str(char, end='')

    def print_output(self, command):
        """Print or animate output"""
        if 'text' in command:
            self.print_str(command['text'])
        elif 'title' in command:
            figlet = Figlet(
                width=self.width, font=command.get('font', DEFAULT_FONT),
                justify=command.get('justify', 'center')
            )
            self.print_str(figlet.renderText(command['title']))
        elif 'progressbar' in command:
            self.progressbar()
        elif 'sleep' in command:
            sleep(command['sleep'])

    def run(self, clear=True, auto_exit=False):
        """Run everything"""
        if clear:
            os.system('cls' if os.name == 'nt' else 'clear')

        for cmd in self.cmds:
            if not self.check_cmd(cmd):
                continue

            self.print_input(cmd['input'])

            if 'output' in cmd:
                if isinstance(cmd['output'], dict):
                    self.print_output(cmd['output'])
                elif isinstance(cmd['output'], list):
                    for output in cmd['output']:
                        self.print_output(output)
            else:
                os.system(cmd['input'])

        if not auto_exit:
            self.print_input('', end='')
            input()
