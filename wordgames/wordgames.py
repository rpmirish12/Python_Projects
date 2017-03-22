import random


def process_letter(letter, secret_word, blanked_word):
    result = False
    for i in range(0, len(secret_word)):
        if letter == secret_word[i]:
            blanked_word[i] = letter
            result = True
    return result


def show_word(word):
    for character in word:
        print(character, " ", end="")
    print("")


def get_guess():
    print("Enter a letter: ")
    return input()


def get_random_word():
    words = ["pizza", "cheese", "apples"]
    rand_word = words[random.randint(0, len(words)-1)]
    return rand_word


def print_strikes(num_strikes):
    for i in range(0, num_strikes):
        print("X ", end="")
    print("")


def play_word_game():
    strikes = 0
    max_strikes = 3
    playing = True

    my_word = get_random_word()
    blanked_word = list("_" * len(my_word))

    while playing:
        show_word(blanked_word)
        letter = get_guess()
        found = process_letter(letter, my_word, blanked_word)
        if not found:
            strikes += 1
            print_strikes(strikes)

        if strikes >= max_strikes:
            playing = False

        if not "_" in blanked_word:
            playing = False

    if strikes >= max_strikes:
        print("loser!")
    else:
        print("winner!")


print("Game Started!")
play_word_game()
print("Game Over!")
