import unittest
from lying.utils.settings import Settings
from lying.utils.settings import get_prompt, get_width


class TestFuncs(unittest.TestCase):

    def test_get_prompt(self):
        self.assertIsInstance(get_prompt('test'), str)

    def test_get_width(self):
        self.assertIsInstance(get_width(100), int)


class TestSettings(unittest.TestCase):

    def test_defaults(self):
        settings = Settings()
        for key, value in settings.DEFAULTS.items():
            self.assertEqual(settings[key], value)

    def test_kwargs(self):
        settings = Settings(prompt='foo ')
        self.assertEqual(settings.prompt, 'foo ')
        self.assertEqual(settings['prompt'], 'foo ')

    def test_kwargs_custom(self):
        settings = Settings(custom='foo ')
        self.assertEqual(settings.custom, 'foo ')
        self.assertEqual(settings['custom'], 'foo ')

    def test_magic(self):
        settings = Settings(foo='foo')
        self.assertNotEqual(str(settings).find('foo="foo"'), -1)

        with self.assertRaises(AttributeError):
            settings.test


if __name__ == '__main__':
    unittest.main()
