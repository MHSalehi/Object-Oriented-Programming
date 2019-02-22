# Abstraction - a methodology to hide background information until it is needed.

# Encapsulation - prevents access to methods and variables to prevent them being modified accidentally from outside.

import random
import pygame, sys
from pygame.locals import *

pygame.init()
pygame.display.set_caption("My first PyGame program")
screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

# ------------------------------------------------------------------

Raindrop_List = []


class Raindrops:
    def __init__(self):
        self.xpos = random.randint(1, 640)
        self.ypos = 0
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)
        self.fallspeed = random.randint(1, 4)
        self.size = random.randint(5, 17)

    def draw(self):
        # ((COLOUR R, COLOUR G, COLOUR B), (X POSITION, Y POSITION), RADIUS, BORDER STROKE (inherited from COLOUR))
        pygame.draw.circle(screen, (self.r, self.g, self.b), (self.xpos, self.ypos), self.size, 2)

    def move(self):
        self.ypos += self.fallspeed


class Clouds:
    def __init__(self):
        # Load the cloud image
        self.image = pygame.image.load("cloud.png").convert_alpha()
        self.x = 50
        self.y = 50

    def key_controls(self):
        # State the key module variable.
        pressed_key = pygame.key.get_pressed()
        distance = 4

        # Cloud movement controls
        if pressed_key[pygame.K_DOWN]:
            self.y += distance
        if pressed_key[pygame.K_UP]:
            self.y -= distance
        if pressed_key[pygame.K_RIGHT]:
            self.x += distance
        if pressed_key[pygame.K_LEFT]:
            self.x -= distance

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


# ------------------------------------------------------------------

# Import human image
human_image = pygame.image.load("human.png").convert_alpha()

# Create cloud
cloud = Clouds()

# Main game loop (place near the start after initialisation).
game_running = True
while game_running:
    # Handle all events since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Handle cloud controls
    cloud.key_controls()

    # Draw/'render' the background fill colour. Uses tuple for different colour values.
    screen.fill((0, 100, 100))

    # Append one execution of the 'Raindrops()' method to the 'Raindrop_List' list.
    Raindrop_List.append(Raindrops())

    # For each raindrop in the list,
    for i in Raindrop_List:
        i.draw()
        i.move()
        # Remove the circle from the list if it reaches the lower screen (since the graphic leaves the while loop, it
        # will no longer be drawn).
        if i.ypos > 400:
            Raindrop_List.remove(i)

    # Draw human image
    screen.blit(human_image, (10, 275))

    # Draw cloud
    cloud.draw(screen)

    # Update code MUST be placed at the bottom of all the 'drawing' functions.
    pygame.display.update()

    # Sets the FPS - by calling Clock.time(60) once per frame, the program is capped at 60 FPS.
    clock.tick(60)
