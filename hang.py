from game import Game

def hangman():
    game = Game()
    # inputHandler = InputHander()

    # Header of the game
    game.printHeader()

    # Main loop
    while game.canGameContinue():
        print "You have", game.guessesNumber, "guesses left."

        for letter in game.avaiableLetters:
            if letter in game.lettersGuessed:
                game.avaiableLetters = game.avaiableLetters.replace(letter, "")

        print "Available letters", game.avaiableLetters

        # Get letter by input
        game.inputHandler.getPlayerInput()

    else:
        game.endGame()


"""
Start the game!
"""
hangman()
