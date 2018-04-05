import random
import string

WORDLIST_FILENAME = "palavras.txt"

class Game:
	# Overloads init
	def __init__(self, guessesNumber=8):
		self.guessesNumber = guessesNumber
		self.secretWord = self.pickSecretWord()
		self.lettersGuessed = []
		self.avaiableLetters = string.ascii_lowercase
	#--

	# Overloads printing
	def __repr__(self):
		msg = "Hi, my name is %s\n" % self.guessesNumber
		msg = msg + "Some other shit.\n"

		return msg
	#--

	# Pick a random word from a text file loaded
	def pickSecretWord(self):
		wordList = self.loadWords()
		word = random.choice(wordList)
		print "  ", len(wordList), "words loaded."

		return word.lower()
	#--

	# Load text file
	def loadWords(self):
		"""
		Depending on the size of the word list, this function may
		take a while to finish.
		"""
		print "Loading word list from file..."# inFile: file
		inFile = open(WORDLIST_FILENAME, 'r', 0)
		# line: string
		line = inFile.readline()
		# wordList: list of strings
		wordList = string.split(line)
		# Close file
		inFile.close()
		
		return wordList
	#--

