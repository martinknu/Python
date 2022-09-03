

def thing1(name):
    print("Welcome to thing 1", name)
   
    #Thing 2 looks for "name" outside its own scope when not 
    #Existing in own scope
    def thing2():
        print("Welcome to thing 2", name)
    thing2()

thing1("Martin")