import pygame, sys 
from pygame.locals import *


pygame.init()
PURPLE = (255,0,255)
BLACK = (0,0,0)
YELLOW = (50,255,0)
RED = (255,0,0)
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("My first PyGame program")


def drawHouse(x, y, width, height, screen, colour):
    points = [(x,y- ((2/3.0) * height)), (x,y), (x+width,y), (x+width,y-(2/3.0) * height), 
        (x,y- ((2/3.0) * height)), (x + width/2.0,y-height), (x+width,y-(2/3.0)*height)]
    lineThickness = 2
    #### The False is that I choose NOT to join the first and last point of the list with a line
    pygame.draw.lines(screen, colour, False, points, lineThickness)

def drawPolygon(x,y,screen,colour):
	points = [(x,y), (x+100,y-100), (x+200, y-100), (x+300, y), (x+150, y+300)]
	lineThickness = 3
	pygame.draw.polygon(screen, colour, points, lineThickness)

#### If you want to draw both with fill and stroke one way is to draw two shapes one on top of the 
#### other, one with a fill and the other with a stroke
def drawfilledRectangle(x,y,screen,colour):
	 
	pygame.draw.rect(screen, colour, (x, y, 100,150), 3)
	pygame.draw.rect(screen, PURPLE, (x, y, 100,150), 0)

xpos = 50


while 1:
	
	clock.tick(40)
	#### EXITING PART
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	pressed_key = pygame.key.get_pressed()

	if pressed_key[K_RIGHT]:
		xpos += 1

	#### DRAWING PART (The order is: what is written first gets drawn first)
	#### screen.fill(colour) should be first since it is the background and 
	#### the display.update() last. Change the position of the shapes in the code so that
	#### they overlap (or add motion to all and move them when the app runs). Then change 
	#### the order you draw them/order you write them in the main loop and see what happens 
	
	screen.fill((0,255,255))

	pygame.draw.circle(screen, (255,0,0), (xpos,50), 10)
	pygame.draw.ellipse(screen, (0,45,35), (50,50,100,200))
	drawHouse(100,400,200,200,screen,BLACK)
	drawfilledRectangle(xpos,300,screen,BLACK)
	drawPolygon(300,150,screen,YELLOW)
	
	
	pygame.display.update()