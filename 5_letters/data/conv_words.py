#Clean dataset
def main5():
	input_data_path= "wordle_data.txt"
	
	output_data_path5= "wordle_words5.txt"
	
	five_let_words= []

	with open(input_data_path, "r") as f:
		for line5 in f.readlines():
			word5= line5.strip() #remove whitespace
			if len(word5)== 5: 
				five_let_words.append(word5)

	with open(output_data_path5, "w") as f:
		for word5 in five_let_words:
			f.write(word5+ "\n")

	print(f"Found {len(five_let_words)} five letter words")

def main6():
	input_data_path= "wordle_data.txt"
	output_data_path6= "wordle_words6.txt"

	six_let_words= []

	with open(input_data_path, "r") as f:
		for line6 in f.readlines():
			word6= line6.strip() 
			if len(word6)== 6: 
				six_let_words.append(word6)

	with open(output_data_path6, "w") as f:
		for word6 in six_let_words:
			f.write(word6+ "\n")

	print(f"Found {len(six_let_words)} six letter words")

def main7():
	input_data_path= "wordle_data.txt"
	output_data_path7= "wordle_words7.txt"

	seven_let_words= []

	with open(input_data_path, "r") as f:
		for line7 in f.readlines():
			word7= line7.strip() 
			if len(word7)== 7: 
				seven_let_words.append(word7)

	with open(output_data_path7, "w") as f:
		for word7 in seven_let_words:
			f.write(word7+ "\n")

	print(f"Found {len(seven_let_words)} seven letter words")

def main8():
	input_data_path= "wordle_data.txt"
	output_data_path8= "wordle_words8.txt"
	
	eight_let_words= []
	with open(input_data_path, "r") as f:
		for line8 in f.readlines():
			word8= line8.strip() 
			if len(word8)== 8:
				eight_let_words.append(word8)

	with open(output_data_path8, "w") as f:
		for word8 in eight_let_words:
			f.write(word8+ "\n")

	print(f"Found {len(eight_let_words)} eight letter words")

if __name__== "__main__":
	main5()
	main6()
	main7()
	main8()