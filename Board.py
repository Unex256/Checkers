from Const import ROWS, COLS
from BlackPeace import BlackPeace
from WhitePeace import WhitePeace



class Board:
    def __init__(self, win):
        self.win = win
        self.board = []
        self.whitePeaces = 12
        self.blackPeaces = 12
        self.check = False
        self.draw_black_peaces(win)
        self.add_white_space()
        self.draw_white_peaces(win)

    def draw_black_peaces(self, win):
        for row in range(3):
            self.board.append([])
            if self.check == False:
                self.check = True
            else:
                self.check = False
            for col in range(COLS):
                self.board[row].append(None)
                if self.check:
                    self.board[row][col] = BlackPeace(col, row, win)
                    self.check = False
                else:
                    self.check = True

    def add_white_space(self):
        for row in range(3, 5):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(None)

    def draw_white_peaces(self, win):
        for row in range(5, 8):
            self.board.append([])
            if self.check == False:
                self.check = True
            else:
                self.check = False
            for col in range(COLS):
                self.board[row].append(None)
                if self.check:
                    self.board[row][col] = WhitePeace(col, row, win)
                    self.check = False
                else:
                    self.check = True
