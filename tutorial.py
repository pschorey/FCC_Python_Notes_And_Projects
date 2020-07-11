#Notes from W3 Schools Python3 Lessons.  
#I am comparing them to JS to help with learning

##Learning Comments##
#used for comments. JS //
#Python doesn't exactly have multiline comments...  
#Python uses tripple quotes:
"""
turns a multiline string
into a comment (just don't save it to a variable)
similar to JS using /* */
"""

##LOGGING
print("Hello World") #JS console.log("Hello World")

##VARIABLES
#Python simply assings the variable
x = "Lives in Texas" #notice there is no var, let, or const 
y = 9
#variables can change types
x = 5 #now an int instead of the earlier string
y = 'All my exes' #strings can be declared with single or double quotes
#Like JS variables are case sensitive
#variables can only be alpha-numeric and underscore _

#assign same value to multiple variables
x = y = z = 3.14
#Assign multiple variables at once
x, y, z = 'All', ' my friends', ' drive a low rider!'

#combine variables / strings with + just like JS
print("Derp de derp " + x + y + z)

#All variables created outside a function have a global scope
#local variables (those declared inside a function) can have the same var name as a global, and they will stay different variables
#example of Local and Global variable scope with same names:
x = "awesome"
def myfunc(): #we haven't talked about functions yet, this declares a py func
  x = "fantastic" #indented instead of using braces
  print("I am " + x)
myfunc() #this invokes it
print("I am " + x) #back to the global variable.

#Use keyword 'global' inside a function to declare a global variable instead of local
def myfunc():
  global x #global in scope instead of local
  x = "fantastic"
myfunc()
print("Python is " + x) #no error, global declared in myfunc


##DATA TYPES
"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
"""

#get data type
print(type(x)) #JS console.log(typeof x)
#above prints: <class 'str'>

#PY Data Type Examples (will be explained later...)
"""
x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	 #complex use imaginary j
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview
"""


##NUMBERS
#Int -whole number of unlimited length
#float -mixed number like 3.14, or 5e3 (e= power of ten)
#Complex -numbers are written with a "j" as the imaginary part (TBH, not sure what this means yet)

x = 1;
y = 1.5
#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)


##RANDOM NUMBERS
import random #imports the random module (Unlike JS, you can apparently import other than at the top of your file, probably not a good idea though)
print(random.randrange(1,10))

#Casting, specifying types when declaring variables:
#Casting Ints
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3 -note the string needs to be a whole number
#Casting Floats
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
#Casting Strings
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'


##STRINGS & STRING METHODS
x = 'howdy' 
#or double quotes
x = "howdy"
#three double quotes, or three single quotes makes a multiline string
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#strings are arrays
a = "Sup Dawg!"
print(a[2]) #prints p (zero indexed like JS)
#slicing (b[startIndex (inclusive) : end index(non-inclusive)])
b = "Sup Dawg!"
print(b[4:8]) #prints Dawg [inclusive:exclusive]
#negative indexing (index from the end of the string)
b = "Hello, World!"
print(b[-5:-2]) #prints 'orl' #[position 5 from end inclusive: position 2 from end exclusive]
#String length
a = "Hello, World!"
print(len(a)) #prints 13, JS would be:  a.length
#trim / remove whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!", JS would use a.trim()
#lowercase, removes capital letter
a = "Hello, World!"
print(a.lower()) #prints 'hello, world', JS a.toLowerCase()
#capitalize, all string changed to uppercase
a = "Hello, World!"
print(a.upper()) #prints "HELLO, WORLD!", JS a.toUpperCase()
#replace one string for another, case sensitive
a = "Hello, World!"
print(a.replace("H", "J")) #prints "Jello, World!"
#split
a = "Hello, World!"
b = a.split(",") #string a remains unmodified
print(b) #prints ['Hello', ' World!']
#'in' and 'not in' -similar functionality to .indexOf() -but returns a bool, instead of -1 if false
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x) #prints true
txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt #return true if not present
print(x) #prints false
#concatenation, just like JS, use a +
#!but, unlike JS, can't combine numbers with strings
a = "Hello"
b = "World"
c = a + ' ' + b
print(c)
#format(), print numbers with strings using concat
age = 36
txt = "My name is John, and I am {}" #{} is placeholder
print(txt.format(age)) #age gets formatted inside the braces, prints ";::My name is John, and I am 36"
#format multiple variables, place them in order as params of .format()
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#format with index orders if repeating variables, or want to make sure things are in correct order
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
#escape characters with \ like in JS
txt = "We are the so-called \"Vikings\" from the north."
"""
ESCAPED CHARACTERS IN PY
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ ooo	Octal value	 #be sure to remove the space...
\ xhh	Hex value    #be sure to remove the space...
"""


##******STRING METHODS*****
"""
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case ####LIKE LOWER, BUT CHECKS FOR LETTERS IN LANGUAGES OTHER THAN ENGLISH
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""


