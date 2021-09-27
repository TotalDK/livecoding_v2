## Choose a word
## Choose no. wrong guesses allowed
## Show current word as _
## Input from user
## Check whether input is 1 long
## (Save guessed letter)
## Check whether character is in the word
## Show word with guessed letters and _
## Check if completely guessed
## (Prevent guessing same letter more than once)
## (Allow guessing of whole word)
## (Winning message)
## Check if loss
## (Loss mesage)

#TODO:
# (Take a custom txt of words)
# - (Have a default list of words if no txt)

#Finishing touches:
# Clean up code
# - Remove unnecessary lines/sections
# - Using printstr feels clunky - Revamp
# - Check if win feels clunky - Revamp

#Left as an exercise:
# Check guess.isaplha()
# Make sure upper-/lowercase is handled


import random

def reveal_letters(word, guessed):
	returnstr = ""
	for letter in word:
		if letter in guessed:
			returnstr += f" {letter}"
		else:
			returnstr += " _"
	return returnstr

def is_valid_guess(guess, guessed, word):
	if not guess.isalpha():
		print(f"The guess '{guess}' is not alpha!")
		return False
	if guess == word:
		return True
	if len(guess) != 1:
		print(f"The guess '{guess}' is not a single letter!")
		return False
	if guess in guessed:
		print(f"The letter '{guess}' has already been guessed!")
		return False
	return True

def has_won(guess, word, printstr):
	return (guess == word or (not "_" in printstr))

def has_lost(max_wrong):
	return max_wrong <= 0

def load_wordlist(fname):
	wordlist = []
	with open(fname, "r") as infile:
		for line in infile:
			wordlist.append(line.strip())
	return wordlist

def main():
	wordlist = load_wordlist("hangman_words.txt")
	word = random.choice(wordlist)
	max_wrong = 9
	guessed = set()

	print(" _"*len(word))
	
	printstr = "_"
	guess = "_"
	while not has_won(guess, word, printstr) and not has_lost(max_wrong):
		guess = input("Guess a letter: ")
		while not is_valid_guess(guess, guessed, word):
			guess = input("Try again: ")


		if len(guess) == 1:
			guessed.add(guess)
			
			if guess in word:
				print(f"Great guess! '{guess}' is in the word!")
			else:
				max_wrong -= 1
				print(f"Wrong! You have {max_wrong} chances left!")
		
		
		printstr = reveal_letters(word, guessed)
		
		if has_won(guess, word, printstr):
			print(f"Congratulations, you win! The word was:\n{word}")
		elif has_lost(max_wrong):
			print(f"Congratulations, you lost! The word was:\n{word}")
		else:
			print(printstr)



	#print(guessed)



if __name__ == "__main__":
	main()