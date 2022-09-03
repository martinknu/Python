

from functools import total_ordering


num = input("Enter a number")
num2 = input("Enter a second number")
try:
    num = int(num)
    num2 = int(num2)
    total = num / num2

except ValueError:
    print(num, "Was not a valid number")

except ZeroDivisionError:
    print("Numbers could not be divided")

except Exception as e:
    print("Exception was caught")
    print(type(e))
    num = "unknown"
    
print(num)