##Booleans
#similar to JS, 
'''
The following will return True: 
Almost any value is evaluated to True if it has some sort of content.
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
'''

#isinstance() --similar to checking if typeof === true
x = 200
print(isinstance(x, int)) #true

#operators
#all same as JS except:

x = 15
y = 2
print(x // y) #the floor division // rounds the result down to the nearest whole number
x = 2
y = 5
print(x ** y) #exponent, same as 2*2*2*2*2

'''
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3
'''

'''
Comparison operators.  Doesn't compare type like JS, == but no ===, or >==
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y
'''

#Logical Operators
#and or not #use the words instead of the symbols (&& || !==)

#identity operators
'''
is 	Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object	x is not y
'''

#membershipo operators
'''
in 	Returns True if a sequence with the specified value is present in the object	x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y
'''

##Python Lists
'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
'''

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#This example returns the items from "cherry" and to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) #prints 2nd to the end of the list

#Change an item in the list
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#check if item exists in list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Print the number of items in the list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#Using the append() method to append an item to the end of a list:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#insert at index
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Remove a named item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Remove last item, or at index
thislist = ["apple", "banana", "cherry"]
thislist.pop() #or thislist.pop(1) -removes index 1
print(thislist)

#The del keyword removes the specified index: -similar to .pop
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#del can also delete the entire list
thislist = ["apple", "banana", "cherry"]
del thislist

#The clear() method empties the list:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


####You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
#Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Another way to make a copy is to use the built-in method list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#join two lists
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
#join using a for loop (like pushing for JS)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)
#join using the extend word
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

#List Methods
'''
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''

##Tuples##
#like lists, but they are ordered, and UNCHANGEABLE, like a const, but no values can change in the array
#they are writen with paranthesis instead of braces
thistuple = ("apple", "banana", "cherry")
print(thistuple)


##Sets##
##unordered, and unindexed, but changeable...
##Sets are like array, but they are non-indexed, you can't get values based on position
thisset = {"apple", "banana", "cherry"}
print(thisset)
#To add one item to a set use the add() method.
#To add more than one item to a set use the update() method.
#To remove an item in a set, use the remove(), or the discard() method.

#Set Methods
'''
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
'''


##Dictionaries##
#They seem just like JS Objects, takes a key and value
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#get a value
x = thisdict["model"]
#get a value using .get()
x = thisdict.get("model")

#change value that matches a key
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#print all keys
for x in thisdict:
  print(x)
#print all key values
for x in thisdict:
  print(thisdict[x])
#You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
  print(x)

#Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
  print(x, y)

#Check if key is in dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Print the number of items in the dictionary:
print(len(thisdict))

#Add a key and value
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#The pop() method removes the item with the specified key name: (key needs to be specified)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
#del can also delete the entire dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
#print(thisdict) #this will cause an error because "thisdict" no longer exists.

#The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict) #prints {}

'''
####You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
#Make a copy of a dictionary with the dict() function:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

##Nested Dictionaris
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#Dictionary Constructor
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)

'''
Dictionary Methods
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
'''

##Conditions
a = 33
b = 200
if b > a:
  print("b is greater than a") #notice indentation

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:#JS version of else if
  print("a and b are equal")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#One line if statement:
if a > b: print("a is greater than b")

#one line if else
a = 2
b = 330
print("A") if a > b else print("B")

#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200
if b > a:
  pass

##While Loops
i = 1
while i < 6:
  print(i)
  i += 1

#Break, stops loop even if still true
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
#Continue, stops the current iteration, and immediately goes to the next
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i) # Note that number 3 is missing in the result

#While with an else, after the while finishes the else runs
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


##For loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Break in a loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
	#loop stops as soon as bannana == x
    break
#Continue, ends current iteration jumps to next
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#Range
for x in range(6):
  print(x) #prints 0-5

for x in range(2, 6):
  print(x) #prints 2-5

for x in range(2, 30, 3):
  print(x)  #starts at 2, ends at 30, increment by 3
'''
same as
for (x = 2; x < 30; x += 3) {
	console.log(x)
}
'''

#else, runs after loop finishes
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

for x in [0, 1, 2]:
  pass
# having an empty for loop like this, would raise an error without the pass statement



#Creating functions
def my_function():
  print("Hello from a function")

#calling a function
my_function()

#Passing arguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")  

#Unlike JS, functions can only be called with the number of parameters that are declared in the function

#Unknown number of arguments
#If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#Using keyvalues, allows arguments to be reordered
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#returning a function...
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

##Recursion, works the same as JS
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    text = 'result = {}'
    print(text.format(result))
  else:
    result = 0
    text = 'result = {}'
    print(text.format(result))
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

'''
Recursion Example Results
result = 0
result = 1
result = 3
result = 6
result = 10
result = 15
result = 21
'''

##Lambda functions
#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.
x = lambda a : a + 10
print(x(5))

#using lambdas to make quick custom functions
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

#Use lambda functions when an anonymous function is required for a short period of time.



##Classes & Objects
#create a class
class MyClass:
  x = 5

#create an object
#Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)  

#Create a class with properties and methods.
#self -similar to this in JS, will be first param passed, can be named anything
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#change property of an object
p1.age = 40

#delete object property
#Delete the age property from the p1 object:
del p1.age

#delete a whole object
del p1


#Obj Inheritance
#child objects inherit properties from parent obj (if init like Student below, otherwise it overwrites parent inheritance)
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname) #could have also done Person.__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2020)
x.welcome()


##Iterators
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit)) #apparently first next call it acts as 0
print(next(myit)) #next ups the index each time it's called
print(next(myit))


#To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


##Scope...exactly the same as JS, use global if declaring a global from within a function


##Modules...
'''
similar to JS version of import * from ....

import mymodule

mymodule.greeting("Jonathan")
'''

#naming a module
#You can name the module file whatever you like, but it must have the file extension .py

#renaming a module
#You can create an alias when you import a module, by using the as keyword:

'''
import mymodule as mx

a = mx.person1["age"]
print(a)
'''

#import one var, function, etc. from a module: use 'from'
#from mymodule import person1
#Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]



##Dates
import datetime
x = datetime.datetime.now()
print(x) #2020-07-08 00:00:05.381649

'''
%a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18	
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM	
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
%%	A % character	%
'''



'''
Math Module
math.acos(x)	Returns the arc cosine value of x
math.acosh(x)	Returns the hyperbolic arc cosine of x
math.asin(x)	Returns the arc sine of x
math.asinh(x)	Returns the hyperbolic arc sine of x
math.atan(x)	Returns the arc tangent value of x
math.atan2(y, x)	Returns the arc tangent of y/x in radians
math.atanh(x)	Returns the hyperbolic arctangent value of x
math.ceil(x)	Rounds a number upwards to the nearest integer, and returns the result
math.comb(n, k)	Returns the number of ways to choose k items from n items without repetition and order
math.copysign(x, y)	Returns a float consisting of the value of the first parameter and the sign of the second parameter
math.cos(x)	Returns the cosine of x
math.cosh(x)	Returns the hyperbolic cosine of x
math.degrees(x)	Converts an angle from radians to degrees
math.dist(p, q)	Calculates the euclidean distance between two specified points (p and q), where p and q are the coordinates of that point
math.erf(x)	Returns the error function of x
math.erfc(x)	Returns the complementary error function of x
math.exp(x)	Returns the value of Ex, where E is Euler's number (approximately 2.718281...), and x is the number passed to it
math.expm1(x)	Returns the value of Ex - 1, where E is Euler's number (approximately 2.718281...), and x is the number passed to it
math.fabs(x)	Returns the absolute value of a number
math.factorial()	Returns the factorial of a number
math.floor(x)	Rounds a number downwards to the nearest integer, and returns the result
math.fmod(x, y)	Returns the remainder of specified numbers when a number is divided by another number
math.frexp()	Returns the mantissa and the exponent, of a specified value
math.fsum(iterable)	Returns the sum of all items in an iterable (tuples, arrays, lists, etc.)
math.gamma(x)	Returns the gamma value of x
math.gcd()	Returns the highest value that can divide two integers
math.hypot()	Find the Euclidean distance from the origin for n inputs
math.isclose()	Checks whether two values are close, or not
math.isfinite(x)	Checks whether x is a finite number
math.isinf(x)	Check whether x is a positive or negative infinty
math.isnan(x)	Checks whether x is NaN (not a number)
math.isqrt(n)	Returns the nearest integer square root of n
math.ldexp(x, i)	Returns the expression x * 2i where x is mantissa and i is an exponent
math.lgamma(x)	Returns the log gamma value of x
math.log(x, base)	Returns the natural logarithm of a number, or the logarithm of number to base
math.log10(x)	Returns the base-10 logarithm of x
math.log1p(x)	Returns the natural logarithm of 1+x
math.log2(x)	Returns the base-2 logarithm of x
math.perm(n, k)	Returns the number of ways to choose k items from n items with order and without repetition
math.pow(x, y)	Returns the value of x to the power of y
math.prod(iterable, *, start=1)	Returns the product of an iterable (lists, array, tuples, etc.)
math.radians(x)	Converts a degree value (x) to radians
math.remainder(x, y)	Returns the closest value that can make numerator completely divisible by the denominator
math.sin(x)	Returns the sine of x
math.sinh(x)	Returns the hyperbolic sine of x
math.sqrt(x)	Returns the square root of x
math.tan(x)	Returns the tangent of x
math.tanh(x)	Returns the hyperbolic tangent of x
math.trunc(x)	Returns the truncated integer parts of x

math.e	Returns Euler's number (2.7182...)
math.inf	Returns a floating-point positive infinity
math.nan	Returns a floating-point NaN (Not a Number) value
math.pi	Returns PI (3.1415...)
math.tau	Returns tau (6.2831...)
'''


##JSON
import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

##Convert .py Dict to JSON
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)



##REGEX
import re
#searches for match, return true / false
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")

#find all matches
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#split text using regex
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#find and replace
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


##Opening and reading files
'''
fhand = open('somefile.txt') #fhand var name is short for 'file handler'
for line in fhand:
	line = line.rstrip() #removes new lines, whitespace from right side of line
	if line.startswith('From:') :
		print(line)
'''

##Loop with index
friends = ['bob', 'hank', 'tom']
for i in range(len(friends)) :
	friend = friends[i]
	print('sup ' + friend)	

amigo = 'Paco'
print(amigo[:-1])	

##Get & set value of an object if the key does not exist
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("price", 15000) #if price key not there, it ads it and initializes with value 15000
print(x)

##Two iteration variables
myDict = {'bob':1, 'tom':3, 'fred':5}
for key,val in myDict.items() :
	print(key,val)