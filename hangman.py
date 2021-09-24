import random
import stage_art
import words


class Hangman:
    def __init__(self, manual_word=None):
        self.incorrect = 0
        if manual_word is not None:
            self.word = manual_word
        else:
            self.word = random.choice(words.word_list)
        self.word_list = list(self.word)
        self.reveal = list('_' * len(self.word))
        self.stage = ''
        self.guesses = []

    def validate_guess(self, guess):
        # single letter
        if len(guess) == 1:
            self.guesses.append(guess)
            # look for guessed letter in word
            if guess in self.word:
                for i in range(0, len(self.word_list)):
                    if guess == self.word_list[i]:
                        self.reveal[i] = guess
            else:
                self.incorrect += 1
                self.stage = stage_art.stage[str(self.incorrect)]
        # word
        else:
            if guess != self.word:
                self.guesses.append(guess)
                self.incorrect += 1
                self.stage = stage_art.stage[str(self.incorrect)]

    def print_status(self):
        print()
        print('Current Status')
        print(' '.join(self.reveal))
        print(f"""Guesses: {', '.join(self.guesses)}""")
        print(self.stage)
        if self.incorrect == 10:
            print('Sorry, you ran out of chances')
            print(f'The word was "{self.word}"')
