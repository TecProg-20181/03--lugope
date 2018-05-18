import sys

class InputHandler:
	def __init__(self, game):
		self.game = game

		if not game:
			print "Error log: InputHandler couldn't load Game."
			sys.exit()


	# Get letter by input and verify if the letter belongs to the secret word
	def getPlayerInput(self):
		letter = raw_input("Please guess a letter: ")

		if self.isValidInput(letter):
			if letter in self.game.lettersGuessed:
				print "Oops! You have already guessed that letter: ", self.game.getGessedWord()

			elif letter in self.game.secretWord:
				self.game.lettersGuessed.append(letter)
				print "Good Guess: ", self.game.getGessedWord()

			else:
				self.game.loseOneGuess()
				self.game.lettersGuessed.append(letter)
				print "Oops! That letter is not in my word: ",  self.game.getGessedWord()

		print "------------"

	# Check if the input is a minuscle letter
	def isValidInput(self, letter):
		if letter.isupper():
			print "Please, tipe a minuscle letter."
			return False

		else:
			return True

