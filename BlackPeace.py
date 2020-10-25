from Const import BLACK, TILE_SIZE, BLACK_KING


class BlackPeace:
    def __init__(self, col, row, win):
        self.x = 0
        self.y = 0
        self.col = col
        self.row = row
        self.win = win
        self.king = False
        self.draw_black_peace(col, row, win)

    def draw_black_peace(self, col, row, win):
        self.find_position(col, row)
        if self.king:
            win.blit(BLACK_KING, (self.x, self.y))
        else:
            win.blit(BLACK, (self.x, self.y))

    def find_position(self, col, row):
        self.x = col * TILE_SIZE
        self.y = row * TILE_SIZE

    def set_king(self):
        self.king = True

    def get_if_king(self):
        return self.king

    def __str__(self):
        return "black"

    def __repr__(self):
        return "B"