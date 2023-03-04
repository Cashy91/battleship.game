from random import randint

# Declare game boards
hidden_board = [[" " for _ in range(8)] for _ in range(8)]
guess_board = [[" " for _ in range(8)] for _ in range(8)]

# Converts letter to numbers
to_num = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}