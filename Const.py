import pygame
from pygame import image

pygame.init()

WIDTH, HEIGHT = 512, 512
TOOLBAR_HEIGHT = 63
ROWS, COLS = 8, 8
TILE_SIZE = WIDTH // COLS
TOOLBAR_START = HEIGHT

WHITE = pygame.transform.scale(image.load("white.png"), (TILE_SIZE, TILE_SIZE))
WHITE_KING = pygame.transform.scale(image.load("white_king.png"), (TILE_SIZE, TILE_SIZE))
BLACK = pygame.transform.scale(image.load("black.png"), (TILE_SIZE, TILE_SIZE))
BLACK_KING = pygame.transform.scale(image.load("black_king.png"), (TILE_SIZE, TILE_SIZE))
BOARD = pygame.transform.scale(image.load("board.png"), (WIDTH, HEIGHT))
LEGAL_MOVE = pygame.transform.scale(image.load("legal_move.png"), (TILE_SIZE, TILE_SIZE))
BLACK_WON = pygame.transform.scale(image.load("black_is_the_winner.png"), (WIDTH, HEIGHT))
WHITE_WON = pygame.transform.scale(image.load("white_is_the_winner.png"), (WIDTH, HEIGHT))

WIN = pygame.display.set_mode((WIDTH, HEIGHT + TOOLBAR_HEIGHT))
pygame.display.set_icon(BOARD)
pygame.display.set_caption('Checkers')

FPS = 60
