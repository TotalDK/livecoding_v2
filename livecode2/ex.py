thelist = [1,2,3,4,5,6,7,8,9]


def sumlist(mylist):

	if len(mylist) == 1:
		return mylist[0]

	return mylist[0] + sumlist(mylist[1:])

def even_odd_count(mylist, odd= 0, even=0):

	if len(mylist) == 0:
		return even, odd

	if mylist[0]%2 == 0:
		return even_odd_count(mylist[1:], odd = odd, even = even + 1)
	else:
		return even_odd_count(mylist[1:], odd = odd + 1, even = even)	


if __name__ == "__main__":

	print("The sum of the list is:",sumlist(thelist))
	print("The count of even and odd is:", even_odd_count(thelist))