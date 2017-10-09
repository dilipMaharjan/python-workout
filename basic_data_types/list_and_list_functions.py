
# indicates arrays but called list in python
myArray=["apple",1,2,"ball"]

# print first value
print myArray[0]

myArray[2]="replced 2"

#update the value at specified position
print myArray

# delete item at index 2
del myArray[2]
 # del myArray

# printing list after deleting gives error
# NameError: name 'myArray' is not defined
print myArray

newArray=['a','b','c']

# combies two list together
print myArray + newArray

# prints number of items in the array
print len(myArray)

# prints the samllest item in list
print min(myArray)

# prints largest item in list
print max(myArray)

# appends item to existing list
myArray.append("2")

# counts number of item passed in the argument
print myArray.count("2")
