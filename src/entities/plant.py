class Plant:
    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        print("Plant health:", self.health)

        if self.health <= 0:
            self.destroy()

    def destroy(self):
        pass

    def draw(self, screen):
        import pygame

        pygame.draw.circle(
            screen,
            (0, 200, 0),
            (self.x, self.y),
            25
        )