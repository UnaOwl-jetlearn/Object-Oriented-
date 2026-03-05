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

# ring settings
ring_width = 10
ring_radius = 60

blue_circle   = Circle(ring_radius, "blue",  (120,180), ring_width)
black_circle  = Circle(ring_radius, "black", (250,180), ring_width)
red_circle    = Circle(ring_radius, "red",   (380,180), ring_width)
yellow_circle = Circle(ring_radius, "yellow",(185,240), ring_width)
green_circle  = Circle(ring_radius, "green", (315,240), ring_width)

while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

    screen.fill("white")

   
    yellow_circle.Draw()
    green_circle.Draw()
    blue_circle.Draw()
    red_circle.Draw()
    black_circle.Draw()

    pygame.display.update()