import pygame
from sys import exit

pygame.init()                                 # Initialize pygame.
SCRWIDTH = 2000
SCRHEIGHT = 800
screen = pygame.display.set_mode((SCRWIDTH, SCRHEIGHT))  # Set bounds of window/display surface.
pygame.display.set_caption('Bean Game') 
clock = pygame.time.Clock()

# Colors
SAND = (156, 117, 82)

# Objects
s_width = 2000
s_height = 200

sky = pygame.Surface((2000, 800)) 
sky.fill("SKYBLUE") 

land = pygame.Surface((s_width, s_height))          # Normal surface.
land.fill(SAND)

test_image = pygame.image.load('gamegraphics/sans.png')
test_image_x = 600

while True:
    for event in pygame.event.get():          # Checks for all possible events.
        if event.type == pygame.QUIT:          # If the window is exited, the game quits.
            pygame.quit()
            exit()

    screen.blit(sky, (0,0))
    screen.blit(land, (0,600))           # Block Image Transfer.
    test_image_x -= 10    
    if test_image_x < -300: test_image_x = 2000                
    screen.blit(test_image, (test_image_x,210))

    pygame.display.update()
    clock.tick(60)                            # FPS Ceiling - Cannot run faster than 60 FPS.

# DISPLAYSURF.fill(WHITE)