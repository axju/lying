import unittest
from io import StringIO
from lying.terminal import Terminal


class TestTerminal(unittest.TestCase):

    def run_data(self, data):
        with StringIO() as stdout:
            terminal = Terminal(stdout=stdout, wait=0)
            terminal.load(data=data)
            terminal.run(clear=False, auto_exit=True)
            output = stdout.getvalue()
        return output

    def test_load(self):
        pass


if __name__ == '__main__':
    unittest.main()
