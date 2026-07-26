class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.plant = None  # در ابتدا هیچ گیاهی در این خانه نیست

    def is_empty(self):
        return self.plant is None

    def place_plant(self, plant):
        if self.is_empty():
            self.plant = plant
            return True
        return False

    def remove_plant(self):
        self.plant = None