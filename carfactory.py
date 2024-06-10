from battery import SpindlerBattery, NubbinBattery
from engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from car import Car


class CarFactory:
    @staticmethod
    def create_calliope(self, last_service_date, current_date, last_service_milage, current_milage):
        new_battery = SpindlerBattery(current_date, last_service_date)
        new_engine = CapuletEngine(current_milage, last_service_milage)
        return Car(engine=new_engine, battery=new_battery)

    @staticmethod
    def create_glissade(self, last_service_date, current_date, last_service_milage, current_milage):
        new_battery = SpindlerBattery(current_date=current_date, last_service_date=last_service_date)
        new_engine = WilloughbyEngine(current_milage, last_service_milage)
        return Car(engine=new_engine, battery=new_battery)

    @staticmethod
    def create_palindrome(self, last_service_date, current_date, warning_light_is_on):
        new_battery = SpindlerBattery(current_date=current_date, last_service_date=last_service_date)
        new_engine = SternmanEngine(warning_light_is_on)
        return Car(engine=new_engine, battery=new_battery)

    @staticmethod
    def create_roschache(self, last_service_date, current_date, last_service_milage, current_milage):
        new_battery = NubbinBattery(current_date=current_date, last_service_date=last_service_date)
        new_engine = WilloughbyEngine(current_milage, last_service_milage)
        return Car(engine=new_engine, battery=new_battery)
    @staticmethod
    def create_thovex(last_service_date, current_date, last_service_milage, current_milage):
        new_battery = NubbinBattery(current_date=current_date, last_service_date=last_service_date)
        new_engine = CapuletEngine(current_milage, last_service_milage)
        return Car(engine=new_engine, new_battery=new_battery)