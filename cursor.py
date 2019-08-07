class Cursor:

    def __init__(self, rows, columns):
        self.clear_cursor(rows, columns)

    def move_up(self):
        self.row_index = (self.row_index - 1) % self.rows

    def move_down(self):
        self.row_index = (self.row_index + 1) % self.rows

    def move_left(self):
        self.column_index = (self.column_index - 1) % self.columns

    def move_right(self):
        self.column_index = (self.column_index + 1) % self.columns

    def clear_cursor(self, rows, columns):
        self.row_index = 0
        self.rows = rows
        self.columns = columns
        self.column_index = 0
