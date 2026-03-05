import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
run = True

class Circle():
    def __init__ (self, radius,color,pos,width,):
        self.radius=radius
        self.color=color
        self.pos=pos
        self.width=width
        self.screen=screen
    
    def Draw(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius, self.width)

    def grow(self,r):
        self.radius += r 
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius, self.width)

circle_filled = Circle(10, "red", (250,250), 0,)
circle_unfilled = Circle(10, "blue", (150,300),7)


while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

        if i.type == pygame.MOUSEBUTTONDOWN:
            screen.fill("yellow")
            circle_filled.Draw()
            circle_unfilled.Draw()
            pygame.display.update()

        elif i.type == pygame.MOUSEBUTTONUP:
            screen.fill("yellow")
            circle_filled.grow(10)
            circle_unfilled.grow(10)
            pygame.display.update()

    




