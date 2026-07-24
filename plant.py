class Plant:
    def __init__(self, name, health, cost):
        self.name = name
        self.health = health
        self.cost = cost

    def take_damage(self, amount):
        self.health -= amount
        return self.health <= 0  # اگر جان گیاه تمام شد، یعنی مرده است


class ShooterPlant(Plant):
    def __init__(self, name="Peashooter", health=100, cost=100, damage=20):
        super().__init__(name, health, cost)
        self.damage = damage

    def attack(self):
        return self.damage


class Sunflower(Plant):
    def __init__(self, name="Sunflower", health=80, cost=50, production_rate=25):
        super().__init__(name, health, cost)
        self.production_rate = production_rate

    def produce_sun(self):
        return self.production_rate