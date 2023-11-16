import random


red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
gray = (50,50,50)
black = (0,0,0)

piece_colors = [red,
                green,
                blue]


def get_random_piece_color():
    return random.choice(piece_colors)
