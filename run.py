from random import randint

# Declare game boards
hidden_board = [[" " for _ in range(8)] for _ in range(8)]
guess_board = [[" " for _ in range(8)] for _ in range(8)]

# Converts letter to numbers
to_num = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}

# Game info for user understanding
print("-----------------------------")
print("You have entered the\nbattlefield take aim and fire".upper())
print("-----------------------------")
print("You have 15 shots to take\ndown the 5 battleships".upper())
print("-----------------------------")


# Setting row and column explanation
def make_board(board):
    print("   A B C D E F G H")
    print("-----------------------------")
    # Print each row of the board
    for i, row in enumerate(board):
        # Convert the row to a string with '|' separators
        row_str = '|'.join(row)
        # Print the row number and the row string
        print(f"{i+1:2d}|{row_str}|")
    print("-----------------------------")
