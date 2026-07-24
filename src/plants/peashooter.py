from entities.plant import Plant
from entities.projectile import Projectile


class Peashooter(Plant):
    def __init__(self, x, y):
        super().__init__(x, y, 100)

        self.shoot_cooldown = 60

    def shoot(self):
        if self.shoot_cooldown == 0:

            self.shoot_cooldown = 6

            return Projectile(
                self.x,
                self.y,
                5,
                20
            )
        return None
    
    def update(self):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1