import pygame

pygame.init()
pygame.display.set_caption("Text Class")
screen = pygame.display.set_mode((640, 480))
screen_rect = screen.get_rect()
pygame.font.get_fonts()
# font = pygame.font.Font(None, 20)
font = pygame.font.SysFont("arial", 20)             # Load into the 'Setup' section


clock = pygame.time.Clock()
score = 0

# Main game loop (place near the start after initialisation).
game_running = True
while game_running:
    # Handle all events since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((100, 100, 100))

    screen.blit(font.render("Score: " + str(score), True, (0, 255, 0)), (5, 5))

    pygame.draw.rect(screen, (0, 255, 0), (524, 16, 100, 16))

    # Update code MUST be placed at the bottom of all the 'drawing' functions.
    pygame.display.flip()

# Sets the FPS - by calling Clock.time(60) once per frame, the program is capped at 60 FPS.
clock.tick(60)