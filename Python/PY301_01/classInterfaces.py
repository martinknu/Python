
#Create your first class


class Animal:
    fur_color = "Grey" 
    
    def eat(self):
        print("Eating")

    def chase(self, animal="Gazelle"):
        print("chasing", animal)

    def speak(self):
        raise NotImplementedError #Defines that if overloaded speak method must be implemented


#Housecat inherits / overloads Animal class
#Overwrites speak method
class Housecat(Animal):
    fur_color = "Greyish black"
    
    def speak(self):
        print("Meoooowww")
    
    def eat(self):
        #Wrong way Animal.eat()
        super().eat() # Right way, get the class above and execute eat method
        print("I am eating salmon")

    def chase(self, animal):
        super().chase(animal)
        print("Animal was caught")    

cat = Housecat()
cat.speak()
cat.eat()
cat.chase("baboon")
cat.chase("mouse")