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

NEXT_PIECE_STARTING_X = SCREEN_WIDTH - (BOARD_SQUARE_SIZE*8) #the next piece display will be a 5x5 grid
NEXT_PIECE_STARTING_Y = 10 #the next piece display will be a 5x5 grid
NEXT_PIECE_CARTESIAN_COORDINATES = board_logic.init_next_piece_display()
NEXT_PIECE_PIXEL_COORDINATES = board_logic.generate_board_square_positions(
                                                            NEXT_PIECE_CARTESIAN_COORDINATES,
                                                            NEXT_PIECE_STARTING_X,
                                                            NEXT_PIECE_STARTING_Y,
                                                            BOARD_SQUARE_SIZE)
NEXT_PIECE_ORIGIN_ROW = 0
NEXT_PIECE_ORIGIN_COL = 2

PIECE_GENERATOR_FUNCTIONS = pieces.piece_generator_functions

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#random_piece_func = random.choice(PIECE_GENERATOR_FUNCTIONS)
#piece_cartesian_coordinates = random_piece_func(BOARD_PIECE_STARTING_X, BOARD_PIECE_STARTING_Y)
GAME_TIMER = pygame.USEREVENT + 1
pygame.time.set_timer(GAME_TIMER, 1000)  # 1000 milliseconds = 1 second

occupied_coordinates = set()
colors_at_coordinates = dict()

#TODO: colors are causing bugs. when we update positions during a row clear,
# we also need to update the colors for those positions or else we'll end Up
#with a keynotfound error

def draw_board(piece, occupied_coordinates):
    piece_coordinates = piece.coordinates
    for row in range(len(BOARD_CARTESIAN_COORDINATES)):
        for col in range(len(BOARD_CARTESIAN_COORDINATES[0])):
            pixel_row, pixel_col = BOARD_PIXEL_COORDINATES[row][col]
            if (row, col) in piece_coordinates:
                pixel_color = piece_color

                pygame.draw.rect(screen, 
                                 pixel_color,
                                 (pixel_row, pixel_col, BOARD_SQUARE_SIZE-1, BOARD_SQUARE_SIZE-1))
            elif (row, col) in occupied_coordinates:
                pixel_color = colors_at_coordinates[(row, col)]
                pygame.draw.rect(screen, 
                                 pixel_color,
                                 (pixel_row, pixel_col, BOARD_SQUARE_SIZE-1, BOARD_SQUARE_SIZE-1))
            else:
                pygame.draw.rect(screen, 
                                 colors.black, 
                                 (pixel_row, pixel_col, BOARD_SQUARE_SIZE-1, BOARD_SQUARE_SIZE-1))
    pygame.display.flip()
    pygame.time.Clock().tick(60)

def draw_next_piece(piece, piece_color):
    adjusted_coordinates = set()
    if piece.piece_type == "regular_l":
        adjusted_coordinates = pieces.generate_regular_l(NEXT_PIECE_ORIGIN_ROW, 
                                                         NEXT_PIECE_ORIGIN_COL).coordinates
    if piece.piece_type == "reversed_l":
        adjusted_coordinates = pieces.generate_reversed_l(NEXT_PIECE_ORIGIN_ROW, 
                                                          NEXT_PIECE_ORIGIN_COL).coordinates
    if piece.piece_type == "box":
        adjusted_coordinates = pieces.generate_box(NEXT_PIECE_ORIGIN_ROW, 
                                                   NEXT_PIECE_ORIGIN_COL).coordinates
    if piece.piece_type == "stick":
        adjusted_coordinates = pieces.generate_stick(NEXT_PIECE_ORIGIN_ROW, 
                                                     NEXT_PIECE_ORIGIN_COL).coordinates
    if piece.piece_type == "s":
        adjusted_coordinates = pieces.generate_s(NEXT_PIECE_ORIGIN_ROW, 
                                                 NEXT_PIECE_ORIGIN_COL).coordinates
    if piece.piece_type == "z":
        adjusted_coordinates = pieces.generate_z(NEXT_PIECE_ORIGIN_ROW, 
                                                 NEXT_PIECE_ORIGIN_COL).coordinates
    if piece.piece_type == "t":
        adjusted_coordinates = pieces.generate_t(NEXT_PIECE_ORIGIN_ROW, 
                                                 NEXT_PIECE_ORIGIN_COL).coordinates
    for row in range(len(NEXT_PIECE_CARTESIAN_COORDINATES)):
        for col in range(len(NEXT_PIECE_CARTESIAN_COORDINATES[0])):
            pixel_row, pixel_col = NEXT_PIECE_PIXEL_COORDINATES[row][col]
            if (row, col) in adjusted_coordinates:
                pygame.draw.rect(screen,
                                 piece_color,
                                 (pixel_row, pixel_col, BOARD_SQUARE_SIZE-1, BOARD_SQUARE_SIZE-1))

            else:
                pygame.draw.rect(screen,
                                 colors.black,
                                 (pixel_row, pixel_col, BOARD_SQUARE_SIZE-1, BOARD_SQUARE_SIZE-1))

