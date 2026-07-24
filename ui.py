class SunSystem:
    def __init__(self, initial_suns=50):
        self.suns = initial_suns

    def add_sun(self, amount=25):
        self.suns += amount

    def spend_sun(self, amount):
        if self.suns >= amount:
            self.suns -= amount
            return True
        return False

    def get_suns(self):
        self.suns


class PlantCard:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def can_afford(self, current_suns):
        return current_suns >= self.cost