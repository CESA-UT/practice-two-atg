import pygame

from settings import WIDTH, HEIGHT, FPS, TITLE
from plants.peashooter import Peashooter
from zombies.normal_zombie import NormalZombie
from systems.collision import Collision
from systems.wave_manager import WaveManager


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()
        self.running = True

        self.row_y = [120, 200, 280, 360, 440]

        self.plants = [
            Peashooter(150, self.row_y[0], row=0),
            Peashooter(150, self.row_y[2], row=2)
        ]
        self.zombies = []
        self.projectiles = []
        self.wave_manager = WaveManager(spawn_x=WIDTH, row_y_positions=self.row_y)

        self.game_over = False
        self.game_won = False
        self.font = pygame.font.Font(None, 80)

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0
            self.handle_events()
            self.update(dt)
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self, dt):
        if self.game_over or self.game_won:
            return

        self.wave_manager.update(dt, self.zombies)

        if self.wave_manager.game_won:
            self.game_won = True
            return

        for plant in self.plants:
            plant.update()

            projectile = plant.shoot(self.zombies) if hasattr(plant, 'shoot') else None
            if projectile is not None:
                self.projectiles.append(projectile)

        for zombie in self.zombies:
            attacking = False

            for plant in self.plants:
                if Collision.zombie_plant(zombie, plant):
                    zombie.attack(plant, dt)
                    attacking = True
                    break

            if not attacking:
                zombie.move()

            if zombie.x <= 50:
                self.game_over = True
                return

        for projectile in self.projectiles:
            if not projectile.active:
                continue

            projectile.move()

            for zombie in self.zombies:
                if zombie.alive and Collision.projectile_zombie(projectile, zombie):
                    break

        self.projectiles = [p for p in self.projectiles if p.active]
        self.zombies = [z for z in self.zombies if z.alive]
        self.plants = [p for p in self.plants if p.alive]

    def draw(self):
        self.screen.fill((50, 150, 50))

        for plant in self.plants:
            plant.draw(self.screen)

        for zombie in self.zombies:
            zombie.draw(self.screen)

        for projectile in self.projectiles:
            projectile.draw(self.screen)

        if self.game_over:
            text_surface = self.font.render("GAME OVER", True, (200, 0, 0))
            text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            self.screen.blit(text_surface, text_rect)

        elif self.game_won:
            text_surface = self.font.render("YOU WIN!", True, (255, 215, 0))
            text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            self.screen.blit(text_surface, text_rect)

        pygame.display.update()