current_piece = pieces.generate_random_piece(BOARD_PIECE_STARTING_X, BOARD_PIECE_STARTING_Y)
next_piece = pieces.generate_random_piece(BOARD_PIECE_STARTING_X, BOARD_PIECE_STARTING_Y)
piece_color = colors.get_random_piece_color()
next_piece_color = colors.get_random_piece_color()


print(NEXT_PIECE_CARTESIAN_COORDINATES)
print(NEXT_PIECE_PIXEL_COORDINATES)





score = 0
while True:
    #break
    screen.fill(colors.gray)
    occupied_coordinates, colors_at_coordinates, added_score = board_logic.clear_rows(occupied_coordinates, 
                                                               BOARD_ROWS, 
                                                               BOARD_COLS, 
                                                               colors_at_coordinates)
    score += added_score
    draw_next_piece(next_piece, next_piece_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == GAME_TIMER:
            #print(occupied_coordinates)
            board_column_heights = board_logic.get_column_heights(BOARD_ROWS, occupied_coordinates)
            if pieces.detect_overlap(current_piece.coordinates, board_column_heights):
                print("game over")
                pygame.quit()
            if pieces.detect_collision(current_piece.coordinates, occupied_coordinates, BOARD_ROWS):
                print("collision detected")
                for piece_coords in current_piece.coordinates:
                    occupied_coordinates.add(piece_coords)
                    colors_at_coordinates[piece_coords] = piece_color
                #current_piece = pieces.generate_random_piece(BOARD_PIECE_STARTING_X, BOARD_PIECE_STARTING_Y)
                current_piece = next_piece
                piece_color = next_piece_color
                next_piece = pieces.generate_random_piece(BOARD_PIECE_STARTING_X, BOARD_PIECE_STARTING_Y)
                next_piece_color = colors.get_random_piece_color()
            else:
                current_piece.move_self("down", occupied_coordinates, BOARD_ROWS, BOARD_COLS)
        elif event.type == pygame.KEYDOWN:
            # Check for keypresses
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                current_piece.rotate_self(occupied_coordinates, BOARD_ROWS, BOARD_COLS)
                draw_board(current_piece, occupied_coordinates)
                print("Up key pressed")
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                current_piece.move_self("down", occupied_coordinates, BOARD_ROWS, BOARD_COLS)
                draw_board(current_piece, occupied_coordinates)
                print("Down key pressed")
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                print("Left key pressed")
                current_piece.move_self("left", occupied_coordinates, BOARD_ROWS, BOARD_COLS)
                draw_board(current_piece, occupied_coordinates)
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                current_piece.move_self("right", occupied_coordinates, BOARD_ROWS, BOARD_COLS)
                draw_board(current_piece, occupied_coordinates)
                print("Right key pressed")
    #board_column_heights = board_logic.get_column_heights(BOARD_ROWS, occupied_coordinates)
    #if pieces.detect_collision(current_piece.coordinates, board_column_heights):
    if pieces.detect_collision(current_piece.coordinates, occupied_coordinates, BOARD_ROWS):
        for piece_coords in current_piece.coordinates:
            occupied_coordinates.add(piece_coords)
            colors_at_coordinates[piece_coords] = piece_color
        current_piece = next_piece
        piece_color = next_piece_color
        next_piece = pieces.generate_random_piece(BOARD_PIECE_STARTING_X, BOARD_PIECE_STARTING_Y)
        next_piece_color = colors.get_random_piece_color()
        continue

    piece_pixel_coordinates = {BOARD_PIXEL_COORDINATES[p[0]][p[1]]
                               for p in current_piece.coordinates}
    #print(BOARD_CARTESIAN_COORDINATES)
    draw_board(current_piece, occupied_coordinates)






