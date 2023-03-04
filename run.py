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


# row input and checking values
def get_ship_location():
    row = input("Please enter a ship row 1-8:\n".upper())
    while row not in "12345678":
        print("Please enter a valid row.".upper())
        row = input("Please enter a ship row 1-8:\n".upper())

    # column input and checking values
    column = input("Please enter a ship column A-H:\n".upper())
    while column not in "ABCDEFGH":
        print("Please enter a valid column.".upper())
        column = input("Please enter a ship column A-H:\n".upper())

    return int(row) - 1, to_num[column]


# Function that creates the ships and declere X as hit
def create_ships(board):
    for ship in range(5):
        ship_r, ship_cl = randint(0, 7), randint(0, 7)
        while board[ship_r][ship_cl] == "X":
            ship_r, ship_cl = randint(0, 7), randint(0, 7)
        board[ship_r][ship_cl] = "X"


# Function that counts the remaning ships
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


create_ships(hidden_board)


# Game messages and checking for hit or miss also win or lose
turns = 15
while turns > 0:
    make_board(guess_board)
    row, column = get_ship_location()
    if guess_board[row][column] == "-":
        print("You dont want do do that again do you?".upper())
    elif hidden_board[row][column] == "X":
        print("Bullseye thats a hit!".upper())
        guess_board[row][column] = "X"
        turns -= 1
    else:
        print("Sorry, you poffed".upper())
        guess_board[row][column] = "-"
        turns -= 1
    if count_hit_ships(guess_board) == 5:
        print("Congratulations you have conquered this battlefield".upper())
        break
    print(f"You have {turns} turns remaining".upper())
    if turns == 0:
        print("Game Over, better luck next time!".upper())
