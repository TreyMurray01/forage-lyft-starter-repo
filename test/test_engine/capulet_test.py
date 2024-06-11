import unittest
import datetime
from engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service(self):
        current_mileage = 3000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage,last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_dont_service(self):
        current_mileage = 3000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())
    # add assertion here


if __name__ == '__main__':
    unittest.main()
