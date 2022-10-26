#hello

# dict: way to store info 
my_dict= {"idsp": ["name1", "name2"], "dsrbs": ["name3", "name4"]}
my_students = {"Altea": ["Italian", "22", "CPH", "whatever"], "julia": ["poland", "19", "hvi", "tha"], 0: "zero", 0.3: "bu", 5: {0: "zero", 0.3: "bu"}}




# seeing what happens if I assign two values or more to one key
#test = {"altea": "pretty", "smart", "humble"}
#print(test)
# looking at what a set looks like
#the= set(["emma", "emma", "julai"])
#print(the)

#indexing the dictionary at specific keys
#print(my_dict["idsp"])
#print(my_students[0])

#indexing the first value of the list of values of altea
# print(my_students["Altea"][0])

# finding the values at position 1 of all the keys in the dictionary.
# for key in my_students.keys():
#     print(my_students[key][1])

# # adding a new key,val to the dict
# my_students["florentina"]= ["yes"]
# print(my_students)



# new_one = {"altea": {"nationality":["italian", "danish"], "age":22, "where":"cph"}, "julia": {"nationality":"poland", "age":19, "where":"hvi"}}

# # finding the nationallity value of a specific key, .items() returns two values, so the for loop needs two variables. 
# for key, value in new_one.items():
#     print(key,value["nationality"])

# # trying to find the second nationality 
# print(new_one["altea"]["nationality"][1])


#Exercise 1


myPet = {}

myPet["name"] = "Spot"
myPet["animal"] = "dog"
myPet["age"] = 4
myPet["snacks"] = ["sausages","peanutbutter", "droppedpopcorn"]

#print(myPet)


#exercise 2
inventory = {
'gold' : 500,
'pouch' : ['flint', 'twine', 'gemstone'],
'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']}

# for key, value in inventory.items():
#     print(key,value)
inventory["pocket"] = ["youeru"]
#inventory["pocket"] = inventory["pocket"]+["seashells", "lint"] # adding more values to an existing list
inventory["pocket"] = ["seashells", "lint"]
print(inventory["backpack"])

inventory["backpack"].sort()

print(inventory["backpack"])
print(inventory)









