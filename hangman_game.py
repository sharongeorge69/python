import random
import hangman_words
import hangman_art
logo = hangman_art.logo
print(logo)
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
stages = hangman_art.stages
# print(chosen_word)
word_len = len(chosen_word)
s = ""
for letter in range(word_len):
    s+= "_"
print(s)
game_over = False
correct_letter = []
lives = 6
while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess word :").lower()
    display = ""
    if guess in correct_letter:
        print(f'You\'ve already guessed {guess}')
    for letter in chosen_word:
        if letter == guess:
            display+=letter
            correct_letter.append(guess)

        elif letter in correct_letter:

            display+=letter
        else:
            display += "_"

    print(display)
    if "_" not in display:
        game_over = True
        print("You won")

    if guess not in chosen_word:
        lives -=1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives ==0:
            game_over = True
            print(f"***********************It was {chosen_word}! YOU LOSE**********************")

    print(stages[lives])