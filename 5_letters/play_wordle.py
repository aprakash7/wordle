from wordle import Wordle
from colorama import Fore, init
from letter_states import LetterStates
import random

init() #windows

def main():
	word_set= load_data_set(r'data/wordle_words5.txt') #set path
	secret= random.choice(list(word_set))
	wordle= Wordle(secret)

	#play till correct
	while wordle.can_attempt:
		x= input("\nType your guess: ")

		if len(x)!= wordle.WORD_LENGTH:
			print(Fore.RED + f"Word must be {wordle.WORD_LENGTH} characters long" + Fore.RESET)
			continue 
		if not x in word_set:
			print("Invalid word!")
			continue

		wordle.attempt(x)
		display_res(wordle)
		
	if wordle.solved: #solved
		
		if len(wordle.attempts)==1:
			print(f"You have completed the puzzle in 1 attempt! ")
		else:
			print(f"You have completed the puzzle in {len(wordle.attempts)} attempts!")
	else:
		print("Your failed!")
		print(f"The secret word was: {wordle.secret} ")

#displays the result
def display_res(wordle: Wordle):
	print("\nResults so far.. ")	
	print(f"You have {wordle.rem_attempts} attempts remaining")

	lines= []
	#convert to color
	for word in wordle.attempts:
		result= wordle.guess(word)
		colored_result= res_in_color(result)
		lines.append(colored_result) 

	#print _ for the remaining attempts
	for _ in range(wordle.rem_attempts):
		lines.append(" ".join(["_"] *wordle.WORD_LENGTH))

	border(lines)

def load_data_set(path: str):
	word_set= set()
	with open(path, 'r') as f:
		for line in f.readlines():
			word= line.strip().upper()
			word_set.add(word)
	return word_set

#colored results
def res_in_color(result: list[LetterStates]):
	res_with_color= []

	#designate colors
	for letter in result:
		if letter.in_position:
			color= Fore.GREEN
		elif letter.in_word: 
			color= Fore.YELLOW
		else:
			color= Fore.WHITE

		colored_letter= color+ letter.character + Fore.RESET
		res_with_color.append(colored_letter)

	#join strings as one string 	
	return " ".join(res_with_color)

def border(lines: list[str], size:int= 9, pad: int=1):
	content_len= size+ pad*2
	top_border= "┌" + "─" *content_len+ "┐"
	bottom_border= "└" + "─" *content_len+ "┘"
	space= " " *pad

	print(top_border)
	for line in lines:
		print("│" + space+ line + space+ "│")
	print(bottom_border)

if __name__=="__main__":
	main()