

# Recursion tasks from Lecture 4
# exercise 04

# factorial
def factorial(n):
	if n == 1: # n * n-1 * n-2 ... n=1
		return 1
	return n * factorial(n-1)

# custom length
vowel_count = 0		# could also be written as
consonant_count = 0 # consonant_count, vowel_count = 0,0

def custom_length(word):
	# assumption: word doesn't cotain spaces or special signs
	if word == '':
		return 0

	global vowel_count
	global consonant_count

	vowels = list('aeiouy')

	if word[0] in vowels:
		vowel_count += 1
	else:
		consonant_count += 1
	
	return 1 + custom_length(word[1:])


# palindrome
def is_palindrome(word):
	if len(word) <= 1:
		return True
	if word[0] == word[-1]:
		return is_palindrome(word[1:-1])
	return False

if __name__ == '__main__':
	# fact = factorial(3) 
	# print(fact) # -> 120

	length = custom_length('hey')
	print(length) # 3
	print(f"{vowel_count=}")
	print(f"{consonant_count=}")

	# is_it = is_palindrome("racecar")
	# print(is_it)
