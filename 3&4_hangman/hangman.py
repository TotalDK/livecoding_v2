## Choose a word
## Choose no. wrong guesses allowed
## Show current word as _
## Input from user
## Check whether input is 1 long
## (Save guessed letter)
## Check whether character is in the word
## Show word with guessed letters and _
## Check if completely guessed

#TODO:
# (Prevent guessing same letter more than once)
# (Allow guessing of whole word)
# (Take a custom txt of words)
# - (Have a default list of words if no txt)

#Finishing touches:
# Clean up code
# - Remove unnecessary lines/sections
# - Using printstr feels clunky - Revamp
# - Check if win feels clunky - Revamp


def reveal_letters(word, guessed):
	returnstr = ""
	for letter in word:
		if letter in guessed:
			returnstr += f" {letter}"
		else:
			returnstr += " _"
	return returnstr



def main():
	word = "aeroplane"
	max_wrong = 9
	guessed = set()

	print(" _"*len(word))
	
	printstr = "_"
	while "_" in printstr and max_wrong > 0:
		guess = "__"
		while len(guess) != 1:
			guess = input("Guess a letter: ")
		guessed.add(guess)
		
		if guess in word:
			print(f"Great guess! '{guess}' is in the word!")
		else:
			max_wrong -= 1
			print(f"Wrong! You have {max_wrong} chances left!")
		
		printstr = reveal_letters(word, guessed)
		print(printstr)



	#print(guessed)



if __name__ == "__main__":
	main()