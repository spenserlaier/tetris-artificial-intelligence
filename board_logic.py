import collections


def generate_board_square_positions(board, starting_x, starting_y, square_size):
    curr_x, curr_y = starting_x, starting_y
    rec_positions = []
    for row in board:
        curr_y += square_size 
        curr_x = starting_x
        curr_row = list()
        for col in row:
            curr_x += square_size 
            curr_row.append((curr_x, curr_y))
        rec_positions.append(curr_row)
    return rec_positions

def init_next_piece_display(rows=5, cols=5):
    return [[0 for _ in range(cols)]for _ in range(rows)]

def clear_rows(occupied_coordinates, num_rows, num_cols, colors_at_coordinates):
    blocks_in_row = collections.defaultdict(lambda: 0)
    for row, col in occupied_coordinates:
        blocks_in_row[row] += 1
    rows_to_remove = set()
    score = 0
    for i in range(0, num_rows):
        if blocks_in_row[i] == num_cols:
            rows_to_remove.add(i)
            score += num_cols
    downward_shifts = collections.defaultdict(lambda: 0)
    # how much does each row need to be shifted down? default 0
    cnt = 0
    for i in range(num_rows-1, -1, -1):
        if i in rows_to_remove:
            cnt += 1
        else:
            downward_shifts[i] = cnt
    new_coordinates = set()
    new_colors = dict()
    for row, col in occupied_coordinates:
        if row in rows_to_remove:
            continue
        else:
            new_coordinates.add((row + downward_shifts[row], col))
            new_colors[(row + downward_shifts[row], col)] = colors_at_coordinates[(row, col)]
    return (new_coordinates, new_colors, score)

        










def init_board(rows=20, cols=10):
    return [[0 for _ in range(cols)]for _ in range(rows)]

def get_pixel_positions():
    # TODO: more concise pixel position calculator
    return 5


def get_column_heights(num_rows, occupied_coordinates):
    max_height_at_column = collections.defaultdict(lambda: num_rows)
    for row, col in occupied_coordinates:
        max_height_at_column[col] = min(max_height_at_column[col], row)
    #print(max_height_at_column)
    return max_height_at_column

