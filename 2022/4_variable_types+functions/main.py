
print("What is a variable")
# variable
## types:
#	int
# 	float
# 	bool
# 	string
# 	list
# 	set
#	tuple
# 	range

int_name = 10
print(f'{int_name=}, type={type(int_name)}')

float_name = 10.5
print(f'{float_name=}, type={type(float_name)}')

bool_name = True
print(f'{bool_name=}, type={type(bool_name)}')

string_name = "hello"
string_name = 'hello'
print(f'{string_name=}, type={type(string_name)}')

## container ##
# variable, list, tuple, set. Something that can store a value.

list_name = []
list_name = list()
print(f'{list_name=}, type={type(list_name)}')
my_list = [1,2,3,"hello",1.1]
print(my_list)

print()

# exercise 1.2 from week 4 - we want to print the value and type of datalist.
print("exercise 1.2 from week 4")
# shortcut: comment all marked lines -> cmd shift 7
# shortcut: mark multiple variables with same name: mark word + cmd d
datalist= [1452, 11.12, 1+2j, True, 'python', (0,-1), [5,12]]
for item in datalist:
	print(item, type(item))
# 
my_list = [4,5,6]
# change 5 to be a 10
my_list[1] = 10
print(my_list)

# what is a set?
print("what is a set?")
set_name = set()
print(f'{set_name=}, type={type(set_name)}')
my_list = [1,1.1,2,5,5,6]
# a set should return the unique values
my_set = set(my_list)
my_list_from_a_set = list(my_set)
print(my_list_from_a_set)

print()
# what is a tuple
print("what is a tuple")
tuple_name = ()
tuple_name = tuple()
print(f'{tuple_name=}, type={type(tuple_name)}')
x1 = (1,2)
# lets change 2 to be a 3
# x1[1] = 3 # not possible
# Lets inspect index=1 of (”emma”, 200)
my_tuple = ("emma", 200)
print(my_tuple[1])

# function
print()
print('functions:')

def name_of_function():
	print('hello inside function')

name_of_function()

# parameter
def add_one_to_x(input_x):
	return input_x+1

output_1 = add_one_to_x(input_x=2) # expected output: 3
output_2 = add_one_to_x(input_x=4) # expected output: 5
print(output_1)
print(output_2)

# function to add elements of a list
# when a function see a return, it stops and return whatever the return states at that point
print("function to add elements of a list")
def sum_my_list(some_list):
	sum_variable = 0
	for value in some_list:
		sum_variable = sum_variable + value # same as -> sum_variable += value
	return sum_variable

my_list = [4,5,6]
output_1 = sum_my_list(some_list=my_list) # same as: sum(my_list)
print(output_1)

def add_three_things(thing_1, thing_2, thing_3):
	return thing_1 + thing_2 + thing_3

print()

# loops

# for loop

print(list(range(5)))

for i in range(5): # list(range(5)) = [0,1,2,3,4]
	print(i)

my_list = [4,5,6]
for i in my_list:
	print(i)

# for variable in iterable:
# 	# do something
# 	pass

# iterable:
	# list 
	# set 
	# tuple
	# string

print()
for i in set([1,1,2]):
	print(i)

print()
for i in (1,1,2):
	print(i)

print()
new_var = "hello world hello".split(' ')
for i in new_var:
	print(i)


# while loop
# iterates until some condition is met
x = 4
c = 0
while x == 4:
	print(f'{c}: in while loop')
	c += 1
	if c == 1000000:
		x = 2

c = 0
while True:
	print(f'{c}: in while loop')
	c += 1
	if c == 1000000:
		break

c = 0
keep_running = True
while keep_running: # same as: while keep_running == True:
	print(f'{c}: in while loop')
	c += 1
	if c == 1000000:
		keep_running = False

x = 4
c = 0
while x: # same as: while bool(x) == True
	print(f'{c}: in while loop')
	c += 1
	if c == 1000000:
		x = 0
