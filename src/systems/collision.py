class Collision:
    @staticmethod
    def projectile_zombie(projectile, zombie):
        if (
            abs(projectile.x - zombie.x) < 10
            and abs(projectile.y - zombie.y) < 10
        ):
            projectile.hit(zombie)
            return True

        return False


    @staticmethod
    def zombie_plant(zombie, plant):
        if (
            abs(zombie.x - plant.x) < 50
            and abs(zombie.y - plant.y) < 50
        ):
            return True

        return False