"""EX 02 - One Shot Battleship - A 4 by 4 grid"""

__author__ = "730499558"
grid_size: int = 4
secret_row: int = 3
secret_col: int = 2
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
result: str = ""
row_count: int = 1
# Making a guess
boat_row: int = int(input("Guess a row: "))
while boat_row > grid_size:
    new_row_guess: int = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    boat_row = new_row_guess
boat_col: int = int(input("Guess a column: "))
while boat_col > grid_size:
    new_col_guess: int = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    boat_col = new_col_guess
# Determining if it hit
if boat_row == secret_row:
    if boat_col == secret_col:
        result = RED_BOX
    else:
        result = WHITE_BOX
else:
    result = WHITE_BOX
# Creating the emoji grid
while row_count <= grid_size:
    emojis: str = ""
    col_count: int = 1
    if boat_row == row_count:
        while col_count <= grid_size:
            if boat_col == col_count:
                emojis += result
            else:
                emojis += BLUE_BOX
            col_count += 1
    else:
        while col_count <= grid_size:
            emojis += BLUE_BOX
            col_count += 1
    print(emojis)
    row_count += 1
# User Feedback
if boat_row == secret_row:
    if boat_col == secret_col:
        print("Hit!")
    else:
        print("Close! Correct row, wrong column.")
else:
    if boat_col == secret_col:
        print("Close! Correct column, wrong row.")
    else:
        print("Miss!")