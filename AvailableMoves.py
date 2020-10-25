from Const import TILE_SIZE, LEGAL_MOVE

class AvailableMoves():
    def __init__(self, row, col, win, peace_col, peace_row, takedown):
        self.col = col
        self.row = row
        self.peace_col = peace_col
        self.peace_row = peace_row
        self.takedown = takedown
        self.win = win
        self.draw_legal_move()

    def find_position(self, col, row):
        self.x = col * TILE_SIZE
        self.y = row * TILE_SIZE

    def draw_legal_move(self):
        self.find_position(self.col, self.row)
        self.win.blit(LEGAL_MOVE, (self.x, self.y))

    def get_col_row(self):
        return self.col, self.row

    def get_col(self):
        return self.col

    def get_row(self):
        return self.row

    def get_peace_col(self):
        return self.peace_col

    def get_peace_row(self):
        return self.peace_row

    def get_takedown(self):
        return self.takedown


