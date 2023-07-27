

#input filename an content
filename = input("what is the filename")
content = input("Enter the content")

#Write content to file
with open(filename, "w") as file:
    file.write(content)

#Prompt for read?
openFile = input("Would you like to read this file")
#Check if feedback is either y / n
if openFile in ["y", "n"]:
    if openFile == "y":
        with open(filename, "r") as file:
            print(file.read())




