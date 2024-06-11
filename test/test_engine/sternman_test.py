
import unittest
from engine import SternmanEngine


class TestSternmanEngine(unittest.TestCase):
    def test_needs_service(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())  # add assertion here

    def test_dont_service(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
