class LetterStates:

	def __init__(self, character: str):
		self.character: str= character
		self.in_word: bool1= False
		self.in_position: boo2= False
	
	#overrides the returning of addresses for result= wordle.guess(x)
	def __repr__(self):
		return f"[{self.character} in_word: {self.in_word} in_position: {self.in_position}]"