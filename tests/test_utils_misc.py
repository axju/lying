import unittest
from logging import Logger
from lying.utils.misc import ClassLogger


class TestClassLogger(unittest.TestCase):

    def test_class_logger(self):
        log = ClassLogger()
        self.assertIsInstance(log.logger, Logger)


if __name__ == '__main__':
    unittest.main()
