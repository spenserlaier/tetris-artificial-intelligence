piece_generator_functions = list()

def generate_regular_l(starting_x, starting_y):
    positions = set()
    positions.add((starting_x, starting_y))
    positions.add((starting_x, starting_y + 1))
    positions.add((starting_x, starting_y + 2))
    positions.add((starting_x +1, starting_y + 2))
    return positions


def generate_reversed_l(starting_x, starting_y):
    positions = set()
    positions.add((starting_x, starting_y))
    positions.add((starting_x, starting_y + 1))
    positions.add((starting_x, starting_y + 2))
    positions.add((starting_x -1, starting_y + 2))
    return positions

def generate_stick(starting_x, starting_y):
    positions = set()
    positions.add((starting_x, starting_y))
    positions.add((starting_x, starting_y + 1))
    positions.add((starting_x, starting_y + 2))
    positions.add((starting_x, starting_y + 3))
    return positions


def generate_box(starting_x, starting_y):
    positions = set()
    positions.add((starting_x, starting_y))
    positions.add((starting_x, starting_y + 1))
    positions.add((starting_x+1, starting_y))
    positions.add((starting_x+1, starting_y+ 1))
    return positions

def generate_s(starting_x, starting_y):
    positions = set()
    positions.add((starting_x, starting_y))
    positions.add((starting_x+1, starting_y))
    positions.add((starting_x+1, starting_y+1))
    positions.add((starting_x+1, starting_y-1))
    return positions

def generate_z(starting_x, starting_y):
    positions = set()
    positions.add((starting_x, starting_y))
    positions.add((starting_x-1, starting_y))
    positions.add((starting_x, starting_y+1))
    positions.add((starting_x+1, starting_y+1))
    return positions


def generate_t(starting_x, starting_y):
    positions = set()
    positions.add((starting_x, starting_y))
    positions.add((starting_x-1, starting_y))
    positions.add((starting_x+1, starting_y))
    positions.add((starting_x, starting_y+1))
    return positions

piece_generator_functions.append(generate_regular_l)
piece_generator_functions.append(generate_reversed_l)
piece_generator_functions.append(generate_s)
piece_generator_functions.append(generate_z)
piece_generator_functions.append(generate_stick)
piece_generator_functions.append(generate_t)
piece_generator_functions.append(generate_box)

