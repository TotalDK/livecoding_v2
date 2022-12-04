# Write a function called specialmean that takes a positive integer n as input. Given this integer input, 
# calculate the mean value of the following list: [1,2,...,n,2**1,2**2,...,2**n].

# For example, specialmean(5) should return the mean value of the list [1,2,3,4,5,2,4,8,16,32], which is 7.7.
# Hint: To calculate the mean of a list, feel free to use Python's mean() function by adding the following line before your 
# function definition:  from statistics import mean

# If the input is not a positive integer, the function should return 0. 
# Hint: isinstance(n,int) returns True if n is an integer.

from statistics import mean

def specialmean(n):
    if isinstance(n, int):
        if n <= 0:
            return 0
        else:
            simple = [*range(1,n+1)]
            for i in range(1, n+1):
                simple.append(2**i)
            
            me = mean(simple)
            return me
    return 0

#print(specialmean(-1))

def read_csv(filename):
	
	lists = []
	with open(filename, "r") as infile:
		for line in infile:
			lists.append(line.strip().split(","))

	dictionary = {}
	for item in lists[0]:
		dictionary[item]= []

	
	head = lists[0]
	
	for i in range(len(head)):
		for line in lists[1:]:
			dictionary[head[i]].append(line[i])
	return dictionary




