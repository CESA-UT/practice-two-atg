import pygame

from settings import WIDTH, HEIGHT, FPS, TITLE
from plants.peashooter import Peashooter
from zombies.normal_zombie import NormalZombie



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
        pass


    def draw(self):
        self.screen.fill((50, 150, 50))
        for plant in self.plants:
                plant.draw(self.screen)
        for zombie in self.zombies:
                zombie.draw(self.screen)
        pygame.display.update()
