import random
# Never import something other places than here




# Simple python program:
# - "Hello World!"
# - Run script from terminal
# - Run script from Sublime
# - Ask for name: input()
# - Print "Hello, $name"


# print("Hello World!")
# userinput = input("What is your name?\n")
# print("Hello,", userinput)




# Good Python style:
# - If name main: main() #A way of telling other programmers "this is a script and meant to be run"
# - Global variables
# - One script imports the other and overwrites a global variable

#print(__name__)



# Function basics:
# - Arguments (keyword and default arguments?)
# - Local variables
# - Return statements
# - Calling functions within functions


def main():
	# print("This is main()")
	# hello_name(age=22, name="Simon")
	# hello_name("Johan")
	# hello_name()
	# hello_name()
	a = returnfunction("Simon", 22)
	print(2+a)

def hello_name(name="Unnamed person", age=0):
	print("Hello,", name, "you are", age, "years old!")

def returnfunction(name, age):
	print("Start")
	#print(2+2)
	return 2+2
	print("End")

def add(a,b):
	return "Yea, go fish"

if __name__ == "__main__":
	main()







