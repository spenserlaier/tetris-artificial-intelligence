import pieces
import collections
import numpy

def get_piece_type(piece):
    out = [0 for _ in range(7)] # 7 total pieces- use one-hot encoding
    if piece.piece_type == "regular_l":
        out[0] = 1
    elif piece.piece_type == "reversed_l":
        out[1] = 1
    elif piece.piece_type == "box":
        out[2] = 1
    elif piece.piece_type == "t":
        out[3] = 1
    elif piece.piece_type == "s":
        out[4] = 1
    elif piece.piece_type == "z":
        out[5] = 1
    elif piece.piece_type == "stick":
        out[6] = 1
    return numpy.array(out)

def generate_board_array(rows, cols, occupied_coords):
    single_row = [0]*cols
    out = [single_row for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            if (row, col) in occupied_coords:
                out[row][col] = 1
    out = numpy.array(out).flatten()

    return out

def get_piece_coordinates(piece):
    out = sorted(list(piece.coordinates))
    out = numpy.array(out).flatten()
    return out

def get_normalized_piece_coordinates(piece):
    sorted_coords = sorted(list(piece.coordinates))
    # needs to be flattened
    # TODO: consider normalization (maybe a separate method that generated normalized coords?)
    flattened_coords = numpy.array(sorted_coords).flatten()
    normalized_coords = flattened_coords / max(flattened_coords.max(), 1)
    return normalized_coords

def count_holes(not_occupied):
    # we can count holes by performing a bfs on the coordinates that are 
    # not occupied. we should expect one primary "hole"-- the one that 
    # represents the top half of the board, and if there are no user-created
    # holes then this will be the only one. otherwise, there must be other
    # user-created holes aside from the empty space in the top half of the screen
    not_occupied_list = list(not_occupied)
    visited = set()
    queue = collections.deque()
    holes = -1 #offset to account for the empty space of the regular game board
    current_hold = set()
    for coord in not_occupied:
        if coord not in visited:
            queue.append(coord)
            holes += 1
        while queue:
            row, col = queue.popleft()
            visited.add((row, col))
            # get four directions-- currently_occupied and not_occupied should contain all coordinates
            l = (row, col-1)
            if l in not_occupied:
                queue.append(l)
            r = (row, col+1)
            if r in not_occupied:
                queue.append(r)
            u = (row -1, col)
            if u in not_occupied:
                queue.append(u)
            d = (row +1, col)
            if d in not_occupied:
                queue.append(d)
    return numpy.array(holes)




