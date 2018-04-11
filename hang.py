from game import Game

def hangman():
    game = Game()

    # Header of the game
    print "Welcome to the game, Hangam!"
    print "I am thinking of a word that is", len(game.secretWord), "letters long."
    print "This secret word has", game.differentLettersNumber(game.secretWord), "different letters."
    print "-------------"

    # Main loop
    while game.canGameContinue():
        print "You have", game.guessesNumber, "guesses left."

        for letter in game.avaiableLetters:
            if letter in game.lettersGuessed:
                game.avaiableLetters = game.avaiableLetters.replace(letter, "")

        print "Available letters", game.avaiableLetters

        # Get letter by input and verify if the letter belongs to the secret word
        letter = raw_input("Please guess a letter: ")
        if letter in game.lettersGuessed:
            print "Oops! You have already guessed that letter: ", game.getGessedWord()

        elif letter in game.secretWord:
            game.lettersGuessed.append(letter)
            print "Good Guess: ", game.getGessedWord()

        else:
            game.guessesNumber -= 1
            game.lettersGuessed.append(letter)
            print "Oops! That letter is not in my word: ",  game.getGessedWord()

        print "------------"

    else:
        game.endGame()


"""
Start the game!
"""
hangman()
