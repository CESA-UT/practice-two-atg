import pygame

from settings import WIDTH, HEIGHT, FPS, TITLE
from plants.peashooter import Peashooter
from zombies.normal_zombie import NormalZombie
from systems.collision import Collision


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()
        self.running = True

        self.plants = [Peashooter(150, 300)]
        self.zombies = [NormalZombie(750, 300)]
        self.projectiles = []

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        for plant in self.plants:
            plant.update()

            projectile = plant.shoot(self.zombies)
            if projectile is not None:
                self.projectiles.append(projectile)

        for zombie in self.zombies:
            attacking = False

            for plant in self.plants:
                if Collision.zombie_plant(zombie, plant):
                    zombie.attack(plant)
                    attacking = True
                    break

            if not attacking:
                zombie.move()

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

        pygame.display.update()