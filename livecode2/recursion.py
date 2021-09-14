mylist = [1,2,3,4,5]
# indices 0,1,2,3,4

i = 0

mylistsmall = mylist[1:] #[2,3,4,5]

def rec_print(mylist):

	if len(mylist) == 0:
		return None
	else:
		first_element = mylist[0]
		print(first_element)
		rest_of_list = mylist[1:]
		rec_print(rest_of_list)
		return None

mylist = [1,2,3,4,5]
# i: 0 1 2 3 4
def rec_print2(mylist, i=0):

	if i >= len(mylist): # 5 and up
		return None

	print(mylist[i])
	next_i = i + 1
	rec_print2(mylist, next_i)




rec_print2(mylist) #rec_print2(mylist, 0)
# rec_print2(mylist, 1)
# rec_print2(mylist=mylist, i = 1)

















