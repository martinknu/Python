
#Create your first class


class Animal:
    fur_color = "Grey" 
    
    def eat(self):
        print("Eating")

    def chase(self):
        print("chasing")

    def speak(self):
        print("Roarrrrr")


#Tiger inherits / overloads Animal class
#Overwrites speak method
class Tiger(Animal):
    def speak(self):
        print("They are greeeeeaaaaaattttttttt")

#Housecat inherits / overloads Animal class
#Overwrites speak method
class Housecat(Animal):
    fur_color = "Greyish black"
    
    def speak(self):
        print("Meoooowww")
    

# tiger = Animal()
# tiger.eat()
# tiger.speak()

Tiger2 = Tiger()
Tiger2.speak()

cat = Housecat()
cat.speak()
print(cat.fur_color)