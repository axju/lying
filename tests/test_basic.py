import unittest
from io import StringIO
from lying.utils import Terminal


class TestTerminal(unittest.TestCase):

    def run_cmds(self, cmds, result, **kwargs):
        with StringIO() as stdout:
            terminal = Terminal(cmds=cmds, stdout=stdout, wait=0, **kwargs)
            terminal.run(clear=False, auto_exit=True)
            output = stdout.getvalue()
        self.assertEqual(output, result)

    def test_text(self):
        cmds = [{'input': 'cat hello.txt', 'output': {'text': 'hello :)'}}]
        result = '>>> cat hello.txt\nhello :)\n'
        self.run_cmds(cmds, result, prompt='>>> ')

    def test_dummy(self):
        self.assertEqual(1, 1)

    def test_title(self):
        cmds = [{'input': 'cat hello.txt', 'output': {'title': 'lying'}}]
        result = """>>> cat hello.txt
              _       _
             | |_   _(_)_ __   __ _
             | | | | | | '_ \ / _` |
             | | |_| | | | | | (_| |
             |_|\__, |_|_| |_|\__, |
                |___/         |___/

"""
        #self.run_cmds(cmds, result, prompt='>>> ', width=50)


if __name__ == '__main__':
    unittest.main()
