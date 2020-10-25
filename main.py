import pygame
from Checkers import Checkers
from Const import WIN, FPS, BOARD, TILE_SIZE



def get_click_col_row(pos):
    x, y = pos
    col = x // TILE_SIZE
    row = y // TILE_SIZE

    return col, row


def main():
    clock = pygame.time.Clock()
    run = True
    WIN.blit(BOARD, (0, 0))
    checkers = Checkers(WIN)

    while run:
        clock.tick(FPS)
        if checkers.game_over() == "black":
            checkers.draw_winner_black()
        elif checkers.game_over() == "white":
            checkers.draw_winner_white()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()
                col, row = get_click_col_row(pos)
                WIN.blit(BOARD, (0, 0))
                checkers.draw_turn()
                checkers.check_move(col, row)
                checkers.update_board()
                checkers.draw_turn()

        pygame.display.update()


main()
