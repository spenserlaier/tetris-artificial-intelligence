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

def get_time(current_time):
    return numpy.array(current_time)

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

def generate_input_state(rows, cols, occupied_coordinates, piece):
    board_state = generate_board_array(rows, cols, occupied_coordinates)
    piece_type = get_piece_type(piece)
    piece_coords = get_piece_coordinates(piece)
    normalized_coords = get_normalized_piece_coordinates(piece)
    output_arr = numpy.concatenate((board_state, piece_type, piece_coords, normalized_coords))
    # print(f"complete board state: {output_arr}")
    return output_arr
    

def get_average_coord_height(occupied_coordinates, max_rows):
    total_row_heights = 0

    for row, col in occupied_coordinates:
        total_row_heights += (max_rows - row)
    return total_row_heights // len(occupied_coordinates) if occupied_coordinates else 0

def get_normalized_piece_coordinates(piece):
    sorted_coords = sorted(list(piece.coordinates))
    flattened_coords = numpy.array(sorted_coords).flatten()
    normalized_coords = flattened_coords / max(flattened_coords.max(), 1)
    return normalized_coords

def get_piece_height_penalty(occupied_coords, piece):
    # a bit paradoxical, because when rows are used,
    # higher rows mean lower down in the grid
    min_row = float('inf')
    result = 0
    for row, col in occupied_coords:
        min_row = min(row, min_row)
    for row, col in piece.coordinates:
        if row < min_row:
            # penalize for each coordinate above the tallest row
            result -= 1
        elif row == min_row:
            continue
        else:
            result += 1
    return result



def get_number_of_good_rows(occupied_coords):
    blocks_in_rows = collections.defaultdict(lambda: 0)
    for row, col in occupied_coords:
        blocks_in_rows[row] += 1
    good_rows = [key for key in blocks_in_rows.keys() if blocks_in_rows[key] >= 7]
    return len(good_rows)

def get_max_column_height(occupied_coords):
    column_counts = collections.defaultdict(lambda: 0)
    for row, col in occupied_coords:
        column_counts[col] += 1
    out = 0
    for col in column_counts:
        out = max(column_counts[col], out)
    return out


def get_max_row_width(occupied_coords):
    row_counts = collections.defaultdict(lambda: 0)
    for row, col in occupied_coords:
        row_counts[row] += 1
    out = 0
    for row in row_counts:
        out = max(row_counts[row], out)
    return out

def get_average_row_width(occupied_coords):
    row_widths = collections.defaultdict(lambda: 0)
    for row, col in occupied_coords:
        row_widths[row] += 1
    return 0 if not occupied_coords else sum(row_widths.values())//len(row_widths)






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
            l = (row, col-1)
            if l in not_occupied and l not in visited:
                queue.append(l)
            r = (row, col+1)
            if r in not_occupied and r not in visited:
                queue.append(r)
            u = (row -1, col)
            if u in not_occupied and u not in visited:
                queue.append(u)
            d = (row +1, col)
            if d in not_occupied and d not in visited:
                queue.append(d)
    return numpy.array(holes)




