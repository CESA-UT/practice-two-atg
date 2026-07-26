import pygame


class Projectile:
    def __init__(self, x, y, speed, damage):
        self.x = x
        self.y = y
        self.speed = speed
        self.damage = damage
        self.active = True

    def move(self):
        self.x += self.speed
        if self.x > 1000:
            self.destroy()

    def hit(self, zombie):
        zombie.take_damage(self.damage)
        self.destroy()

    def destroy(self):
        self.active = False

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 0),
            (int(self.x), int(self.y)),
            6
        )