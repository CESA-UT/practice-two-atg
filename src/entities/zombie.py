class Zombie:
    def __init__(self, x, y, health, speed, damage):
        self.x = x
        self.y = y
        self.health = health
        self.speed = speed
        self.damage = damage
        self.alive = True

    def move(self):
        self.x -= self.speed

    def take_damage(self, damage):
        self.health -= damage

        if self.health <= 0:
            self.destroy()

    def attack(self, plant):
        plant.take_damage(self.damage)

    def destroy(self):
        self.alive = False
        pass
    
    def draw(self, screen):
        import pygame

        pygame.draw.circle(
            screen,
            (150, 0, 0),
            (self.x, self.y),
            30
        )