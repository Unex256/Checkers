from Const import WHITE, TILE_SIZE, WHITE_KING


class WhitePeace:
    def __init__(self, col, row, win):
        self.x = 0
        self.y = 0
        self.col = col
        self.row = row
        self.win = win
        self.king = False
        self.draw_white_peace(col, row, win)

    def draw_white_peace(self, col, row, win):
        self.find_position(col, row)
        if self.king:
            win.blit(WHITE_KING, (self.x, self.y))
        else:
            win.blit(WHITE, (self.x, self.y))

    def find_position(self, col, row):
        self.x = col * TILE_SIZE
        self.y = row * TILE_SIZE

    def get_if_king(self):
        return self.king

    def set_king(self):
        self.king = True

    def __str__(self):
        return "white"

    def __repr__(self):
        return "W"