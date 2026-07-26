class Plant:
    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.health = health
        self.alive = True

    def take_damage(self, damage):
        self.health -= damage

        if self.health <= 0:
            self.destroy()

    def destroy(self):
        self.alive = False
        pass

    def draw(self, screen):
        import pygame

        pygame.draw.circle(
            screen,
            (0, 200, 0),
            (self.x, self.y),
            25
        )