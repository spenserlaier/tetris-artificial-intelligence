import pygame
import sys
import pieces
import random
import colors
import board_logic


BOARD_ROWS = 20
BOARD_COLS = 10
BOARD_SQUARE_SIZE = 20
BOARD_STARTING_X = 10
BOARD_STARTING_Y = 10
BOARD_PIECE_STARTING_X = 0
BOARD_PIECE_STARTING_Y = BOARD_COLS//2
BOARD_CARTESIAN_COORDINATES = board_logic.init_board(BOARD_ROWS, BOARD_COLS)
BOARD_PIXEL_COORDINATES = board_logic.generate_board_square_positions(
                                                            BOARD_CARTESIAN_COORDINATES, 
                                                            BOARD_STARTING_X, 
                                                            BOARD_STARTING_Y, 
                                                            BOARD_SQUARE_SIZE)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

PIECE_GENERATOR_FUNCTIONS = pieces.piece_generator_functions

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#random_piece_func = random.choice(PIECE_GENERATOR_FUNCTIONS)
#piece_cartesian_coordinates = random_piece_func(BOARD_PIECE_STARTING_X, BOARD_PIECE_STARTING_Y)
piece_cartesian_coordinates = pieces.generate_random_piece(BOARD_PIECE_STARTING_X, BOARD_PIECE_STARTING_Y)
GAME_TIMER = pygame.USEREVENT + 1
pygame.time.set_timer(GAME_TIMER, 200)  # 1000 milliseconds = 1 second

occupied_coordinates = set()
colors_at_coordinates = dict()

while True:
    screen.fill(colors.gray)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == GAME_TIMER:
            print("game timer detected")
            print(occupied_coordinates)
            board_column_heights = board_logic.get_column_heights(BOARD_ROWS, occupied_coordinates)
            if pieces.detect_collision(piece_cartesian_coordinates, board_column_heights):
                print("collision detected")
                for piece_coords in piece_cartesian_coordinates:
                    occupied_coordinates.add(piece_coords)
                    colors_at_coordinates[piece_coords] = piece_color
                piece_cartesian_coordinates = pieces.generate_random_piece(BOARD_PIECE_STARTING_X, BOARD_PIECE_STARTING_Y)
            else:
                piece_cartesian_coordinates = pieces.move_down(piece_cartesian_coordinates)
    piece_pixel_coordinates = {BOARD_PIXEL_COORDINATES[p[0]][p[1]]
                               for p in piece_cartesian_coordinates}
    for row in BOARD_CARTESIAN_COORDINATES:
        for col in row:
            var = 5
    for pos_row in BOARD_PIXEL_COORDINATES:
        for pos in pos_row:
            if pos not in piece_pixel_coordinates:
                pygame.draw.rect(screen, 
                                 colors.black, 
                                 (pos[0], pos[1], BOARD_SQUARE_SIZE-1, BOARD_SQUARE_SIZE-1))

            else:
                # print("detected")
                pygame.draw.rect(screen,
                                 colors.green,
                                 (pos[0], pos[1], BOARD_SQUARE_SIZE-1, BOARD_SQUARE_SIZE-1))
    # Update the display
    pygame.display.flip()
    # Control the frame rate
    pygame.time.Clock().tick(60)

