import random
import string
from game import Game

def getGuessedWord():

     guessed = ''


     return guessed

def getAvailableLetters():
    import string
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase


    return available

def hangman():
    game = Game()

    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word (', game.secretWord,') that is', len(game.secretWord), 'letters long.' #hide secret word later
    print '-------------'

    while  game.canGameContinue():
        print 'You have', game.guessesNumber, 'guesses left.'

        available = getAvailableLetters()
        for letter in available:
            if letter in game.lettersGuessed:
                available = available.replace(letter, '')

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        if letter in game.lettersGuessed:

            guessed = getGuessedWord()
            for letter in game.secretWord:
                if letter in game.lettersGuessed:
                    guessed += letter
                else:
                    guessed += ' _ '

            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in game.secretWord:
            game.lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in game.secretWord:
                if letter in game.lettersGuessed:
                    guessed += letter
                else:
                    guessed += ' _ '

            print 'Good Guess: ', guessed
        else:
            game.guessesNumber -=1
            game.lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in game.secretWord:
                if letter in game.lettersGuessed:
                    guessed += letter
                else:
                    guessed += ' _ '

            print 'Oops! That letter is not in my word: ',  guessed
        print '------------'

    else:
        game.endGame()


"""
MAIN()
"""
hangman()
