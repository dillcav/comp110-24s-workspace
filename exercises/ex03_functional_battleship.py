"""EX 03 - Functional Battelship - A full game with 5 guesses!"""

__author__ = "730499558"
import random

def input_guess(grid_size: int,r_or_c: str) -> int:
    """Takes in the users guess for row or column."""
    assert r_or_c == "row" or r_or_c == "column"
    guess: int = int(input(f"Guess a {r_or_c}: "))
    while guess > grid_size or guess <= 0:
        guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    return guess

def print_grid(grid_size: int,row_guess: int,col_guess: int,correct: bool) -> None:
    """Setting up the emojis."""
    row_count: int = 1
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
    result: str = ""
    if correct == True:
        result += RED_BOX
    else:
        result += WHITE_BOX
    while row_count <= grid_size:
        emojis: str = ""
        col_count: int = 1
        if row_guess == row_count:
            while col_count <= grid_size:
                if col_guess == col_count:
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

def correct_guess(secret_row: int, secret_col: int, row_guess: int, col_guess: int) -> bool:
    """Determine if a guess is correct."""
    return bool((secret_row == row_guess) and (secret_col == col_guess))

def main(grid_size: int, secret_row: int, secret_col: int) -> None:
    """Putting it all together!"""
    turn: int = 1
    state: bool = True
    while state == True:
        print(f"=== Turn {turn}/5 ===")
        row_guess: int = input_guess(grid_size, "row")
        col_guess: int = input_guess(grid_size, "column")
        correct: bool = correct_guess(secret_row, secret_col, row_guess, col_guess)
        print_grid(grid_size, row_guess, col_guess, correct)
        if correct == True:
            print("Hit!")
            print(f"You won in {turn}/5 turns!")
            state = False
        else:
            print("Miss!")
            if turn == 5:
                print("X/5 - Better luck next time!")
                state = False
            else:
                turn += 1

if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))