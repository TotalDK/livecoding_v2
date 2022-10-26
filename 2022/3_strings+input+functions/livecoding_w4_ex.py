
import random

def guessing_game(low,high):
	
	print(f'Guess a value between {low} and {high}')

	x = random.randint(low,high)
	count = 0
	guess_list = list() # []
	guess_limit = 10

	while True:
		
		count += 1
		
		guess = int(input(f"Guess #{count}: Previous guess: {guess_list}, What is your guess?\n"))
		
		if guess > high or guess < low:
			print('Guess is outside of the range')
		
		guess_list.append(guess)
		
		if guess != x:
	
			if count == guess_limit:
				print('Maximum number of guesses reached')
				break
		
		else: # guess == x
			print("Well guessed!")
			break


guessing_game(low=5,high=10)















