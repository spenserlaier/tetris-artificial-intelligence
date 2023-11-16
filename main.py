import pygame
import sys
import tetris


def generate_board_square_positions(board, starting_x, starting_y, square_size):
    curr_x, curr_y = starting_x, starting_y
    rec_positions = []
    for row in board:
        curr_y += 10
        curr_x = starting_x
        curr_row = list()
        for col in row:
            curr_x += 10
            curr_row.append((curr_x, curr_y))
        rec_positions.append(curr_row)
    return rec_positions


pygame.init()
width, height = 400, 400
screen = pygame.display.set_mode((width, height))

box_width, box_height = 50, 50
box_x, box_y = (width - box_width) // 2, (height - box_height) // 2
red = (255, 0, 0)

board = tetris.init_board(20, 10)
positions = generate_board_square_positions(board, 10, 10, square_size=10)
for row in positions:
    for col in row:
        print(col)
for row in board:
    print(row)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    square_size = 10
    positions = generate_board_square_positions(board, 10, 10, square_size)
    for pos_row in positions:
        for pos in pos_row:
            pygame.draw.rect(screen, red, (pos[0], pos[1], square_size-1, square_size-1))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)

