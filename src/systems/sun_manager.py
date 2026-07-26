import random
import pygame
from entities.sun import Sun


class SunManager:
    def __init__(self):
        self.sun_count = 150
        self.suns = []
        self.sky_timer = 0
        self.sky_cooldown = 8.0
        self.font = pygame.font.Font(None, 36)

    def update(self, dt):
        self.sky_timer += dt
        if self.sky_timer >= self.sky_cooldown:
            self.sky_timer = 0
            spawn_x = random.randint(100, 800)
            target_y = random.randint(150, 450)
            self.suns.append(Sun(spawn_x, 0, target_y=target_y, is_sky=True))

        for sun in self.suns:
            sun.update(dt)

        self.suns = [s for s in self.suns if s.alive]

    def add_sun(self, sun):
        self.suns.append(sun)

    def handle_click(self, pos):
        for sun in self.suns:
            if sun.alive and sun.is_clicked(pos):
                sun.alive = False
                self.sun_count += sun.value
                return True
        return False

    def draw(self, screen):
        for sun in self.suns:
            sun.draw(screen)

        sun_text = self.font.render(f"Sun: {self.sun_count}", True, (255, 255, 255))
        screen.blit(sun_text, (20, 20))