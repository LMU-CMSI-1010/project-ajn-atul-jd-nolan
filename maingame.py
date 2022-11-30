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


player = pygame.image.load('gamegraphics/literalbeans.png')
player_rect = player.get_rect(midbottom = (80,625))
dashcooldown = 0

enemy = pygame.image.load('gamegraphics/lilsprite.png')
enemy_rect = enemy.get_rect(bottomright = (1250,600))
enemy_gravity = 0
enemy_dodge_timer = 0



class Player(object):

    def __init__(self, health, agility, slowness):
        self.health = health
        self.agility = agility
        self.gravity = 0
        self.left_inertia = 0
        self.right_inertia = 0
        self.score = 0
        self.slowness = slowness

    def update(self):
        screen.blit(player, player_rect)

    def jump(self):
        if player_rect.bottom == 600:
            self.gravity = -27

    def dashright(self):
        self.left_inertia = dude.agility

    def dashleft(self):
        self.right_inertia = dude.agility

dude = Player(3, 40, 120)



while True:


    for event in pygame.event.get():          # Checks for all possible events.
        if event.type == pygame.QUIT:          # If the window is exited, the game quits.
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:       # Detects key being pressed down and then up, respectively.
            if event.key == pygame.K_w:            # Specific key event.
                dude.jump()
            if event.key == pygame.K_d:
                if dashcooldown == 0:
                    dude.dashright()       
                    dashcooldown = dude.slowness      
                else:
                    pass    
            if event.key == pygame.K_a:
                if dashcooldown == 0:
                    dude.dashleft()       
                    dashcooldown = dude.slowness    
                else:
                    pass 
            # if event.key == pygame.K_SPACE:
            #     Blah blah blah generate bullet or something
        # if event.type == pygame.KEYUP:


    screen.blit(sky, (0,0))
    screen.blit(land, (0,600))           # Block Image Transfer.

    # Our lovely player.
    dude.gravity += 1
    player_rect.y += dude.gravity             # Natural-ish gravity mechanic.

    # Right Dash
    dude.left_inertia -= 1
    if dude.left_inertia < 0:
        dude.left_inertia = 0
    player_rect.right += dude.left_inertia

    # Left Dash
    dude.right_inertia -= 1
    if dude.right_inertia < 0:
        dude.right_inertia = 0
    player_rect.left -= dude.right_inertia    
    
    dashcooldown -= 1
    if dashcooldown < 0:
        dashcooldown = 0
# Score by exiting the screen on the right side
    if player_rect.left > 1500: 
        player_rect.left = -150
        dude.score += 1
    if player_rect.left < -150:
        player_rect.left = 1500
    if player_rect.bottom > 600: player_rect.bottom = 600

    dude.update()
    # Our deplorable enemy.

    # enemy_gravity += 1
    # enemy_rect.y += enemy_gravity
    enemy_rect.left -= 5
    if enemy_rect.left < -150: enemy_rect.left = 1500
    if enemy_rect.bottom > 800: enemy_rect.bottom = 800
    # enemy_dodge_timer += 1
    # if enemy_dodge_timer == 120:
    #     enemy_gravity = -20
    #     enemy_dodge_timer = 0
    screen.blit(enemy,enemy_rect)

    if enemy_rect.colliderect(player_rect):
        if dude.right_inertia != 0 or dude.left_inertia != 0:
            pass
        else:
            dude.health -= 1

            if dude.health == 0:
                print("GAME OVER! FINAL SCORE:", dude.score)
                pygame.quit()
                exit()

    pygame.display.update()
    clock.tick(60)                            # FPS Ceiling - Cannot run faster than 60 FPS.


    '''
    THINGS TO IMPLEMENT:
    - PLAYER CLASS
    - ENEMY CLASS
    - ENEMY BULLETS
    - PLAYER BULLETS

    - IMPLEMENT BACKGROUND
    - FRAME SHIFT WITH PLAYER MOVEMENT - MAKE A DECISION

    - SCORE
    
    - SHIFT TO DIFFERENT GAME STATE AFTER SCORE REACHES A CERTAIN LEVEL, CHANGE SKY COLOR, ETC ETC!
    
    
    '''