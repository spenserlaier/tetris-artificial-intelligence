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

