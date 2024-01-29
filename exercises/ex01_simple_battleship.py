"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730499558"
# Box Codes:
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
# Player 1's turn:
boat_location: int = int(input("Pick a secret boat location between 1 and 4: "))
if boat_location < 1:
    print("Error! " + str(boat_location) + " too low!")
    exit()
else:
    if boat_location > 4:
        print("Error! " + str(boat_location) + " too high!")
        exit()
# Player 2's turn:
player_guess: int = int(input("Guess a number between 1 and 4: "))
if player_guess < 1:
    print("Error! " + str(player_guess) + " too low!")
    exit()
else:
    if player_guess > 4:
        print("Error! " + str(player_guess) + " too high!")
        exit()
# Results:
if boat_location == player_guess:
    result: str = RED_BOX
    emojis: str = ""
    if player_guess == 1:
        emojis += result
    else:
        emojis += BLUE_BOX
    if player_guess == 2:
        emojis += result
    else:
        emojis += BLUE_BOX
    if player_guess == 3:
        emojis += result
    else:
        emojis += BLUE_BOX
    if player_guess == 4:
        emojis += result
    else:
        emojis += BLUE_BOX
    print(emojis)
    print("Correct! You hit the ship.")
else:
    result: str = WHITE_BOX
    emojis: str = ""
    if player_guess == 1:
        emojis += result
    else:
        emojis += BLUE_BOX
    if player_guess == 2:
        emojis += result
    else:
        emojis += BLUE_BOX
    if player_guess == 3:
        emojis += result
    else:
        emojis += BLUE_BOX
    if player_guess == 4:
        emojis += result
    else:
        emojis += BLUE_BOX
    print(emojis)
    print("Incorrect! You missed the ship.")