"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.
do initialization message with sleep module
"""

import random


def start_game():
    answer = random.randint(1, 10)
    number_of_guesses = 1
    high_score = number_of_guesses
    exit_game_message = "Thanks for playing. See you next time!"

    def in_game_message(message):
        print("\n" + "-" * 50)
        print(message)
        print("-" * 50 + "\n")

    in_game_message("Welcome to The Number Guessing Game!")
    print("Type EXIT to leave the game.\n")


    while True:
        try:
            prompt = input("Pick a number between 1 and 10: ")
            if prompt == "EXIT":
                in_game_message(exit_game_message)
                break
            guess = int(prompt)

            if guess > 10 or guess < 1:
                raise ValueError()

            if guess < answer:
                print("It's higher!")
                number_of_guesses += 1

            if guess > answer:
                print("It's lower!")
                number_of_guesses += 1


            elif guess == answer:
                print("\nYou got it! It took you {} tries!".format(number_of_guesses))
                play_again = input("Would you like to play again? [y]es/[n]o: ")


                if high_score == 1:
                    high_score = number_of_guesses
                    print("\nThe HIGHSCORE is {}".format(number_of_guesses))
                else:
                    print("\nThe HIGHSCORE is {}".format(number_of_guesses))

                if play_again.upper() == 'Y':
                    high_score = number_of_guesses
                    print("\nYour score is {}".format(high_score))
                    number_of_guesses = 1
                    continue
                else:
                    in_game_message(exit_game_message)
                    break
        except ValueError:
            print("Oops!! Your guess must be a number between 1 and 10. Try again.\nType EXIT to leave the game")


if __name__ == '__main__':
    start_game()
