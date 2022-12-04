import pygame
from sys import exit

pygame.init()                                 # Initialize pygame.
SCRWIDTH = 1500
SCRHEIGHT = 800
screen = pygame.display.set_mode((SCRWIDTH, SCRHEIGHT))  # Set bounds of window/display surface.
pygame.display.set_caption('Bean Game') 
clock = pygame.time.Clock()

# Colors
SAND = (156, 117, 82)

# Objects
s_width = 1500
s_height = 200

bluesky = pygame.Surface((s_width, 800)) 
bluesky.fill("SKYBLUE") 

redsky = pygame.Surface((s_width, 800))
redsky.fill("RED")

land = pygame.Surface((s_width, s_height))          # Normal surface.
land.fill(SAND)


player = pygame.image.load('gamegraphics/literalbeans.png')
playerscaled = pygame.transform.scale(player, (400,500))
player_rect = player.get_rect(midbottom = (80,625))
dashcooldown = 0

enemy = pygame.image.load('gamegraphics/enemy1.png')
enemy1scaled = pygame.transform.scale(enemy, (150,250))
enemy_rect = enemy1scaled.get_rect(midbottom = (1250,600))
enemy_gravity = 0
enemy_dodge_timer = 0

dash_ability = pygame.image.load('gamegraphics/dashsymbol.png')
dash_icon = pygame.transform.scale(dash_ability, (200, 200))
dash_rect = dash_icon.get_rect(topleft = (50,600))



class Player(object):

    def __init__(self, agility, slowness):
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


class Enemy(object):

    def __init__(self, slowness, init_speed):
        self.slowness = slowness
        self.gravity = 0
        self.speed = init_speed

    def update(self):
        screen.blit(enemy1scaled, enemy_rect)

    def jump(self):
        self.gravity = -10

gamestate = "startscreen"

dude = Player(40, 60)
villain = Enemy(120, 5)

while gamestate == "startscreen":
    screen.blit(bluesky, (0,0))
    screen.blit(land, (0,600))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:          # If the window is exited, the game quits.
            pygame.quit()
            exit()

        x,y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and 0<x<1500 and 0<y<800:
            gamestate == "play"



while gamestate == "play":

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
        # if event.type == pygame.KEYUP:


    if dude.score < 5:
        screen.blit(bluesky, (0,0))
        enemy_rect.left -= villain.speed

    elif dude.score >= 5 and dude.score < 10:
        screen.blit(redsky, (0,0))
        enemy_rect.left -= villain.speed + 5

    screen.blit(land, (0,600))           # Block Image Transfer.

    # pygame.draw.rect(screen, (255,0,0), player_rect) #(ACCESS HITBOXES)
    # pygame.draw.rect(screen, (255,0,0), enemy_rect)

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

    if dashcooldown == 0:
        screen.blit(dash_icon,dash_rect).inflate(0.5,0.5)


    # Our deplorable enemy.

    enemy_gravity += 1
    enemy_rect.y += enemy_gravity

    if enemy_rect.left < -150: 
        enemy_rect.left = 1500
    if enemy_rect.bottom > 600: 
        enemy_rect.bottom = 600
    enemy_dodge_timer += 1
    if enemy_dodge_timer == 120:
        enemy_gravity = -20
        villain.jump()
        enemy_dodge_timer = 0
    villain.update()

    if enemy_rect.colliderect(player_rect):
        # if dude.right_inertia != 0 or dude.left_inertia != 0:
        #     pass
        # else:
            print("GAME OVER! FINAL SCORE:", dude.score)
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)                            # FPS Ceiling - Cannot run faster than 60 FPS.


    '''
    THINGS TO IMPLEMENT:
    - ENEMY CLASS
    - ENEMY BULLETS
    - PLAYER BULLETS

    - HEALTH SYSTEM + GAME OVER SCREEN

    - IMPLEMENT BACKGROUND
    - FRAME SHIFT WITH PLAYER MOVEMENT - MAKE A DECISION

    - SCORE

    - SHIFT TO DIFFERENT GAME STATE AFTER SCORE REACHES A CERTAIN LEVEL, CHANGE SKY COLOR, ETC ETC!
    
    
    '''