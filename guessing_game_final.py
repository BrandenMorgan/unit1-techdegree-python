import random


def in_game_message(message):
    print("\n" + "-" * 50)
    print(message)
    print("-" * 50 + "\n")


def get_users_number():
    while True:
        try:
            prompt = input("Pick a number between 1 and 10: ")
            if prompt == "EXIT":
                return prompt
            prompt = int(prompt)
            if prompt <= 0 or prompt > 10:
                raise ValueError
            return prompt
        except ValueError:
            print("Please enter a number between 1 and 10.\n")


def calculate_high_score(score, guesses):
    if score > guesses:
        score = guesses
    return score


def keep_playing(answer, score, guesses):
    if answer.upper() == 'Y':
        print("\nThe HIGHSCORE is {}".format(score))
        print("Your SCORE is {}".format(guesses) + "\n")
    return answer


def start_game():
    answer = random.randint(1, 10)
    number_of_guesses = 1
    high_score = 1000
    exit_game_message = "Thanks for playing. See you next time!"
    in_game_message("Welcome to The Number Guessing Game!")
    print("Type EXIT to leave the game")
    while True:
        guess = get_users_number()
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
            high_score = calculate_high_score(high_score, number_of_guesses)
            if high_score >= number_of_guesses:
                in_game_message("****CONGRATULATIONS!!! You got the HIGHSCORE!!!****")
            print("\nYou got it! It took you {} tries!".format(number_of_guesses))
            play_again = input("Would you like to play again? [y]es/[n]o: ")
            play_again = keep_playing(play_again, high_score, number_of_guesses)
            if play_again.upper() == "Y":
                number_of_guesses = 1
                answer = random.randint(1, 10)
                continue
            in_game_message(exit_game_message)
            break
if __name__ == '__main__':
    start_game()
