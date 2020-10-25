from AvailableMoves import AvailableMoves
from Board import Board
from Const import ROWS, COLS, TOOLBAR_START, WHITE, BLACK, BLACK_WON, WHITE_WON


class Checkers(Board):

    def __init__(self, win):
        super().__init__(win)
        self.turn = "white"
        self.legal_moves = []

    def game_over(self):
        if self.whitePeaces == 0:
            return "black"
        if self.blackPeaces == 0:
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
            pass


    def check_if_peace_there(self, col, row):
        return str(self.board[row][col]) == self.turn

    def check_available_moves(self, col, row):
        if self.turn == "black":
            self.check_available_moves_black(col, row)
        if self.turn == "white":
            self.check_available_moves_white(col, row)

    def check_available_moves_black(self, col, row):
        self.legal_moves = []
        if row < 7 and col < 7 and self.board[row + 1][col + 1] is None:
            self.legal_moves.append(AvailableMoves(row + 1, col + 1, self.win, col, row, False))
        elif row < 6 and col < 6 and str(self.board[row + 1][col + 1]) == "white":
            if row < 6 and col < 6 and self.board[row + 2][col + 2] is None:
                self.legal_moves.append(AvailableMoves(row + 2, col + 2, self.win, col, row, True))

        if row < 7 and col > 0 and self.board[row + 1][col - 1] is None:
            self.legal_moves.append(AvailableMoves(row + 1, col - 1, self.win, col, row, False))
        elif row < 6 and col > 1 and str(self.board[row + 1][col - 1]) == "white":
            if row < 6 and col > 1 and self.board[row + 2][col - 2] is None:
                self.legal_moves.append(AvailableMoves(row + 2, col - 2, self.win, col, row, True))

        if self.board[row][col].get_if_king():
            if row > 0 and col < 7 and self.board[row - 1][col + 1] is None:
                self.legal_moves.append(AvailableMoves(row - 1, col + 1, self.win, col, row, False))
            elif row > 1 and col < 6 and str(self.board[row - 1][col + 1]) == "white":
                if row > 1 and col < 6 and self.board[row - 2][col + 2] is None:
                    self.legal_moves.append(AvailableMoves(row - 2, col + 2, self.win, col, row, True))

            if row > 0 and col > 0 and self.board[row - 1][col - 1] is None:
                self.legal_moves.append(AvailableMoves(row - 1, col - 1, self.win, col, row, False))
            elif row > 1 and col > 1 and str(self.board[row - 1][col - 1]) == "white":
                if row > 1 and col > 1 and self.board[row - 2][col - 2] is None:
                    self.legal_moves.append(AvailableMoves(row - 2, col - 2, self.win, col, row, True))

    def check_available_moves_white(self, col, row):
        self.legal_moves = []

        if row > 0 and col < 7 and self.board[row - 1][col + 1] is None:
            self.legal_moves.append(AvailableMoves(row - 1, col + 1, self.win, col, row, False))
        elif row > 1 and col < 6 and str(self.board[row - 1][col + 1]) == "black":
            if row > 1 and col < 6 and self.board[row - 2][col + 2] is None:
                self.legal_moves.append(AvailableMoves(row - 2, col + 2, self.win, col, row, True))

        if row > 0 and col > 0 and self.board[row - 1][col - 1] is None:
            self.legal_moves.append(AvailableMoves(row - 1, col - 1, self.win, col, row, False))
        elif row > 1 and col > 1 and str(self.board[row - 1][col - 1]) == "black":
            if row > 1 and col > 1 and self.board[row - 2][col - 2] is None:
                self.legal_moves.append(AvailableMoves(row - 2, col - 2, self.win, col, row, True))

        if self.board[row][col].get_if_king():
            if row < 7 and col < 7 and self.board[row + 1][col + 1] is None:
                self.legal_moves.append(AvailableMoves(row + 1, col + 1, self.win, col, row, False))
            elif row < 6 and col < 6 and str(self.board[row + 1][col + 1]) == "black":
                if row < 6 and col < 6 and self.board[row + 2][col + 2] is None:
                    self.legal_moves.append(AvailableMoves(row + 2, col + 2, self.win, col, row, True))

            if row < 7 and col > 0 and self.board[row + 1][col - 1] is None:
                self.legal_moves.append(AvailableMoves(row + 1, col - 1, self.win, col, row, False))
            elif row < 6 and col > 1 and str(self.board[row + 1][col - 1]) == "black":
                if row < 6 and col > 1 and self.board[row + 2][col - 2] is None:
                    self.legal_moves.append(AvailableMoves(row + 2, col - 2, self.win, col, row, True))

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
