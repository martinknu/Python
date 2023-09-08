

#------------ in operator checks if variable is included in list---------------

names = ["martin","tanja","victor","oliver"]

myName = "martin"

if myName in names :
    print("Your name is in the list")
else:
    print("Your name is not in the list")


#------------ in operator in dictionary---------------

key = "name"

person = {
    "name": "martin",
    "profession": "coder",
}

if key in person:
    print("name is a valid key")


#------------ in operator in set---------------

sets = {"martin","tanja","victor","oliver"}

if myName in sets:
    print("can also be used in sets")


#------------ not operator---------------

myThing = True

if not myThing :
    print("Statement is true")
else:
    print("Statement is false")

# myName = "astro"
if myName not in sets:
    print(f"{myName} is not in the club")
else:
    print(f"{myName} is in the club")    



#------------ read files---------------

#File open within with statement
with open("myFile.txt" , "r") as file:
    content = file.read()


print("The content is", content)


#------------ create files---------------

with open("writeFile.txt" , "w") as file:
    file.write("Hello from python 202")


#------------ append to files---------------

with open("writeFile.txt" , "a") as file:
    file.write("\n\tAppended text 1")
    file.write("\n\tAppended text 2")


#------------ read multiple lines in .txt document---------------
with open("emails.txt" , "r") as elist:
    emails = elist.readlines()

for email in emails:
    # print(email.rstrip())
    if "@hotmail" in email.rstrip():
        print("Found hotmail account")
        print(email)



