import unittest
from tires import OctoprimeTire

class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service(self):
        states = [0.5,0.4,0,0]
        tires = OctoprimeTire(states)
        self.assertTrue(tires.needs_service())

    def test_dont_service(self):
        states = [0,0,0,0]
        tires = OctoprimeTire(states)
        self.assertFalse(tires.needs_service())


if __name__ == '__main__':
    unittest.main()
