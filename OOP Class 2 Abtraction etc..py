# Abstraction - a methodology to hide background information until it is needed.

# Encapsulation - prevents access

import random
import pygame, sys
from pygame.locals import *

pygame.init()
pygame.display.set_caption("My first PyGame program")
screen = pygame.display.set_mode((640,480))
cloud_image = pygame.image.load("cloud.png").convert_alpha()                      # Load the image

# ------------------------------------------------------------------

Raindrop_List = []


class Raindrops:
    def __init__(self):
        self.xpos = random.randint(1, 640)
        self.ypos = 0
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)

    def draw(self):
        pygame.draw.circle(screen, (self.r, self.g, self.b), (self.xpos, self.ypos), 20, 2)  # COLOUR, X Y POSITION, RADIUS, BORDER STROKE (inherited from COLOUR)

    def move(self):
        self.ypos += 1


# xpos = random.randint(1, 640)
# ypos = random.randint(1, 480)
clock = pygame.time.Clock()

while 1:                                                    # Place the while loop near the start after initialisation
    clock.tick(60)                                          # Sets the FPS - by calling Clock.time(60) once per frame, the program is capped at 60 FPS.

    screen.fill((0, 100, 100))                              # 'Renders' the background fill. Tuple with different colour values
    Raindrop_List.append(Raindrops())
    for i in Raindrop_List:
        i.move()
        i.draw()
        if i.ypos > 380:
            Raindrop_List.remove(i)
    # pygame.draw.circle(screen,(255,130,130),(xpos,ypos),20,2)   # COLOUR, X Y POSITION, RADIUS, BORDER STROKE (inherited from COLOUR)

    # pressed_key = pygame.key.get_pressed()

    #ypos += 1

    # if pressed_key[K_RIGHT]:
    #     xpos += 1
    # if pressed_key[K_LEFT]:
    #     xpos -= 1
    # if pressed_key[K_UP]:
    #     ypos -= 1
    # if pressed_key[K_DOWN]:
    #     ypos += 1



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(cloud_image, (50,50))

    pygame.display.update()                                     # Update MUST be placed at the bottom of all the 'drawing' functions.