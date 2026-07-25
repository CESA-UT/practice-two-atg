import pygame


class Zombie:
    def __init__(self, x, y, row, health, speed, damage):
        self.x = x
        self.y = y
        self.row = row
        self.health = health
        self.speed = speed
        self.damage = damage
        self.alive = True

        self.radius = 30
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

        self.attack_cooldown = 0
        self.attack_speed = 1.0

    def move(self):
        self.x -= self.speed
        self.rect.centerx = int(self.x)

    def attack(self, plant, dt):
        self.attack_cooldown += dt
        if self.attack_cooldown >= self.attack_speed:
            plant.take_damage(self.damage)
            self.attack_cooldown = 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.destroy()

    def destroy(self):
        self.alive = False

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (150, 0, 0),
            (int(self.x), int(self.y)),
            self.radius
        )