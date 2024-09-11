from random import randint
from guess_art import logo
EASY_TURNS = 10
HARD_TURNS = 5


def check_answer(user_guess, answer, turn):
    if user_guess > answer:
        print("Too high")
        return turn - 1

    elif user_guess < answer:
        print("Too Low")
        return turn - 1
    else:
        print(f"You have guessed the correct number : {answer}")


def difficulty():
    easy_or_hard = input("Type 'easy' or 'hard' : ")
    if easy_or_hard == "easy":
        return EASY_TURNS
    else:
        return HARD_TURNS


def game():
    print("I am guessing a number between 1 and 100 : ")
    answer = randint(1, 100)
    turn = difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turn} attempts to make the guesses!")
        guess = int(input("Make a guess : "))
        turn = check_answer(guess, answer, turn)
        if turn == 0:
            print("Oops! you have failed")
            return
        elif guess!=answer:
            print("Guess again!")


game()
