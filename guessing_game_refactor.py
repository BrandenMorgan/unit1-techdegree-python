import random


def in_game_message(message):
    print("\n" + "-" * 50)
    print(message)
    print("-" * 50 + "\n")



def get_users_number():
    while True:
        try:
            # I left out the EXIT code. How would you get that back in?
            # New exit code here and also in beginning of start_game()
            prompt = input("Pick a number between 1 and 10: ")
            if prompt == "EXIT":
                return prompt
            prompt = int(prompt)
            if prompt <= 0 or prompt > 10:
                raise ValueError
            return prompt
        except ValueError:
            print("Please enter a number between 1 and 10.\n")


def start_game():
    answer = random.randint(1, 10)
    number_of_guesses = 1
    high_score = number_of_guesses
    exit_game_message = "Thanks for playing. See you next time!"
    in_game_message("Welcome to The Number Guessing Game!")
    print("Type EXIT to leave the game")
    while True:
        guess = get_users_number()
        # New exit code
        if type(guess) == str:
            in_game_message(exit_game_message)
            break

        if guess < answer:
            print("It's higher!")
            number_of_guesses += 1
        if guess > answer:
            print("It's lower!")
            number_of_guesses += 1
        elif guess == answer:
            print("\nYou got it! It took you {} tries!".format(number_of_guesses))
            play_again = input("Would you like to play again? [y]es/[n]o: ")

            # High score calculation. I wanna get this behavior down and maybe put it into a function
            if high_score == 1:
                # number of guesses for first round always high score.
                high_score = number_of_guesses
                print("1\nThe HIGHSCORE is {}".format(high_score))
            if number_of_guesses < high_score:
                print("2\nThe HIGHSCORE is {}".format(number_of_guesses))

            if play_again.upper() == 'Y':
                if number_of_guesses < high_score:
                    print("3\nThe HIGHSCORE is {}".format(number_of_guesses))

                # print("3\nYour SCORE is {}".format(high_score))
                # print("4\nThe HIGHSCORE is {}".format(high_score))
                print("4\nYour SCORE is {}".format(number_of_guesses))
                high_score = number_of_guesses
                number_of_guesses = 1
                continue
            else:
                in_game_message(exit_game_message)
                break
if __name__ == '__main__':
    start_game()
