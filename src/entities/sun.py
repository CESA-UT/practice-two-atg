class Sun:
    def __init__(self, value=25):
        self.value = value

    def collect(self):
        return self.value


class SunManager:
    def __init__(self, initial_suns=50):
        self.suns = initial_suns

    def add_sun(self, amount):
        self.suns += amount

    def spend_sun(self, amount):
        if self.suns >= amount:
            self.suns -= amount
            return True
        return False