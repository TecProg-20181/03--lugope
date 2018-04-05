import string

class Game:
	WORDLIST_FILENAME = "palavras.txt"

	#Overloads init
	def __init__(self, guessesNumber=8):
		self.guessesNumber = guessesNumber
		self.secretWord = self.pickSecretWord()
		self.lettersGuessed = []
		self.avaiableLetters = string.ascii_lowercase

	#Overloads printing
	def __repr__(self):
		msg = "Hi, my name is %s\n" % self.guessesNumber
		msg = msg + "Some other shit.\n"

		return msg

	#Other functions
	def pickSecretWord(self):
		word = "aaa"

		return word