class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.has_plant = False  # آیا روی این خانه گیاهی کاشته شده؟

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def get_has_plant(self):
        return self.has_plant

    def set_has_plant(self, status):
        self.has_plant = status


class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        # ساخت جدول دو بعدی از سلول‌ها
        self.grid = [[Cell(i, j) for j in range(cols)] for i in range(rows)]

    def display_board_status(self):
        print(f"Board created with {self.rows} rows and {self.cols} cols.")
