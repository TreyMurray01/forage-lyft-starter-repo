from .tires import Tire


class OctoprimeTire(Tire):

    def __init__(self, state_of_tires):
        self.state_of_tires = state_of_tires

    def needs_service(self):
        return sum(self.state_of_tires) >= 3
