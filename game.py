# User selects difficulty
# Computer selects word from .txt based on difficulty 
# Computer returns text letting user know how many letters and shows spaces
# User inputs letter
# Take letter input and compare to word
# If letter is in word, return space filled in with letter, and input for next word 
# If letter is not, return wrong letter message and increment guess counter 
# If input is not valid letter, show message that prompts user to put in a valid letter
# If input is an already guessed letter, show message and don't increment guess counter
# End game when letter is complete OR guess count reaches 8
# Ask user if they want to play again

mystery_word = 'better'

user_input = input('Guess a letter: ')

guess_count = 1 

letter_guesses = []


def display_word(letter, guesses):
    if letter in guesses:
        return letter
    else: 
        return "_"


def print_word(word, guesses):
    output_letters = [display_word(letter, letter_guesses) for letter in mystery_word]
    print(' '.join(output_letters))


while user_input != 'Quit':
    if guess_count == 8:
        print('You are out of guesses!')
        break

    elif user_input in letter_guesses:
        user_input = input('You\'ve already guessed that letter! Try again. ')

    elif user_input not in letter_guesses and user_input in mystery_word:
        letter_guesses.append(user_input)
        guesses_display = print_word(mystery_word, letter_guesses)
        
        if mystery_word == guesses_display:
            print('You won!')

        else:
            user_input = input('Correct! Make your next guess. ')

    elif user_input not in letter_guesses and user_input not in mystery_word:
        user_input = input('Incorrect! Try again. ')
        letter_guesses.append(user_input)