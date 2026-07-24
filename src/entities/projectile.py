class Projectile:
    def __init__(self, x, y, speed, damage):
        self.x = x
        self.y = y
        self.speed = speed
        self.damage = damage
        self.active = True

    def move(self):
        self.x += self.speed

    def hit(self, zombie):
        zombie.take_damage(self.damage)
        self.destroy()

    def destroy(self):
        self.active = False
    def draw(self, screen):
        import pygame

        pygame.draw.circle(
            screen,
            (255, 255, 0),
            (self.x, self.y),
            6
        )