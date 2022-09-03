
#Create your first class


class Animal:
    property_1 = "Something" #This is a property
    property_2 = {
        "key1" : "value 1",
        "key2" : "value 2",
        "key3" : "value 3"
    }
    the_list = ["Lem","Moe","Bitten","Stefano"]


    _private_property = 1 #Private property
    
    def method1(self):
        print(f"From method:",self.property_1)

    @property    
    def method2(self):
        return self.the_list[2]

    def add_name(self, name):
        self.the_list.append(name)
        return self.the_list

    def remove_name(self, name):
        self.the_list.remove(name)
        return self.the_list



animal1 = Animal()

print(animal1.property_1)
print(animal1.property_2["key1"])


animal1.method1()

gully = animal1.method2
print("The cutest cat of all time is ", gully)

animal1.add_name("Pluto")
print(animal1.the_list)

animal1.remove_name("Lem")
print(animal1.the_list)