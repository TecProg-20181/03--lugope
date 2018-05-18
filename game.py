import random
import string

WORDLIST_FILENAME = "palavras_test.txt"

class Game:
	# Overloads init
	def __init__(self, guessesNumber=5):
		self.guessesNumber = guessesNumber #With default value of 5
		self.secretWord = self.pickSecretWord()
		self.lettersGuessed = [] #Initiate with no letters guessed
		self.avaiableLetters = string.ascii_lowercase #All the letters in lower case

	# Overloads printing
	def __repr__(self):
		msg = "Hi, I'm the curent game :D"

		return msg

	# Pick a random word from a text file loaded
	def pickSecretWord(self):
		wordList = self.loadWords()
		print "\t", len(wordList), "words loaded.\n"

		while True:
			word = random.choice(wordList)

			if self.differentLettersNumber(word) <= self.guessesNumber:
				return word.lower()

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

	# Return word guessed so far
	def getGessedWord(self):
		guessedWord = ""
		for letter in self.secretWord:
			if letter in self.lettersGuessed:
				guessedWord += letter
			else:
				guessedWord += ' _ '

		return guessedWord

	# Verify if the Game can keep going on
	def canGameContinue(self):
		if not self.isWordGuessed() and self.guessesNumber > 0:
			return True
		else:
			return False

	# Verify if the word was guessed
	def isWordGuessed(self):
		for letter in self.secretWord:
			if letter in self.lettersGuessed:
				pass
			else:
				return False

		return True	

	# Finish the game
	def endGame(self):
		if self.isWordGuessed():
			print 'Congratulations, you won!'
		else:
			print 'Sorry, you ran out of guesses. The word was', self.secretWord, '.'

	# Find out how many different letters are in the word
	def differentLettersNumber(self, word):
		if word:
			letters = []
			for letter in word:
				if letter not in letters:
					letters.append(letter)

			return len(letters)
		else:
			return 0

