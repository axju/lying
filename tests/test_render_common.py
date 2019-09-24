import unittest
from io import StringIO
from lying.utils.settings import Settings
from lying.render.common import TextRender, CmdRender, InputRender


class TestCommonRender(unittest.TestCase):

    def call_render(self, cls, **kwargs):
        with StringIO() as stdout:
            settings = Settings(stdout=stdout, wait=0)
            render = cls(settings)
            render.render(**kwargs)
            output = stdout.getvalue()
        return output

    def test_text_render(self):
        output = self.call_render(TextRender, text='foo')
        self.assertEqual(output, 'foo')

    def test_cmd_render(self):
        output = self.call_render(CmdRender)
        self.assertEqual(output, '')

    def test_input_render(self):
        output = self.call_render(InputRender)
        self.assertEqual(output, '\n>>> ERROR\n')


if __name__ == '__main__':
    unittest.main()
