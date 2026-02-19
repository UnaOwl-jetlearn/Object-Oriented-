class Pencil():
    can_write = True
    material = "wood"
    eraseable = True
    light = True
    easy_use = True
    small = True

    def draw(self):
        print("Can draw with a pencil.")

    def write(self):
        print("Can write with a pencil.")
    
red_pencil = Pencil()
simple_pencil = Pencil()

print("Can a red pencil draw?")
red_pencil.draw()
print("Is a simple pencil easy to use?", simple_pencil.easy_use)