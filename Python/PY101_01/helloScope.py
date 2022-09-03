from tokenize import Name
from unicodedata import name

name = "Tanja"

#name is scoped in function and different from name 
#scoped outside function
def myFunc():
    name = "Martin"
    return name

print(myFunc())
print(name)