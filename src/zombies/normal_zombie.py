from entities.zombie import Zombie

class NormalZombie(Zombie):
    def __init__(self, x, y, row):
        super().__init__(
            x=x,
            y=y,
            row=row,
            health=100,  
            speed=1,     
            damage=20    
        )