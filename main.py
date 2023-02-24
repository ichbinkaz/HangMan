import random
import hangman_art
import hangman_words


def random_word(vocabulary):
    global chosen_word
    global display
    chosen_word = random.choice(vocabulary)
    display = []

    for letter in chosen_word:
        display.append("_")


def guess_letter():
    global chosen_word
    global display
    lives = 6
    end_of_game = False
    while not end_of_game:

        guess = input("Please guess a letter: ").lower()
        if guess in display:
            print(f"You already have {guess}, please choose another letter")

        chosen_word_len = len(chosen_word)

        for letter in range(chosen_word_len):
            index = chosen_word[letter]
            if guess == index:
                display[letter] = index

        if not guess in display:
            print(f"The letter {guess} is not present in the word, please choose another letter")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You've lost")

        print(f"{' '.join(display)}")
        print(hangman_art.stages[lives])

        if "_" not in display:
            end_of_game = True
            print("You've won")

        print(lives)


print(hangman_art.logo)
print()
random_word(hangman_words.word_list)
guess_letter()
print(f"The actual word is: {chosen_word}")