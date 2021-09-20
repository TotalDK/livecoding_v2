mylist = [1,2,3,4,5]

def rec_sum(mylist):

	if mylist == []:
		return 0

	first_element = mylist[0]
	rest_of_list = mylist[1:]

	return first_element + rec_sum(rest_of_list)

# print(rec_sum(mylist))


# return 1 + 2 + 3 + 4 + 5 + 0 

def rec_mult(mylist):

	if len(mylist) == 0:
		return 1

	first_element = mylist[0]
	rest_of_list = mylist[1:]

	return first_element * rec_mult(rest_of_list)

# return 1 * 2 * 3 * 4 * 5 * 1 
# print(rec_mult(mylist))

mystring = "Hello"
def customLen(mystring):
	
	

	return 

# print(customLen(mystring))
print("This line \n\n\n\n next line")
