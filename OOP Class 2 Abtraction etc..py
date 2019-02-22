# Abstraction - a methodology to hide background information until it is needed.

# Encapsulation - prevents access to methods and variables to prevent them being modified accidentally from outside.

import random
import pygame, sys
from pygame.locals import *
import time

pygame.init()
pygame.display.set_caption("My first PyGame program")
screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

human_image = pygame.image.load("human.png").convert_alpha()
#pygame.transform.scale(human_image, (50, 50))
human_wet_image = pygame.image.load("human_wet.png").convert_alpha()

# ------------------------------------------------------------------

cloud_x = 0
cloud_y = 0

Raindrop_List = []


class Raindrops:
    def __init__(self):
        self.x = cloud_x + random.randint(56, 384)           #random.randint(1, 640)
        self.y = cloud_y + 256
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)
        self.fallspeed = random.randint(1, 4)
        self.size = random.randint(5, 17)

    def draw(self):
        # ((COLOUR R, COLOUR G, COLOUR B), (X POSITION, Y POSITION), RADIUS, BORDER STROKE (inherited from COLOUR))
        pygame.draw.circle(screen, (self.r, self.g, self.b), (self.x, self.y), self.size, 2)

    def move(self):
        self.y += self.fallspeed


class Cloud:
    def __init__(self):
        # Load the cloud image
        self.image = pygame.image.load("cloud.png").convert_alpha()
        self.x = cloud_x
        self.y = cloud_y

    def key_controls(self):
        # State the key module variable.
        pressed_key = pygame.key.get_pressed()
        distance = 4

        # Cloud movement controls
        if pressed_key[pygame.K_DOWN]:
            self.y += distance
            global cloud_y
            cloud_y = self.y
        if pressed_key[pygame.K_UP]:
            self.y -= distance
            cloud_y = self.y
        if pressed_key[pygame.K_RIGHT]:
            self.x += distance
            global cloud_x
            cloud_x = self.x
        if pressed_key[pygame.K_LEFT]:
            self.x -= distance
            cloud_x = self.x

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

class Human:
    def __init__(self):
        # Load the cloud image
        self.x = 10
        self.y = 275

    def draw(self):
        screen.blit(human_image, (self.x, self.y))

    def draw_wet(self):
        screen.blit(human_wet_image, (self.x, self.y))

    def hit_by_raindrop(self, raindrops):
        return pygame.Rect(self.x, self.y, 216, 200).collidepoint((raindrops.x, raindrops.y))


# ------------------------------------------------------------------

# Create cloud
cloud = Cloud()

# Human cloud
human = Human()

t = - 1

# Main game loop (place near the start after initialisation).
game_running = True
while game_running:
    # Draw/'render' the background fill colour. Uses tuple for different colour values.
    screen.fill((0, 100, 100))

    # Detect if time since the last raindrop hit is > 1 second.
    if time.time() - t < 1:
        human.draw_wet()
    else:
        human.draw()



    # Handle all events since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Handle cloud controls
    cloud.key_controls()



    # Draw cloud
    cloud.draw()

    # Draw human
    # human.draw()

    # Append one execution of the 'Raindrops()' method to the 'Raindrop_List' list.
    Raindrop_List.append(Raindrops())

    # For each raindrop in the list,
    # for i in Raindrop_List:
    #     i.draw()
    #     i.move()
    #     # Remove the circle from the list if it reaches the lower screen (since the graphic leaves the while loop, it
    #     # will no longer be drawn).
    #     if i.ypos > 400:
    #         Raindrop_List.remove(i)

    i = 0
    while i < len(Raindrop_List):
        Raindrop_List[i].move()
        Raindrop_List[i].draw()

        # If human rained on
        if human.hit_by_raindrop(Raindrop_List[i]):
            t = time.time()     #human.draw_wet()

        if Raindrop_List[i].y > 600 or human.hit_by_raindrop(Raindrop_List[i]):
            del Raindrop_List[i]
            i -= 1
        i += 1





    # Update code MUST be placed at the bottom of all the 'drawing' functions.
    pygame.display.update()

    # Sets the FPS - by calling Clock.time(60) once per frame, the program is capped at 60 FPS.
    clock.tick(60)
