# Name : Cynthia Wanjiru
# Date : 19/02/2026
# Program to show objects

class Human:
    # First we define the attributes of a human being
    type = "Mammal"
    legs = 2
    brain = True
    Warm_blooded = True
    city = "Nairobi"

    # we then create a constructor for the class object
    # The constructor will be used create copies of this objects
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell_story(self):
        print(f"Hello,I am {self.name} here is a story")
        print("there was once existence of dinosaurs ")

#create the humans
Jenny = Human("Jenny:",28)
Dwayne = Human("Dwayne:",43)

#let the humans created do things
Jenny.tell_story()
print("Jenny's age is:", Jenny.age)

# Modify one of the objects, without modifying other objects 
Dwayne.city = "Kiambu"

print("Dwayne's location:",Dwayne.city)
print("Jenny's location:",Jenny.city)
