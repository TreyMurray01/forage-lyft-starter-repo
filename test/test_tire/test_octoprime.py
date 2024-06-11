import unittest
from tires import CarriganTire

class TestCarriganTire(unittest.TestCase):
    def test_needs_service(self):
        states = [0.5, 0.4, 0, 0]
        tire = CarriganTire(states)
        self.assertTrue(tire.needs_service())

    def test_dont_service(self):
        states = [0.5, 0.4, 0, 0]
        tire = CarriganTire(states)
        self.assertFalse(tire.needs_service())
        # add assertion here


if __name__ == '__main__':
    unittest.main()
