# import sys
# print(sys.version)


"""
#-------------------------------------------------------
###Variables
#-------------------------------------------------------

##Creating Variables, Casting a Variable & Get the Type of a Variable
#------------------------------

# x = 5
x = 5.78
# x = "SKM"
print("x is [", x,"] & it's type is [", type(x), "]")

y = str(x)
# y = int(x)
# y = float(x)
print("y is [", y,"] & it's type is [", type(y), "]")


##Legal variable names:
#------------------------------

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

##Multi Words Variable Names
#------------------------------

Camel Case ->  myVariableName = "John"
Pascal Case -> MyVariableName = "John"
Snake Case ->  my_variable_name = "John"

##Assign Multiple Values
#------------------------------

x, y, z = "Orange", "Banana", "Cherry"

##One Value to Multiple Variables
#------------------------------

x = y = z = "Orange"

##Unpack a Collection
#------------------------------

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

##Output Variables
#------------------------------

print(3 ,"7") # 3 7
print(3 + 7) #10
# print(3 + "7") #TypeError: unsupported operand type(s) for +: 'int' and 'str'

##Global Variables
#------------------------------
x = "awesome" #global variables
def myfunc():
#   x = "fantastic" #local variables
  global x
  x = "fantastic" #becomes global variables
  print("Python is " + x)
myfunc()
print("Python is " + x)



#-------------------------------------------------------
###Data Types
#-------------------------------------------------------

## Built-in Data Types
#------------------------------

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType


## Setting the Data Type
#------------------------------

x = "Hello World"	#str	
x = 20	#int	
x = 20.5	#float	
x = 1j	#complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	#bool	
x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
x = None	#NoneType
print(type(x))


## Setting the Specific Data Type
#------------------------------

x = str("Hello World")	
x = int(20)		
x = float(20.5)		
x = complex(1j)		
x = list(("apple", "banana", "cherry"))		
x = tuple(("apple", "banana", "cherry"))		
x = range(6)		
x = dict(name="John", age=36)		
x = set(("apple", "banana", "cherry"))		
x = frozenset(("apple", "banana", "cherry"))		
x = bool(5)		
x = bytes(5)		
x = bytearray(5)	
x = memoryview(bytes(5))	
print(type(x))


## Python Numbers
#------------------------------
x = 1
y = 35656222554887711
z = -3255522
print(type(x), type(y), type(z))

x = 1.10
y = 1.0
z = -35.59
print(type(x), type(y), type(z))

x = 35e3
y = 12E4
z = -87.7e100
print(type(x), type(y), type(z))

x = 3+5j
y = 5j
z = -5j
print(type(x), type(y), type(z))

# Note: We cannot convert complex numbers into another number type.

## Random Number
#------------------------------

import random # random module

# print(random.random()) # between 0-1 number only
# print(random.randrange(1, 1000000000)) # int number only
# print(random.uniform(1, 10)) # float number only



#-------------------------------------------------------
###Strings
#-------------------------------------------------------

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


## Strings are Arrays
#------------------------------
a = "Hello, World!"
print(a[1])

## Looping Through a String
#------------------------------

for x in a:
  print(x)

print(len(a)) #String Length


## Check String
#------------------------------ 

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
print("expensive" not in txt)


## Slicing Strings
#------------------------------ 
b = "Hello, World!"
print(b[2:5]) # start point index - 2 &  end point index - 5  
print(b[:5]) # start point index - 0 &  end point index - 5  
print(b[2:]) # start point index - 2 &  end point index - end
print(b[-5:-2]) # From: "o" in "World!" (position -5) - To, but not included: "d" in "World!" (position -2):

## Modify Strings
#------------------------------ 
a = "  Hello, World!  "
print(a.upper())
print(a.lower())
print(a.strip()) #removes any whitespace from the beginning or the end

## Replace Strings
#------------------------------ 

a = "Hello, World!"
print(a.replace("H", "J"))

## Split Strings
#------------------------------ 

print(a.split(",")) # returns ['Hello', ' World!']

## String Concatenation
#------------------------------ 

a = "Hello"
b = "World"
c = a + b
print(c)

## Format - Strings [f-strings]
#------------------------------ 
price = 36
txt = f"My name is John, I am {price}"    #A placeholder can contain variables, operations, functions, and modifiers to format the value.
print(txt)
txt2 = f"The price is {price:.2f} dollars"  #A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals
print(txt2)
txt3 = f"The price is {price * 3} dollars" 
print(txt3)

#-------------------------------------------------------
###Booleans
#-------------------------------------------------------
# print(10 > 9, 10 == 9, 10 < 9)
# print(bool(-1), bool(10.9), bool("Hello"))
# print(bool(False), bool(None), bool(0), bool(""), bool(()), bool([]), bool({}))
# x = 200
# print(isinstance(x, int))

#-------------------------------------------------------
###Operators
#-------------------------------------------------------

x = 5	
# x += 3 #8
# x -= 3 #2	
# x *= 3 #15	
# x /= 3	#1.67
# x %= 3	#1.67
# x //= 3	#1	
# x **= 3	#125	
# x &= 3	#1
# x |= 3	#7
# x ^= 3	#6
# x >>= 3		#0
# x <<= 3	#40
print(x)

#-----------------------------------------------------------------------------------------------------------------------------
#Note
Python Collections (Arrays)
There are four collection data types in the Python programming language:

1 - LIST is a collection which is ordered and changeable. Allows duplicate members.
2 - TUPLE is a collection which is ordered and unchangeable. Allows duplicate members.
3 - SET is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
4 - DICTIONARY is a collection which is ordered** and changeable. No duplicate members.
#-----------------------------------------------------------------------------------------------------------------------------



#-------------------------------------------------------
###Lists
#-------------------------------------------------------

thislist = ["apple", "cherry", "apple", True, 2, 3.55, 20j]
# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
print(len(thislist))
print(type(thislist))
print(thislist[4])
print(thislist[-3]) #Negative Indexing
print(thislist[2:5]) #Range of Indexes - The search will start at index 2 (included) and end at index 5 (not included).
print(thislist[:4]) #index 4 (not included)
print(thislist[2:])
print(thislist[-4:-1]) #index -1 (not included)

if "apple" in thislist: #check if item exists
  print("Yes, 'apple' is in the fruits list")

thislist[2] = "blackcurrant" #Change Item Value
print(thislist)

thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist[1:2] = ["34", "45"]
print(thislist)

thislist.insert(5, 99.99) #insert a list item at a specified index
print(thislist)

thislist.append("orange") #add an item to the end of the list
print(thislist)

tropical = list(("mango", False)) 
thislist.extend(tropical)  #append elements from another list to the current list
print(thislist)

thistuple = (24e3j, "mango")
thislist.extend(thistuple) #Add elements of a tuple to a list
print(thislist)


thislist.remove("mango") #Remove the first occurance of "mango"
print(thislist)

thislist.pop() #Remove the last item
print(thislist)

thislist.pop(1) #Remove the mentioned index item
print(thislist)

del thislist[0] #Remove the mentioned index item
print(thislist)

# thislist.clear() #Clear the list content
# print(thislist)

# del thislist #Delete the entire list:
# print(thislist)


thislist = ["apple", "banana", "cherry"]
## For Loop Through a List
#------------------------------ 
# for x in thislist:
#   print(x)

## For Loop Through a List
#------------------------------ 
# for i in range(len(thislist)):
#   print(thislist[i])

## While Loop
#------------------------------ 
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

## Looping Using List Comprehension  
#------------------------------ 
# [List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.]
#Syntax  -  newlist = [expression for item in iterable if condition == True]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

#With no if statement
[print(x) for x in fruits] 

#Without list comprehension
newlist1 = []
for x in fruits:
  if "a" in x:
    newlist1.append(x)
print(newlist1)

#With list comprehension
newlist2 = [x for x in fruits if "a" in x]
print(newlist2)

newlist3 = [x if x != "banana" else "orange" for x in fruits] #Return "orange" instead of "banana"
print(newlist3)


## Sort Lists
#------------------------------ 
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

# thislist.sort() #Sort the list alphabetically
# print(thislist)

thislist.sort(reverse = True) #Sort the list descending
print(thislist)


thislist.reverse() # Reverse the order of the list items:
print(thislist)



#Sort the list based on how close the number is to 50:
thisnumlist = [100, 50, 65, 82, 23]
def myfunc(n):
  return abs(n - 50)

thisnumlist.sort(key = myfunc)
print(thisnumlist)


## Copy Lists
#------------------------------ 
thislist = ["apple", "banana", "cherry"]
mylist = thislist
print(mylist)
mylist1 = thislist.copy() # Make a copy of a list with the copy() method:
print(mylist1)
mylist2 = list(thislist) #Make a copy of a list with the list() method:
print(mylist2)


## Join Lists
#------------------------------ 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = [True, 2e3j, 3.757]

join_list = list1 + list2 + list3
print(join_list)


# Append list1, list2, list3 into join_list using append():
join_list = []
for x,y,z in zip(list1,list2,list3):
  join_list.append(x)
  join_list.append(y)
  join_list.append(z)

print(join_list)

list1.extend(list2) #Use the extend() method to add list2 at the end of list1:
print(list1)


#-------------------------------------------------------
###Tuples
#-------------------------------------------------------
#Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets.

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple)) #Print the number of items in the tuple

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


#Access Tuple Items
#------------------------------
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[1])
print(thistuple[-1])
print(thistuple[1:5])
print(thistuple[-7:-3])
print(thistuple[:5])
print(thistuple[5:])

#Change Tuple Values
#------------------------------
# Convert the tuple into a list to be able to change the value in it:
x = ("apple", "banana", "cherry")
y = list(x) #convert into a list:
y[1] = "kiwi"
y.append("orange") #add "orange" in list mode
z = ("melon",) #Create a new tuple with the value "melon",
y += z #add that tuple with old tuple:
y.remove("apple") #remove "apple" from list
print(y)
x = tuple(y) #convert it back into a tuple:
# del x   #The del keyword can delete the tuple completely:
print(x)


#Unpack Tuples
#------------------------------
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple: fruits = ("apple", "banana", "cherry")

#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking": (green, yellow, red) = fruits

#Unpacking a tuple:
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


#Using Asterisk[*] Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#Loop Tuples
#------------------------------
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
for x in fruits:
  print(x)

for i in range(len(fruits)):
  print(fruits[i])

while i < len(fruits):
  print(fruits[i])
  i = i + 1


#Join Tuples
#------------------------------
#Join two tuples:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2 
print(tuple3)

# Multiply the fruits tuple by 2:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple) #('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')


#-------------------------------------------------------
###Sets
#-------------------------------------------------------
#A set is a collection which is unordered, unchangeable*, and unindexed, but you can remove items and add new items.
#Duplicates Not Allowed
#------------------------------

thisset = {"apple", "banana", "cherry"}
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# Duplicate values will be ignored:
#[True and 1] & [False and 0] is considered the same value and are treated as duplicates:
#------------------------------

thisset = {"apple", "banana", "cherry", "apple", True, 1, 2, False, 0}
print(thisset)
print(len(thisset)) #Get the number of items in a set And ignore the duplicate value count

#Set Items - Data Types
#------------------------------
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}


print(type(set1))
print(type(set2))
print(type(set3))
print(type(set4))


#Access Set Items
#------------------------------
#You cannot access items in a set by referring to an index or a key.
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Check if "banana" is present in the set:
print("banana" in thisset) 

# Check if "mango" is NOT present in the set:
print("mango" not in thisset)

#Add an item to a set, using the add() method:
thisset.add("orange")
print(thisset)


#Add Sets
#------------------------------
# To add items from another set into the current set, use the update() method.
#it can be any iterable object (tuples, lists, dictionaries etc.).

thisset = {"apple", "banana", "cherry"}
thislist = [1, 2, 3.45]
thistuple = [True, 3e2j, False]

tropical = {"pineapple", "mango", "papaya"}

tropical.update(thisset) #Add elements from thisset into tropical
tropical.update(thislist) #Add elements from thislist into tropical
tropical.update(thistuple) #Add elements from thistuple into tropical
print(tropical)

#Remove "banana" by using the remove() method & [Note: If the item to remove does not exist, remove() will raise an error].
tropical.remove("banana")
print(tropical)

# Remove "444" by using the discard() method & [Note: If the item to remove does not exist, discard() will NOT raise an error.]
tropical.discard(444)
print(tropical)

#Remove a random item by using the pop() method:
x = tropical.pop()
print(x)
print(tropical)

# The clear() method empties the set:
tropical.clear()
print(tropical)

# The del keyword will delete the set completely:
del tropical
print(tropical)


#Loop Sets
#------------------------------
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Join Sets
#------------------------------

#Union - The union() method returns a new set with all items from both sets && also with other data types, like lists or tuples. It will exclude any duplicate items.
set1 = {"a", "b", "c"}
set2 = {0, 1, 2e4j, 3.87}
set3 = {"John", True, False}

join_set1 = set1.union(set2, set3)
print(join_set1)

#Use | to join two sets & allows only to join sets with sets 
join_set2 = set1 | set2 | set3 
print(join_set2)

set4 = ("apple", "bananas", "cherry") #Join a set with a tuple
join_set3 = join_set1.union(set4) 
print(join_set3)


#Update - The update() method inserts all items from one set into another. It changes the original set, and does not return a new set. It will exclude any duplicate items.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


#Intersection -  The intersection() method will return a new set, that only contains the items that are present in both sets. [Keep ONLY the duplicates]
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

#Join set1 and set2, but keep only the duplicates:
set3 = set1.intersection(set2) 
print(set3)

#use the & operator instead of the intersection() method, and allows only to join sets with sets.
set3 = set1 & set2
print(set3)

#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1.intersection_update(set2)
print(set1)

# Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:
set11 = {"apple", 1,  "banana", 0, "cherry"}
set22 = {False, "google", 1, "apple", 2, True}

set33 = set11.intersection(set22)
print(set33)

#Difference - The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

set11 = {"apple", 1,  "banana", 0, "cherry"}
set22 = {False, "google", 1, "apple", 2, True}

set33 = set11.difference(set22)
print(set33)
set44 = set22 - set11 #You can use the - operator instead of the difference() method, and allows only to join sets with sets.
print(set44)

#The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2) 
print(set1)

#The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
set4 = set1 ^ set2 #You can use the ^ operator instead of the symmetric_difference() method, and allows only to join sets with sets.
print(set4)

#The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)




#-------------------------------------------------------
###Dictionaries
#-------------------------------------------------------

#Dictionaries are used to store data values in key:value pairs with curly brackets,. 
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"],
  "electric": False,
}
# thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
print(thisdict["colors"]) #Print the "brand" value of the dictionary:
print(len(thisdict)) #Print the number of items in the dictionary:
print(type(thisdict)) #Print the data type of a dictionary:


#Access Dictionary Items
#------------------------------
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"],
  "electric": False,
}

x = car["model"]
print(x)
yx = car.get("electric") #Get the value of the "electric" key using get()
print(yx) 

#Get Keys
x_key = car.keys() #Get a list of the keys:
print(x_key) 
car["fuel_type"] = "Petrol" #Add a new item to the original dictionary
print(x_key) 

#Get Values
x_value = car.values() #Get a list of the values:
print(x_value) 
car["colors"] = "red" #change the value of an key
print(x_value)
car["series"] = "GT500" #Add a new item to the original dictionary
print(x_value)

#Get Items
x_items = car.items()
print(x_items)

#Check if Key Exists
if "model" in car:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


#Add/Update/Remove Dictionary Items
#------------------------------
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"],
  "electric": False,
}
car["series"] = "GT500" #Add a new item to the original dictionary
car.update({"fuel_type": "Petrol"}) #Add item to the dictionary by using the update() method with key:value pairs.

car["colors"] = "red" #Update the value of an key
car.update({"year": 2020}) #Update value by using the update() method with key:value pairs.
print(car)

car.pop("model") #The pop() method removes the item with the specified key name:
print(car)

car.popitem() #The popitem() method removes the last inserted item
print(car)

car.clear() #The clear() method empties the dictionary:
print(car)

del car
print(car) #The del keyword removes the item with the specified key name:

"""

#Loop Dictionaries
#------------------------------
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"],
  "electric": False,
}


for x in car:
  print(x) #Print all key names in the dictionary, one by one:
  # print(car[x]) 

