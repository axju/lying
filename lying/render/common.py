"""Some tools"""
import os
from time import sleep
from random import random
from lying.render.basic import BasicRender


class TextRender(BasicRender):
    """docstring for TextRender."""

    kwargs = {'text': str}

    def render(self, **kwargs):
        """text=ERROR"""
        text = kwargs.get('text', 'ERROR')
        self.conf.stdout.write(text)


class InputRender(BasicRender):
    """docstring for InputRender."""

    kwargs = {'cmd': str}

    def _print_str(self, mes=''):
        """a print function to customiz the stdout"""
        self.conf.stdout.write(mes)
        self.conf.stdout.flush()

    def _print_input(self, command, end='\n'):
        """Animate the input with the prompt."""
        self._print_str('\n' + self.conf.prompt)
        for char in command + end:
            sleep(self.conf.wait*random()/1000)
            self._print_str(char)

    def render(self, **kwargs):
        """cmd=ERROR"""
        cmd = kwargs.get('cmd', 'ERROR')
        self._print_input(cmd)


class CmdRender(InputRender):
    """docstring for CmdRender."""

    kwargs = {'cmd': str}

    def render(self, **kwargs):
        """cmd=pwd"""
        cmd = kwargs.get('cmd', 'ERROR')
        self._print_input(cmd)
        os.system(cmd)
