import unittest
from lying.utils.dispatch import Dispatchers
from lying.render.basic import BasicRender


class TestDispatcher(unittest.TestCase):

    def test_basic_render(self):
        dispatcher = Dispatchers()
        for name, render in dict(dispatcher).items():
            self.assertTrue(issubclass(render, BasicRender))
            self.assertTrue(issubclass(dispatcher[name], BasicRender))

    def test_str(self):
        self.assertIsInstance(Dispatchers().__str__(), str)
        self.assertIsInstance(str(Dispatchers()), str)


if __name__ == '__main__':
    unittest.main()
