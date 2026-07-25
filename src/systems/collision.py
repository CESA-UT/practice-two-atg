class Collision:
    @staticmethod
    def projectile_zombie(projectile, zombie):
        if (
            abs(projectile.x - zombie.x) < 20
            and abs(projectile.y - zombie.y) < 25
        ):
            projectile.hit(zombie)
            return True
        return False

    @staticmethod
    def zombie_plant(zombie, plant):
        if (
            abs(zombie.x - plant.x) < 40
            and abs(zombie.y - plant.y) < 40
        ):
            return True
        return False