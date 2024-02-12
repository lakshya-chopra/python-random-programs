class Dog: #class

    def __init__(self, name, breed, colour, age): #not a constructor, '__new__' is, which is not called explicitily here.

        #Attributes of the object
        self.name = name

        self.breed = breed

        self.colour = colour

        self.age = age

    def print_details(self): #instance method

        print(f'Hi, my name is {self.name}, and I am {self.age} years old')


d1 = Dog('Joey','Labrador','Brown',5)
#calling the constructor (Explicit Call)
#d1 is the reference to the object.

d1.print_details() #calling the instance method

    
