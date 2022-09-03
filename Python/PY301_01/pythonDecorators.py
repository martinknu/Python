
#Decorator
#Normally used to extend the original function without changing it


def my_decorator(func):
    def wrapper():
        print("Do something here")
        func()
        print("Original function is finished")
    return wrapper


@my_decorator
def myFunc():
    print("myFunction")



myFunc()