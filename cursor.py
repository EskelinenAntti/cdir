class Cursor:

    def __init__(self, rows):
        self.clear_cursor(rows)

    def move_up(self):
        self.row_index = (self.row_index - 1) % self.rows

    def move_down(self):
        self.row_index = (self.row_index + 1) % self.rows

    def clear_cursor(self, rows):
        self.row_index = 0
        self.rows = rows
