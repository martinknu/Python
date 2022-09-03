
# TODO : Todo code comment 

from ast import Pass
from stringprep import in_table_a1
from unicodedata import name


none = None
booleans = False # or True
string = "text" # can use both "" and ´´
integers = 99 #Python can handle underscores in numbers e.g. 1_000_000
floats = 3.14
list = ["item1", "item2", floats]
tuples = ("cat", "dog", "zebra") # Cant be changed
sets = {"item1", "item2", "item2", "item3"} #Does not maintain its order
dictionaries = {
    "key1": "Dictionary value1",
    "key2": "Dictionary value2",
    "key3": "Dictionary value3",
}

#Simple print function
print("Hello world")

#Print string in UPPER case 
print(string.upper())

#Print list
print(list)

#More advanced print, printing Na. x times
print("Na" * integers)


# Multiply *
# Power of **
# Moudulus %

# Int
myInt01 = 1
myInt02 = 3
myInt03 = myInt01 + myInt02
print("The result is : ",  myInt03)

# String 
course = "python 101 course"
print(course )

if myInt01 == 1 :
    # pass : used if no code
    print("myInt is 1")
    if myInt01 == 1 :
        print("Indent again")


if myInt01 == 2 :
    print("myInt is 2")    

# -------------------- Lists ----------------------

#Append list
list.append("Martin")
list.append("Henrik")

#Remove from list
list.remove("Martin")

#Pop out
list.pop()

#For loop with list
for item in list:
    print("The item is:", item)


# -------------------- Dictionarys ----------------------
#Print one key from dictionary
print(dictionaries["key1"])

# Adding new item to dictionary
dictionaries["NewKey"] = "Istedvej"
print(dictionaries)



# -------------------- Touple ----------------------
# Touple is immutable = Not changeable

print(tuples)
# print(type.tuples())

for animals in tuples :
    print(animals)


# -------------------- Sets ---------------------- 
#Values in sets are unique
print(sets)

# -------------------- Booleans ---------------------- 

canCode = True 

if canCode == True :
    print("You can code")

if canCode :
    print("You can code 2")


# -------------------- None ---------------------- 
wallet = None 

if wallet == None :
    print("There is nothing in my wallet")

wallet = 82.5 

if wallet != None :
    print("There is ", wallet, "In my wallet")


# -------------------- Indexing and slicing ---------------------- 

lst = ["one","two","three", "four","five"]
#      0 1 2 3 4

print(lst[2])
print(lst[2:4])
print(lst[2::])
print(lst[-1])
print(lst[-2])
print(lst[-2::])


str = "Python 101"
print(str[2])
print(str[2::])


# -------------------- Input ---------------------- 
#Input will always return as string 
age = input("What is your age? ")
dogYears = int(age) * 7
print(dogYears)


# -------------------- casting ---------------------- 
dataType = type(age)
print(dataType )

# age = int(age)

groceryList = ["apples", "Bananas", "pineapple", "Bananas"]

groceryList = set(groceryList)
groceryListTouple = tuple(groceryList)


print(groceryList)
print(type(groceryList))


print(groceryListTouple)
print(type(groceryListTouple))


# -------------------- formatting ---------------------- 

myName = "Martin"
welcomeMessage = f"Hello {myName} welcome to Python"
print(welcomeMessage)


# -------------------- Comparison operators ---------------------- 

if canCode == True:
    # pass
    print("You can code")
else:    
    print("You can not code")


teacher = input("What is your name?")
Food = ""

# =! not operator
# >
# >=
# <
# <=


if teacher.lower() == "kalob": 
    print("You are not a teacher")
    Food = "Pizza"
elif teacher.lower() == "martin":
    print("You are not a teacher")
    Food = "Tacho"    
else:
    print("You are not Kalob")
    Food = "Salmon"
print(f"You are eating {Food}")



# -------------------- Comparison shortcuts ---------------------- 
emptyString = ""
someString = "ss"


if not emptyString :
    print("Empty string returns false ")


# -------------------- Multiple comparison operators ---------------------- 

if int(age) > 18 and teacher.lower() == "kalob" :
    print("You can drink alcohol")
else:
    print(f"You are not Kalob or not old enough, Age{age}, {myName} ")


# -------------------- For loops ---------------------- 
favFoods = ["pizza","tachos","salad","chicken"]
favFoods = set(favFoods)

for food in favFoods:
    print(f"My fav food is {food}")
    # size = input("What size would you like")
    # print(f"You ordered a {size} pizza")
    for letter in food:
        print(letter)


# -------------------- Loop trough dictionary ---------------------- 

person = {
"name": "Martin",
"age": "41",
"heigth": "180",
"weigth": "89",
}

for key, value in person.items():
    print(f"The key is {key} and the value is {value}")



# -------------------- While loop ---------------------- 

iL1 = 0

while iL1 < 100 :
    print(iL1 )
    iL1 = iL1 + 1 



# -------------------- Break and continue ---------------------- 

items = ["one","two","three","four"]

#Continue
for item in items :
    if item == "two" or item == "four":
        continue 
    print(item)

#Break
for item in items :
    if item == "three":
        break 
    print(item)


#Print odd numbers with modulus
iL1 = 0
while iL1 <= 20 :
    iL1 = iL1 + 1 
    if iL1 % 2 == 0:
        continue
    print(iL1 )


#Break at specific number
iL1 = 0
while iL1 <= 1_000_000 :
    iL1 = iL1 + 1 
    if iL1 == 13:
        break
    print(iL1 )


# -------------------- Functions ---------------------- 

#Function definition
def myFunc(name=None, food="Burgers"):

    if name.lower() == "martin":
        print(f"Hello {name}")
    print(f"Hello function {name}, lets eat some {food}")
    return f"Done for {name}"

myFunc("Martin", food="Tachos")
myFunc("Tanja", "Soup")
myFunc("Victor", "Pizza")
myFunc("Oliver", "Bananas")



#Basic exp calculator
def exp(num1, num2):
    total = num1 ** num2
    return total

bigNumber = exp(2,2)
print(bigNumber)
