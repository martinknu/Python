

#Errors and exceptions

try:
    print("One divided by Zero")
    total = 1/0
    print("This will not show since exception raised")
    #This will not execute
except Exception:
    total = 0

print(total)    




# Catch user input e.g. a input as a string
num = input("what is a number")

try:
    num = int(num)
except Exception:
    num = "Unknown"

print(num)

