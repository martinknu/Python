#Create your first class


class Animal():
    fur_color = "Orange" 

    animal_type = "Unknown"

    def __init__(self, fur_color):
        print("Fur color is", fur_color)
        self.fur_color = fur_color
    

    def eat(self):
        print("Eating")

    def chase(self):
        print("chasing")

    def speak(self):
        print("Roarrrrr")

    def getFurColor(self):
        print("Fur color is ", self.fur_color)


class Housecat(Animal):

    #__init__ Executed before anything else in this class
    def __init__(self, fur_color):
        super().__init__(fur_color)
        print("Fur color was saved to the class")
        self.animal_type = "Housecat"
        print(self.animal_type)


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


cat = Housecat("Black")
# cat.getFurColor()