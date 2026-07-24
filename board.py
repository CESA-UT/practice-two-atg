from cell import Cell

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        # ساخت جدول دو بعدی از سلول‌ها
        self.grid = [[Cell(i, j) for j in range(cols)] for i in range(rows)]

    def display_board(self):
        print("=== GAME BOARD ===")
        for row in self.grid:
            row_str = ""
            for cell in row:
                # استفاده از متد is_empty یا بررسی مستقیم self.plant برای نمایش وضعیت
                status = "." if cell.is_empty() else "P"
                row_str += f"[{status}] "
            print(row_str)
