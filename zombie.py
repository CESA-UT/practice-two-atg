class Zombie:
    def __init__(self, name="Basic Zombie", health=100, speed=1, damage=10):
        self.name = name
        self.health = health
        self.speed = speed
        self.damage = damage

    def take_damage(self, amount):
        self.health -= amount
        return self.health <= 0  # اگر جان زامبی تمام شد

    def attack_plant(self, plant):
        return plant.take_damage(self.damage)