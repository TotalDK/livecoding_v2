import numpy as np

a = np.array([1,2,3])

print(a, "\t\t\t\tnumpy array not inside list") #Makes into string using __str__; like str(a)
print([a], "\t\tnumpy array inside list") #Still makes list into string with __str__, but objects inside the list (in this case a) into strings using __repr__


print("\n\n")

class Shape1():
	def __init__(self, s):
		self.s = s #Number of sides

triangle1 = Shape1(3)

print(triangle1)
print([triangle1])
print()

class Shape2():
	def __init__(self, s):
		self.s = s #Number of sides

	def __str__(self):
		return f"<Shape2 with {self.s} sides>"

triangle2 = Shape2(3)
print(triangle2)
print([triangle2])
print()


class Shape3():
	def __init__(self, s):
		self.s = s #Number of sides

	def __str__(self): #If not defined, defaults to __repr__
		return f"<(str) Shape2 with {self.s} sides>"

	def __repr__(self):
		return f"<(repr) Shape2 with {self.s} sides>"

triangle3 = Shape3(3)
print(triangle3)
print([triangle3])