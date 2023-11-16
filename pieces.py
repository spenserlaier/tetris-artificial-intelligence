import random
piece_generator_functions = list()

class Piece:
    def __init__(self, coordinates, piece_type, rotation, anchor_point):
        self.coordinates = coordinates
        self.piece_type = piece_type
        self.rotation = rotation
        self.anchor_point = anchor_point
    def rotate_around(self, anchor_point, current_point):
        translated_point = (current_point[0] - anchor_point[0], current_point[1] - anchor_point[1])
        rotated_point = (-translated_point[1], translated_point[0])
        final_point = (rotated_point[0] + anchor_point[0], rotated_point[1] + anchor_point[1])
        return final_point
    def rotate_all(self, old_coordinates, anchor_point):
        new_coordinates = set()
        for point in old_coordinates:
            new_coordinates.add(self.rotate_around(anchor_point, point))
    def check_valid_coordinates(self, new_coordinates, occupied_coordinates, max_rows, max_cols):
        for point in new_coordinates:
            row_in_range = 0 <= point[0] < max_rows
            col_in_range = 0 <= point[1] < max_cols
            not_occupied = point not in occupied_coordinates
            valid_coord = row_in_range and col_in_range and not_occupied
            if not valid_coord:
                return False
        return True
    def rotate_self(self, occupied_coordinates, max_rows, max_cols):
        # all shapes except stick have a straightforward anchor point where
        # the rotate_around function can be applied
        new_coordinates = self.rotate_all(self.coordinates, self.anchor_point)
        if self.piece_type == "box":
            return
        if self.check_valid_coordinates(new_coordinates, occupied_coordinates, max_rows, max_cols):
            self.coordinates = new_coordinates
    def move_self(self, new_coordinates, new_anchor_point):
        self.coordinates = new_coordinates
        self.anchor_point = new_anchor_point

def generate_regular_l(starting_row, starting_col):
    positions = set()
    positions.add((starting_row, starting_col))
    positions.add((starting_row + 1, starting_col))
    positions.add((starting_row + 2, starting_col))
    positions.add((starting_row +2, starting_col + 1))


    anchor_point = (starting_row+1, starting_col)
    piece = Piece(positions, "regular_l", 0, anchor_point)
    return piece


def generate_reversed_l(starting_row, starting_col):
    positions = set()
    positions.add((starting_row, starting_col))
    positions.add((starting_row + 1, starting_col))
    positions.add((starting_row + 2, starting_col))
    positions.add((starting_row +2, starting_col - 1))

    anchor_point = (starting_row+1, starting_col)
    piece =  Piece(positions, "regular_l", 0, anchor_point)
    return piece

def generate_stick(starting_row, starting_col):
    positions = set()
    positions.add((starting_row, starting_col))
    positions.add((starting_row + 1, starting_col ))
    positions.add((starting_row + 2, starting_col ))
    positions.add((starting_row + 3, starting_col ))

    anchor_point = (starting_row+1.5, starting_col+0.5)
    piece =  Piece(positions, "reversed_l", 0, anchor_point)
    return piece


def generate_box(starting_row, starting_col):
    positions = set()
    positions.add((starting_row, starting_col))
    positions.add((starting_row, starting_col + 1))
    positions.add((starting_row+1, starting_col))
    positions.add((starting_row+1, starting_col+ 1))
    
    anchor_point = None
    piece =  Piece(positions, "box", 0, anchor_point)
    return piece

def generate_s(starting_row, starting_col):
    positions = set()
    positions.add((starting_row, starting_col))
    positions.add((starting_row, starting_col + 1))
    positions.add((starting_row+1, starting_col))
    positions.add((starting_row+1, starting_col-1))

    anchor_point = (starting_row+1, starting_col)
    piece =  Piece(positions, "box", 0, anchor_point)
    return piece

def generate_z(starting_row, starting_col):
    positions = set()
    positions.add((starting_row, starting_col))
    positions.add((starting_row, starting_col -1))
    positions.add((starting_row + 1, starting_col))
    positions.add((starting_row+1, starting_col+1))

    anchor_point = (starting_row+1, starting_col)
    piece =  Piece(positions, "box", 0, anchor_point)
    return piece


def generate_t(starting_row, starting_col):
    positions = set()
    positions.add((starting_row, starting_col))
    positions.add((starting_row, starting_col -1))
    positions.add((starting_row, starting_col + 1))
    positions.add((starting_row + 1, starting_col))

    anchor_point = (starting_row, starting_col)
    piece =  Piece(positions, "box", 0, anchor_point)
    #return positions
    return piece

def detect_collision(piece_coordinates, board_height_at_col):
    for piece_row, piece_col in piece_coordinates:
        if board_height_at_col[piece_col] == piece_row + 1:
            print(piece_coordinates, board_height_at_col[piece_col])
            return True
    return False

def detect_overlap(piece_coordinates, board_height_at_col):
    for piece_row, piece_col in piece_coordinates:
        if board_height_at_col[piece_col] == piece_row:
            print(piece_coordinates, board_height_at_col[piece_col])
            return True
    return False

# TODO: remember rows and cols, not x and y

def move_down(piece_coordinates):
    new_coordinates = set()
    for piece_row, piece_col in piece_coordinates:
        new_coordinates.add((piece_row + 1, piece_col))
    return new_coordinates

def move_right(piece_coordinates):
    new_coordinates = set()
    for piece_row, piece_col in piece_coordinates:
        new_coordinates.add((piece_row, piece_col+1))
    return new_coordinates

def move_left(piece_coordinates):
    new_coordinates = set()
    for piece_row, piece_col in piece_coordinates:
        new_coordinates.add((piece_row, piece_col-1))
    return new_coordinates

def check_valid_move(piece_coordinates, occupied_coordinates):
    for piece_coords in piece_coordinates:
        if piece_coords in occupied_coordinates:
            return False
    return True


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

