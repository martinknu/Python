
# Keywoard arguments are passed into function as dictionary


def person(**kwargs):
    print(kwargs)
    print(type(kwargs))

    if "age" in kwargs:
        print("You are :", kwargs.get("age"))

person(name="Martin", age=41, brain="Huge")


def order_pizza(name, address, **toppings):
    print("order is for", {name})
    print("deliver it to ", {address})
    
    print("The KWARGS type is :", type(toppings))
    
    price = 15.00

    for key, value in toppings.items():
        price = price + 2.00 
    print("the total is: ", {price})
    return price

total_price = order_pizza("Martin", "Istedvej 19", Pepperoni=True, Cheesee=True)
print(total_price)