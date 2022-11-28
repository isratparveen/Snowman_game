import random
from snowman_words import words
from snowman_visuals import snowman_visual_dict
import string


def get_valid_word(words):
    random_word = random.choice(words)  # randomly chooses something from the list
    while '-' in random_word or ' ' in random_word:
        random_word = random.choice(words)

    return random_word.upper()


def snowman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabets = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    pieces = 7

    # getting user input
    while len(word_letters) > 0 and pieces > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', pieces, 'pieces left to save the snowman.')
        print('You have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(snowman_visual_dict[pieces])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                pieces = pieces - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if pieces == 0:
        print(snowman_visual_dict[pieces])
        print('Snowman died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, 'and saved the snowman!!')


if __name__ == '__main__':
    snowman()