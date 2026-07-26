from entities.plant import Plant
from entities.projectile import Projectile


class Peashooter(Plant):
    def __init__(self, x, y, row=None):
        super().__init__(x, y, 100)
        self.row = row
        self.shoot_cooldown = 60

    def can_shoot(self, zombies):
        for zombie in zombies:
            if zombie.alive and zombie.x > self.x:
                if self.row is not None and hasattr(zombie, 'row') and zombie.row is not None:
                    if zombie.row == self.row:
                        return True
                elif abs(zombie.y - self.y) < 35:
                    return True
        return False

    def shoot(self, zombies):
        if self.shoot_cooldown == 0 and self.can_shoot(zombies):
            self.shoot_cooldown = 60
            return Projectile(self.x, self.y, 5, 20)
        return None

    def update(self):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1