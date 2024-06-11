import unittest
from battery import NubbinBattery
import datetime

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service(self):

        current_date = datetime.date.today()
        last_service_date = current_date.replace(year=2000)
        battery = NubbinBattery(last_service_date,current_date)
        self.assertTrue(battery.needs_service())  # add assertion here

    def test_dont_service(self):
        current_date = datetime.date.today()
        last_service_date = current_date.replace(year=2000)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
