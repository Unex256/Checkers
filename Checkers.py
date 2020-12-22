from AvailableMoves import AvailableMoves
from Board import Board
from Const import ROWS, COLS, TOOLBAR_START, WHITE, BLACK, BLACK_WON, WHITE_WON


class Checkers(Board):

    def __init__(self, win):
        super().__init__(win)
        self.turn = "white"
        self.legal_moves = []

    def game_over(self):
        if self.whitePeaces < 1:
            return "black"
        if self.blackPeaces < 1:
            return "white"

    def change_turn(self):
        if self.turn == "black":
            self.turn = "white"
        else:
            self.turn = "black"

    def check_move(self, col, row):

        breakcheck = False

        if len(self.legal_moves) > 0 and self.check_if_used_legal_move(col, row):
            self.board[row][col] = self.board[self.legal_moves[0].get_peace_row()][self.legal_moves[0].get_peace_col()]

            if self.turn == "black" and row == 7:
                self.board[row][col].set_king()
            elif self.turn == "white" and row == 0:
                self.board[row][col].set_king()

            self.board[self.legal_moves[0].get_peace_row()][self.legal_moves[0].get_peace_col()] = None

            for move in self.legal_moves:
                if move.get_col_row() == (col, row):
                    if move.takedown:
                        if self.turn == "white":
                            self.blackPeaces -= 1
                        else:
                            self.whitePeaces -= 1

                        row_remove = (int(move.row) + int(move.peace_row)) // 2
                        col_remove = (int(move.col) + int(move.peace_col)) // 2
                        self.board[row_remove][col_remove] = None
                        self.legal_moves = []
                        self.check_available_moves(col, row)
                        for move in self.legal_moves:
                            if move.takedown:
                                breakcheck = True

            if not breakcheck:
                self.change_turn()
            self.legal_moves = []

        elif self.check_if_peace_there(col, row):
            self.check_available_moves(col, row)
        else:
            return False

    def check_if_peace_there(self, col, row):
        try:
            return str(self.board[row][col]) == self.turn
        except IndexError:
            return False

    def check_available_moves(self, col, row):
        if self.turn == "black":
            self.check_available_moves_black(col, row)
        if self.turn == "white":
            self.check_available_moves_white(col, row)

    def check_available_moves_black(self, col, row):
        self.legal_moves = []
        diagonals = self.get_diagonal_tuple_black(row, col)
        self.add_available_moves(diagonals, row, col)

    def check_available_moves_white(self, col, row):
        self.legal_moves = []
        diagonals = self.get_diagonal_tuple_white(row, col)
        self.add_available_moves(diagonals, row, col)

    def check_if_used_legal_move(self, col, row):
        for move in self.legal_moves:
            if move.get_col_row() == (col, row):
                return True
        return False

    def update_board(self):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] is not None and str(self.board[row][col]) == "black":
                    self.board[row][col].draw_black_peace(col, row, self.win)
                elif self.board[row][col] is not None and str(self.board[row][col]) == "white":
                    self.board[row][col].draw_white_peace(col, row, self.win)

    def update_legal_moves(self):
        for move in self.legal_moves:
            move.draw_legal_move()

    def draw_winner_black(self):
        self.win.blit(BLACK_WON, (0, 0))

    def draw_winner_white(self):
        self.win.blit(WHITE_WON, (0, 0))

    def draw_turn(self):
        if self.turn == "white":
            self.win.blit(WHITE, (0, TOOLBAR_START))
        else:
            self.win.blit(BLACK, (0, TOOLBAR_START))

    @staticmethod
    def diagonal_finder(row, col, diagonal, distance):
        if diagonal == 1:
            row = row - distance
            col = col - distance
            return row, col
        elif diagonal == 2:
            row = row - distance
            col = col + distance
            return row, col
        elif diagonal == 3:
            row = row + distance
            col = col + distance
            return row, col
        else:
            row = row + distance
            col = col - distance
            return row, col

    def is_empty(self, row, col, diagonal):
        row, col = self.diagonal_finder(row, col, diagonal, 1)
        try:
            if self.board[row][col] is None:
                return True
            else:
                return False
        except IndexError:
            return False


    def is_empty_attack(self, row, col, diagonal):
        row, col = self.diagonal_finder(row, col, diagonal, 2)
        try:
            if self.board[row][col] is None:
                return True
            else:
                return False
        except IndexError:
            return False

    def get_pos_color(self, row, col):
        return str(self.board[row][col])

    def get_diagonal_tuple_white(self, row, col):
        if self.board[row][col].get_if_king():
            return tuple(range(1, 5))
        else:
            return tuple(range(1, 3))

    def get_diagonal_tuple_black(self, row, col):
        if self.board[row][col].get_if_king():
            return tuple(range(1, 5))
        else:
            return tuple(range(3, 5))

    def add_available_moves(self, diagonals, row, col):
        info_true = (self.win, col, row, True)
        info_false = (self.win, col, row, False)
        for diagonal in diagonals:
            if self.is_empty(row, col, diagonal):
                self.legal_moves.append(AvailableMoves(*self.diagonal_finder(row, col, diagonal, 1), *info_false))
            elif self.can_attack(row, col, diagonal):
                self.legal_moves.append(AvailableMoves(*self.diagonal_finder(row, col, diagonal, 2), *info_true))

    def get_opponent_color(self):
        if self.turn == "black":
            return "white"
        else:
            return "black"

    def can_attack(self, row, col, diagonal):
        if self.is_empty_attack(row, col, diagonal) and self.enemy_is_close(row, col, diagonal):
            return True
        else:
            return False

    def enemy_is_close(self, row, col, diagonal):
        if self.get_pos_color(*self.diagonal_finder(row, col, diagonal, 1)) == self.get_opponent_color():
            return True
        else:
            return False
