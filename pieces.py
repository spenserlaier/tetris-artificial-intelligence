import random
piece_generator_functions = list()


def generate_regular_l(starting_row, starting_col):
    positions = set()
    positions.add((starting_row, starting_col))
    positions.add((starting_row + 1, starting_col))
    positions.add((starting_row + 2, starting_col))
    positions.add((starting_row +2, starting_col + 1))
    return positions


def generate_reversed_l(starting_row, starting_col):
    positions = set()
    positions.add((starting_row, starting_col))
    positions.add((starting_row + 1, starting_col))
    positions.add((starting_row + 2, starting_col))
    positions.add((starting_row +2, starting_col - 1))
    return positions

def generate_stick(starting_row, starting_col):
    positions = set()
    positions.add((starting_row, starting_col))
    positions.add((starting_row + 1, starting_col ))
    positions.add((starting_row + 2, starting_col ))
    positions.add((starting_row + 3, starting_col ))
    return positions


def generate_box(starting_row, starting_col):
    positions = set()
    positions.add((starting_row, starting_col))
    positions.add((starting_row, starting_col + 1))
    positions.add((starting_row+1, starting_col))
    positions.add((starting_row+1, starting_col+ 1))
    return positions

def generate_s(starting_row, starting_col):
    positions = set()
    positions.add((starting_row, starting_col))
    positions.add((starting_row, starting_col + 1))
    positions.add((starting_row+1, starting_col))
    positions.add((starting_row+1, starting_col-1))
    return positions

def generate_z(starting_row, starting_col):
    positions = set()
    positions.add((starting_row, starting_col))
    positions.add((starting_row, starting_col -1))
    positions.add((starting_row + 1, starting_col))
    positions.add((starting_row+1, starting_col+1))
    return positions


def generate_t(starting_row, starting_col):
    positions = set()
    positions.add((starting_row, starting_col))
    positions.add((starting_row, starting_col -1))
    positions.add((starting_row, starting_col + 1))
    positions.add((starting_row + 1, starting_col))
    return positions

def detect_collision(piece_coordinates, board_height_at_col):
    for piece_row, piece_col in piece_coordinates:
        if board_height_at_col[piece_col] == piece_row + 1:
            print(piece_coordinates, board_height_at_col[piece_col])
            return True
    return False
# TODO: remember rows and cols, not x and y

def move_down(piece_coordinates):
    new_coordinates = set()
    for piece_row, piece_col in piece_coordinates:
        new_coordinates.add((piece_row + 1, piece_col))
    return new_coordinates


piece_generator_functions.append(generate_regular_l)
piece_generator_functions.append(generate_reversed_l)
piece_generator_functions.append(generate_s)
piece_generator_functions.append(generate_z)
piece_generator_functions.append(generate_stick)
piece_generator_functions.append(generate_t)
piece_generator_functions.append(generate_box)


def generate_random_piece(starting_row, starting_col):
    piece_generator = random.choice(piece_generator_functions)
    return piece_generator(starting_row, starting_col)

