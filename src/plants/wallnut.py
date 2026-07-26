from entities.plant import Plant


class WallNut(Plant):
    def __init__(self, x, y, row=None):
        super().__init__(x, y, 300)
        self.row = row

    def block(self):
        return True

    def update(self):
        pass