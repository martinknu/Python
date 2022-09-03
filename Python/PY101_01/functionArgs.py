# def thing(name, *args , **kwargs):
# args passes into function as tuple


from audioop import add
from inspect import ArgSpec


def addnumbers(*args):
    total = 0
    print(args )
    print(type(args))

    for num in args:
        total = total + num

    return total



print(addnumbers(1,2,3,4,5))

