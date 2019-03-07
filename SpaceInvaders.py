# Abstraction - a methodology to hide background information until it is needed.

# Encapsulation - prevents access to methods and variables to prevent them being modified accidentally from outside.

import random
import pygame, sys
import time
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Space Invaders 3000")
screen = pygame.display.set_mode((640, 480))
screen_rect = screen.get_rect()
space_bg = pygame.image.load("spacebg.png").convert_alpha()

clock = pygame.time.Clock()

enemyList = []

missileList = []

dustList = []

time_lastSpawn = 0
time_lastShot = 0
time_lastDustSpawn = 0

score = 0
playerLives = 4

targetMiss = 5

# ------------------------------------------------------------------

class Player:
    def __init__(self):
        # Import player ship
        self.image = pygame.image.load("spaceship.png").convert_alpha()
        self.x = 320
        self.y = 360

    def key_controls(self):
        global time_lastShot

        # State the key module variable.
        pressed_key = pygame.key.get_pressed()
        distance = 4

        # Player ship movement controls
        if pressed_key[pygame.K_DOWN]:
            if 430> self.y:
                self.y += distance
        if pressed_key[pygame.K_UP]:
            if 0 < self.y:
                self.y -= distance
        if pressed_key[pygame.K_RIGHT]:
            if 590 > self.x:
                self.x += distance
        if pressed_key[pygame.K_LEFT]:
            if 0 < self.x:
                self.x -= distance

        # Player firing controls
        if pressed_key[pygame.K_SPACE]:
            # Fire missile if reload finished @ 1secs
            if time.time() - time_lastShot >= 0.35:
                missileList.append(Missile())
                time_lastShot = time.time()

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


class Missile:
    def __init__(self):
        self.x = playerShip.x + 25
        self.y = playerShip.y - 8
        self.size = 8

    def move(self):
        # Propel missile
        self.y -= 8

    def draw(self):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.size, 0)


class Enemy:
    def __init__(self):
        # Import enemy image and scale it
        self.image = pygame.transform.scale(pygame.image.load("enemy.png").convert_alpha(), (64, 64))

        self.rect = self.image.get_rect()

        self.x = random.randint(0, 490)
        self.y = random.randint(0, 0)

        # Acceleration
        self.dy = 0

    def move(self):
        # Increase acceleration
        self.y += self.dy
        self.dy += 0.04

    def draw(self):
        pygame.Rect(self.x, self.y, 64, 64)
        screen.blit(self.image, (self.x, self.y))

    # def checkCollision(self, ):
    #     pygame.sprite.spritecollide()

class SpaceDust:
    def __init__(self):
        # Spawn dust
        self.x = random.randint(0, 640)
        self.y = random.randint(0, 0)

        self.size = random.randint(1, 2)

    def move(self):
        self.y += 2

    def draw(self):
        pygame.draw.circle(screen, (180, 180, 180), (self.x, self.y), self.size, 0)

# ------------------------------------------------------------------

# # Draw Player Ship
# screen.blit(player_ship, (320,360))

# Create player
playerShip = Player()

# Main game loop (place near the start after initialisation).
game_running = True
while game_running:
    # Handle all events since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Handle player controls
    playerShip.key_controls()

    # Draw/'render' the background fill colour. Uses tuple for different colour values.
    screen.fill((0, 100, 100))

    # Draw/'render' the background image.
    screen.blit(space_bg, (0, 0))

    # # Clamp player inside screen view
    # playerShip.rect.clamp_ip(screen.rect)

    # Draw player
    playerShip.draw()

    # Create Enemies if timer @ 1secs
    if time.time() - time_lastSpawn >= 1:
        enemyList.append(Enemy())
        time_lastSpawn = time.time()

    # Move enemies
    for i in enemyList:
        i.draw()
        i.move()
        # i.checkCollision()

        # Remove enemy if outside screen
        if i.y > 480:
            enemyList.remove(i)

    for i in missileList:
        i.draw()
        i.move()

        # Remove missile if outside screen
        if i.y < 0:
            missileList.remove(i)

    # if targetMiss == 5:


    # Spawn Space Dust
    if time.time() - time_lastDustSpawn >= 0.15:
        dustList.append(SpaceDust())
        time_lastDustSpawn = time.time()

    # Move space dust
    for i in dustList:
        i.draw()
        i.move()





    # Update code MUST be placed at the bottom of all the 'drawing' functions.
    pygame.display.update()

    # Sets the FPS - by calling Clock.time(60) once per frame, the program is capped at 60 FPS.
    clock.tick(60)
