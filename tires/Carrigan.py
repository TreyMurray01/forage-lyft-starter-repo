from .tires import Tire

class CarriganTire(Tire):

    def __init__(self, states_of_tires):
        self.state_of_tires = states_of_tires

    def needs_service(self):
        for state in self.state_of_tires:
            if state >= 0.9:
                return True
        return False
