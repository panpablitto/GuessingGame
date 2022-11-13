#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo
print(logo)
computer_num = random.randint(1, 100)


def game_level():
    game_level_score = [5, 10]
    game_level = input("Which level would you like to play easy or hard \n")
    if game_level=="easy":
        return game_level_score[1]
    elif game_level=="hard":
        return game_level_score[0]

def comparason(user_guess):
    if user_guess> computer_num:
        print("Too high")
        return True
    elif user_guess< computer_num:
        print("Too low")
        return True
    elif user_guess == computer_num:
        print("You win")
        return False

def game():
    keep_playing = True
    selected_score = game_level()
    while keep_playing ==True:
        user_guess = int(input("Guess the number: "))
        keep_playing = comparason(user_guess)
        if selected_score == 1:
            print("you lose")
            keep_playing = False
        else:
            selected_score-=1
            print(f"You have still {selected_score} guesses to take")


game()


