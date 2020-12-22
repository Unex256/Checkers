from unittest import TestCase
from Checkers import Checkers
from Const import WIN, BOARD

class TestCheckers(TestCase):
    def test_game_over(self):
        WIN.blit(BOARD, (0, 0))
        checkers_test = Checkers(WIN)
        checkers_test.whitePeaces = 0
        self.assertEqual(checkers_test.game_over(), "black")
        checkers_test.whitePeaces = 2
        checkers_test.blackPeaces = 0
        self.assertEqual(checkers_test.game_over(), "white")

    def test_change_turn(self):
        WIN.blit(BOARD, (0, 0))
        checkers_test = Checkers(WIN)
        if checkers_test.turn == "black":
            checkers_test.change_turn()
            self.assertEqual(checkers_test.turn, "white")
        else:
            checkers_test.change_turn()
            self.assertEqual(checkers_test.turn, "black")

    def test_check_move(self):
        WIN.blit(BOARD, (0, 0))
        checkers_test = Checkers(WIN)
        self.assertFalse(checkers_test.check_move(1, 1))

    def test_check_if_peace_there(self):
        WIN.blit(BOARD, (0, 0))
        checkers_test = Checkers(WIN)
        self.assertFalse(checkers_test.check_if_peace_there(1, 1))

    def test_check_if_used_legal_move(self):
        WIN.blit(BOARD, (0, 0))
        checkers_test = Checkers(WIN)
        self.assertFalse(checkers_test.check_if_used_legal_move(1, 1))

    def test_diagonal_finder(self):
        WIN.blit(BOARD, (0, 0))
        checkers_test = Checkers(WIN)
        self.assertEqual(checkers_test.diagonal_finder(1, 1, 1, 1), (0, 0))
        self.assertEqual(checkers_test.diagonal_finder(1, 1, 2, 1), (0, 2))
        self.assertEqual(checkers_test.diagonal_finder(1, 1, 3, 1), (2, 2))
        self.assertEqual(checkers_test.diagonal_finder(1, 1, 4, 1), (2, 0))

    def test_get_diagonal_tuple_white(self):
        WIN.blit(BOARD, (0, 0))
        checkers_test = Checkers(WIN)
        self.assertEqual(checkers_test.get_diagonal_tuple_white(5, 5), tuple(range(1, 3)))

    def test_get_diagonal_tuple_black(self):
        WIN.blit(BOARD, (0, 0))
        checkers_test = Checkers(WIN)
        self.assertEqual(checkers_test.get_diagonal_tuple_black(5, 5), tuple(range(3, 5)))

