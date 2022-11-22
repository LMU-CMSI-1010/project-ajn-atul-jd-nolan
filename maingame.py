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

sans = pygame.image.load('gamegraphics/sans.png').convert_alpha()
sans_x = 600
sans_rect = sans.get_rect(topleft = (80,200))

while True:
    for event in pygame.event.get():          # Checks for all possible events.
        if event.type == pygame.QUIT:          # If the window is exited, the game quits.
            pygame.quit()
            exit()

    screen.blit(sky, (0,0))
    screen.blit(land, (0,600))           # Block Image Transfer.
    # sans_x -= 10    
    # if sans_x < -300: sans_x = 2000                
    # screen.blit(sans, (sans_x, 210))
    sans_rect.left -= 10
    if sans_rect.left < -300: sans_rect.left = 2000
    screen.blit(sans, sans_rect)

    pygame.display.update()
    clock.tick(60)                            # FPS Ceiling - Cannot run faster than 60 FPS.
 