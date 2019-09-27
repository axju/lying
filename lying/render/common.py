"""Some tools"""
import os
from lying.render.basic import BasicRender
from lying.render.mixin import OutputMixin, WaitMixin


class WaitRender(WaitMixin, BasicRender):

    __kwargs__ = {
        'wait': (int, 1000),
        'random': (float, 0.3)
    }
    __chief__ = 'wait'

    def render(self, **kwargs):
        """text=ERROR"""
        super(WaitRender, self).render(**kwargs)
        self.wait()


class TextRender(OutputMixin, BasicRender):
    """docstring for TextRender."""

    __kwargs__ = {'text': str, 'color': str, 'end': (str, '\n')}
    __chief__ = 'text'

    def render(self, **kwargs):
        """text=ERROR"""
        super(TextRender, self).render(**kwargs)
        self.output.write(self.kwargs.text, color=self.kwargs.color, endl=self.kwargs.end)


class TextStatusRender(OutputMixin, WaitMixin, BasicRender):
    """Render a text, wait and display fail/success"""

    __kwargs__ = {
        'text': str,
        'result': (str, 'ok'),
        'loop': (int, 3),
        'wait': (int, 1000),
        'random': (float, 0.3)
    }
    __chief__ = 'text'

    def render(self, **kwargs):
        """Render a text, wait and display fail/success"""
        super(TextStatusRender, self).render(**kwargs)
        self.output.write(self.kwargs.text, endl='')
        for _ in range(self.kwargs.loop):
            self.wait()
            self.output.write('.', endl='')
        if self.kwargs.result == 'ok':
            self.output.write(' success', color='green')
        else:
            self.output.write(' fail', color='red')


class InputRender(OutputMixin, WaitMixin, BasicRender):
    """Render a fake command"""

    __kwargs__ = {
        'cmd': str,
        'execute': (bool, True),
        'wait': (int, 200),
        'random': (float, 0.5)
    }
    __chief__ = 'cmd'

    def render(self, **kwargs):
        """cmd=ERROR"""
        super(InputRender, self).render(**kwargs)
        self.output.write(self.conf.prompt, endl='')
        for char in self.kwargs.cmd:
            self.wait()
            self.output.write(char, endl='')

        if self.kwargs.execute:
            self.output.write()


class CmdRender(InputRender):
    """docstring for CmdRender."""

    __kwargs__ = {'cmd': str}

    def render(self, **kwargs):
        """cmd=pwd"""
        kwargs['execute'] = True
        super(CmdRender, self).render(**kwargs)
        os.system(self.kwargs.cmd)
