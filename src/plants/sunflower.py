from entities.plant import Plant


class Sunflower(Plant):
    def __init__(self, x, y, row=None):
        super().__init__(x, y, 80)
        self.row = row
        self.sun_timer = 0
        self.sun_cooldown = 300
        self.sun_amount = 25

    def update(self):
        self.sun_timer += 1

    def generate_sun(self):
        if self.sun_timer >= self.sun_cooldown:
            self.sun_timer = 0
            return self.sun_amount
        return 0