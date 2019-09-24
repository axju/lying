import unittest
from lying.render.basic import BasicRender
from lying.utils.settings import Settings


class TestBasicRender(unittest.TestCase):

    def test_basic_render(self):
        settings = Settings()
        render = BasicRender(settings)
        self.assertIsInstance(render.conf, Settings)


if __name__ == '__main__':
    unittest.main()
