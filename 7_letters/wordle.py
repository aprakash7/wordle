from letter_states import LetterStates

class Wordle:

	MAX_ATTEMPTS= 8
	WORD_LENGTH= 7

	#constructor 
	def __init__(self, secret: str):
		self.secret:str= secret.upper()
		self.attempts= []

		pass

	#add words to the attempts
	def attempt(self, word:str):
		word= word.upper()
		self.attempts.append(word)

	def guess(self, word: str):
		#list of letter states
		word= word.upper()
		result= []
		
		for i in range(self.WORD_LENGTH):
			character = word[i]
			letter= LetterStates(character)

			#just compare whether the character matches the word
			letter.in_word= character in self.secret 
			#compare the position of the character with the word
			letter.in_position= character == self.secret[i]
			result.append(letter)
		return result
		
	#@property -> instead of wordle.is_solved, no need to invoke it -treat like a variable.
	@property 
	def solved(self):
		return len(self.attempts)>0 and self.attempts[-1]== self.secret

	@property
	def rem_attempts(self) -> int: #number
		return self.MAX_ATTEMPTS - len(self.attempts)

	@property 
	def can_attempt(self): #attempt till correct, cannot after all tries
		return self.rem_attempts> 0 and not self.solved
