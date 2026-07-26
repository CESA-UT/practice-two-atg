import pygame
from entities.plant import Plant


class WallNut(Plant):
    def __init__(self, x, y, row=None):
        super().__init__(x, y, 300)  # جان ۳۰۰ برای نقش سپری
        self.row = row

    def block(self):
        return True

    def update(self):
        pass

    def draw(self, surface):
        # رسم گردو به صورت شکل هندسی ساده (دایره قهوه‌ای)
        pygame.draw.circle(surface, (139, 69, 19), (int(self.x), int(self.y)), 25)
        pygame.draw.circle(surface, (90, 40, 10), (int(self.x), int(self.y)), 25, 2)