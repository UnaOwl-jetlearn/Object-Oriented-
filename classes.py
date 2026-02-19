class Dog():
    tail = 1
    eyes  = 2
    ears = 2
    can_run = True
    is_animal = True
    legs = 4

    def plays(self):
        print("plays with something toy,other dog, human...")
    
    def walks(self):
        print("Moves using legs")

labrador = Dog()
bull_dog = Dog()
husky = Dog()

print("Labrador has this amount of tails:", labrador.tail)
print("is Bull Dog animal?", bull_dog.is_animal)
print("How many legs does a Husky have?", husky.legs)

labrador.plays()
husky.walks()

