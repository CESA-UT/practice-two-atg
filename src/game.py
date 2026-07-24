import pygame

from settings import WIDTH, HEIGHT, FPS, TITLE
from plants.peashooter import Peashooter
from zombies.normal_zombie import NormalZombie
from systems.collision import Collision
from entities.projectile import Projectile



class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(
            (WIDTH, HEIGHT)
        )

        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()

        self.running = True

        
        self.plants = []

        self.plants.append(
             Peashooter(150, 300)
)
        
        self.zombies = []

        self.zombies.append(
            NormalZombie(750, 300)
)
        self.projectiles = []
        
        


    def run(self):
        while self.running:

            self.handle_events()

            self.update()

            self.draw()

            self.clock.tick(FPS)


    def handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False


    def update(self):
        for plant in self.plants:

            plant.update()

            projectile = plant.shoot()

            if projectile:
                self.projectiles.append(projectile)

        for zombie in self.zombies:

            attacking = False

            for plant in self.plants:

                if Collision.zombie_plant(zombie, plant):
                    zombie.attack(plant)
                    attacking = True

            if not attacking:
                zombie.move()

        for projectile in self.projectiles:
            projectile.move()
        for projectile in self.projectiles:
            for zombie in self.zombies:
                Collision.projectile_zombie(projectile, zombie)

        self.projectiles = [
            projectile
            for projectile in self.projectiles
            if projectile.active
]
        self.zombies = [
            zombie
            for zombie in self.zombies
            if zombie.alive
]

        self.plants = [
            plant
            for plant in self.plants
            if plant.alive
]               
        


    def draw(self):
        self.screen.fill((50, 150, 50))
        for plant in self.plants:
                plant.draw(self.screen)
        for zombie in self.zombies:
                zombie.draw(self.screen)
        for projectile in self.projectiles:
            projectile.draw(self.screen)
        pygame.display.update()
