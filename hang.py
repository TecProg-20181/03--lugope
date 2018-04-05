import random
import string
from game import Game

WORDLIST_FILENAME = "palavras.txt"

def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    secretLetters = []

#    for letter in secretWord:
#        if letter in secretLetters:
#            secretLetters.append(letter)
#        else:
#            pass

    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True

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

    game.guessesNumber = 8
    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word (', game.secretWord,') that is', len(game.secretWord), 'letters long.' #hide secret word later
    print '-------------'

    while  isWordGuessed(game.secretWord, game.lettersGuessed) == False and game.guessesNumber >0:
        print 'You have ', game.guessesNumber, 'guesses left.'

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
        if isWordGuessed(game.secretWord, game.lettersGuessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', game.secretWord, '.'


"""
MAIN()
"""
hangman()
