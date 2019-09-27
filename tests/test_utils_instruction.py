import unittest
from lying.utils.instruction import Instruction


class TestInstruction(unittest.TestCase):

    def test_data(self):
        inst = Instruction({'test': ('cmd', str)})
        data = ('test', {'cmd': 'foo'})
        inst.load(data)

        data = [('test', {'cmd': 'foo'}), ('test', {'cmd': 'foo'})]
        inst.load(data)

        data = ('test', 'foo')
        inst.load(data)

        data = [('test', 'foo'), ('test', 'foo'), ('test', 'foo')]
        inst.load(data)

        for name, kwargs in inst:
            self.assertEqual(name, 'test')
            self.assertEqual(kwargs, {'cmd': 'foo'})


if __name__ == '__main__':
    unittest.main()
