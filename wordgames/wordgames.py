import random

def show_word(word):
    for character in word:
        print(character, " ", end="")
    print("")

def get_guess():
    return "letter"

def get_random_word():
    words = ["pizza", "cheese", "apples"]
    rand_word = words[random.randint(0, len(words)-1)]
    return rand_word


def play_word_game():
    strikes = 0
    max_strikes = 3
    playing = True

    my_word = get_random_word()
    blanked_word = "_" * len(my_word)

    while playing:
        show_word(blanked_word)
        letter = get_guess()
        print(letter)
        strikes += 1
        if strikes >= max_strikes:
            playing = False

    if strikes >= max_strikes:
        print("loser!")
    else:
        print("winner!")
        print(my_word)


print("Game Started!")
play_word_game()
print("Game Over!")
