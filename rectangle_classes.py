import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
run = True

class Rectangle():
    def __init__ (self, radius,color,dimensions,width,):
        self.radius=radius
        self.color=color
        self.dimensions = dimensions
        self.width=width
        self.screen=screen
    
    
    def Draw(self):
        pygame.draw.rect(self.screen, self.color, self.dimensions, self.radius, self.width)

while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    rectangle_orange = Rectangle(10,"orange", (100,100, 100,100), 10)
    rectangle_orange.Draw()

    rectangle_green = Rectangle(15, "green", (300,250, 200,100), 3)
    rectangle_green.Draw()
    pygame.display.update()
        