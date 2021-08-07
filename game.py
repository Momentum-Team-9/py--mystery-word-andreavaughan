# responses should not be case-sensitive 

# If input is not valid letter, show message that prompts user to put in a valid letter


import random

with open('words.txt') as words:
    lines = words.readlines()
    lines = [line.replace('\n', '') for line in lines]
    easy_words = [line for line in lines if 4 <= len(line) <= 6]
    normal_words = [line for line in lines if 6 <= len(line) <= 8]
    hard_words = [line for line in lines if 8 <= len(line)]

difficulty = input('Select your difficulty level by typing "easy" "normal" or "hard". ')


def set_game_level():
    if difficulty == 'easy':
        word_choice = random.choice(easy_words)
    elif difficulty == 'normal':
        word_choice = random.choice(normal_words)
    elif difficulty == 'hard':
        word_choice = random.choice(hard_words)

    return word_choice


mystery_word = set_game_level()

guess_count = 0 

letter_guesses = []


def display_word(letter, guesses):
    if letter in guesses:
        return letter
    else: 
        return "_"


def print_word(word, guesses):
    output_letters = [display_word(letter, letter_guesses) for letter in mystery_word]
    return(' '.join(output_letters))


first_display = print_word(mystery_word, letter_guesses)

print(f'Your word has {len(mystery_word)} letters:  ', first_display)
print(mystery_word)

user_input = input('Guess a letter: ')

while user_input != 'quit':
    
    if user_input in letter_guesses:
        user_input = input('You\'ve already guessed that letter! Try again. ')

    elif user_input not in letter_guesses and user_input in mystery_word:
        letter_guesses.append(user_input)
        guesses_display = print_word(mystery_word, letter_guesses)
        print(guesses_display)
                
        if "_" not in guesses_display:
            print('You won!')
            user_input = input('Do you want to play again? Type yes or quit. ')
            if user_input == 'yes':
                difficulty = input('Select your difficulty level by typing "easy" "normal" or "hard". ')

                mystery_word = set_game_level()
                guess_count = 0 
                letter_guesses = []
                first_display = print_word(mystery_word, letter_guesses)
                print(f'Your word has {len(mystery_word)} letters:  ', first_display)
                print(mystery_word)

                user_input = input('Guess a letter: ')

        else:
            user_input = input('Correct! Make your next guess. ')

    elif user_input not in letter_guesses and user_input not in mystery_word:
        guess_count += 1

        if guess_count == 8:
            print('You are out of guesses!')
            print(f'The mystery word was {mystery_word}.')
            user_input = input('Do you want to play again? Type yes or quit. ')
            if user_input == 'yes':
                difficulty = input('Select your difficulty level by typing "easy" "normal" or "hard". ')

                mystery_word = set_game_level()
                guess_count = 0 
                letter_guesses = []
                first_display = print_word(mystery_word, letter_guesses)
                print(f'Your word has {len(mystery_word)} letters:  ', first_display)
                print(mystery_word)

                user_input = input('Guess a letter: ')

        else:
            print(f'You\'ve used {guess_count} of 8 incorrect guesses.')
            letter_guesses.append(user_input)
            user_input = input('Incorrect! Try again. ')