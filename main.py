from hangman import Hangman

if __name__ == '__main__':
    manual_option = input('Would you like to provide your own word to guess? (y/N) ')
    if manual_option.upper() == 'Y':
        manual_word = input('Please provide your word:')
        print('\n' * 20)  # print blank lines to hide input
    else:
        manual_word = None

    hangman = Hangman(manual_word)
    print('------------------')
    print('Welcome to Hangman')
    print('------------------')
    print('Aim: Guess the word by providing letters')

    while hangman.incorrect < 10:
        player_guess = input('Please enter your guess: ')

        # check for already guessed letters
        if player_guess in hangman.guesses:
            print('You have already tried that. Try again')
            continue
        # check for blank entries
        if len(player_guess) < 1:
            print('Please guess a letter or complete word')
            continue

        hangman.validate_guess(player_guess)

        # check if word completed
        if hangman.reveal.count('_') == 0 or player_guess == hangman.word:
            print('CONGRATULATIONS! You have guessed the word!')
            print(hangman.word)
            break

        hangman.print_status()

#todo: add a external word load
#todo: add a "play again?" at end of game
#todo: improve on the screen clearing
#todo: ensure colours work in terminal
