import pygame
from entities.plant import Plant


class Sunflower(Plant):
    def __init__(self, x, y, row=None):
        super().__init__(x, y, 80)
        self.row = row
        self.sun_timer = 0
        self.sun_cooldown = 300
        self.sun_amount = 25

    def update(self):
        self.sun_timer += 1

    def generate_sun(self):
        if self.sun_timer >= self.sun_cooldown:
            self.sun_timer = 0
            return self.sun_amount
        return 0

    def draw(self, surface):
        # رسم دایره زرد برای آفتابگردان
        pygame.draw.circle(surface, (255, 255, 0), (int(self.x), int(self.y)), 25)
        # حاشیه زرد تیره‌تر برای نمای بهتر
        pygame.draw.circle(surface, (210, 180, 0), (int(self.x), int(self.y)), 25, 2)