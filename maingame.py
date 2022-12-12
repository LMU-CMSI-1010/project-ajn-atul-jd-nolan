'''
UNTITLED BEAN GAME, or "FRIJOLE FIASCO!"

This file serves as the main hub for the project. The full game can be accessed using only this code, 
with of course, our gamegraphics folder for the assets and images.

FUNCTION/CLASS GLOSSARY CAN BE FOUND AT THE BOTTOM.
'''


'''
THE FOUNDATION.
'''
import pygame
from sys import exit

pygame.init()                                 # Initialize pygame.
SCRWIDTH = 1200
SCRHEIGHT = 700
L_BORDER = -50
R_BORDER = 1000
FLOOR = 650
screen = pygame.display.set_mode((SCRWIDTH, SCRHEIGHT))  # Set bounds of window/display surface.
pygame.display.set_caption('Frijole Fiasco!') 
clock = pygame.time.Clock()

# Colors
SAND = (156, 117, 82)
PASTELGREEN = (61, 204, 85)
PASTELRED = (222, 69, 58)

# Objects
bluesky = pygame.Surface((SCRWIDTH, SCRHEIGHT)) 
bluesky.fill("SKYBLUE") 
toolbar = pygame.Surface((200, SCRHEIGHT))
toolbar.fill("WHITE")

font = pygame.font.SysFont("Consolas", 40, False, False)
titlefont = pygame.font.SysFont("Consolas", 60, False, False)

land = pygame.Surface((SCRWIDTH, SCRHEIGHT))          # Normal surface.
land.fill(SAND)

player = pygame.image.load('gamegraphics/hero.png')
playerscaled = pygame.transform.scale(player, (75,100))
# player_rect = playerscaled.get_rect(midbottom = (80,950))
dashcooldown = 0

enemy = pygame.image.load('gamegraphics/enemy1.png')
enemy1scaled = pygame.transform.scale(enemy, (50,100))
enemy_rect = enemy1scaled.get_rect(midbottom = (800,1000))
enemy_gravity = 0
enemy_dodge_timer = 0

dash_ability = pygame.image.load('gamegraphics/dashsymbol.png')
dash_icon = pygame.transform.scale(dash_ability, (100, 100))
dash_rect = dash_icon.get_rect(topleft = (1050,50))

'''
THE CLASSES.

PLAYER CLASS: A character to be controlled by the player. Has abilities such as dash and jump. No attacking
capabilities, just dodging. 

ENEMY CLASS: A non-controllable enemy, set to move across the screen and jump at seemingly random intervals.

WORLD CLASS: A programmable object that sets the background and terrain however the programmer would like it, 
using an array of lists contained within each instance.
'''
class Player(object):

    def __init__(self, agility, slowness, x, y, image):
        self.agility = agility
        self.gravity = 0
        self.left_inertia = 0
        self.right_inertia = 0
        self.x = x
        self.y = y
        self.image = image
        self.rect = image.get_rect(midbottom = (self.x,self.y))
        self.score = 0
        self.slowness = slowness
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):

        dude.gravity += 1
        dude.rect.y += dude.gravity             # Natural-ish gravity mechanic.

        # Right Dash.
        dude.left_inertia -= 1
        if dude.left_inertia < 0:
            dude.left_inertia = 0
        dude.rect.right += dude.left_inertia

        # Left Dash.
        dude.right_inertia -= 1
        if dude.right_inertia < 0:
            dude.right_inertia = 0
        dude.rect.left -= dude.right_inertia  

        # Score by exiting the screen on the right side.
        if dude.rect.left > R_BORDER: 
            dude.rect.left = L_BORDER
            dude.score += 1
        if dude.rect.left < L_BORDER:
            dude.rect.left = R_BORDER
            dude.score -= 1
        if dude.rect.bottom > FLOOR: 
            dude.rect.bottom = FLOOR
        screen.blit(self.image, self.rect)
        
        dx = 0
        dy = 0

        # # code atul is adding to check for collision
        for tile in world.tile_list:
            #check for collision in x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            #check for collision in y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                #check if below the ground i.e. jumping
                if self.gravity < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.gravity = 0
                #check if above the ground i.e. falling
                elif self.gravity >= 0:
                    dy = tile[1].top - self.rect.bottom
                    self.gravity = 0

        self.rect.x += dx
        self.rect.y += dy

    def jump(self):
        # if self.rect.bottom == 650:
            self.gravity = -20

    def dashright(self):
        self.left_inertia = dude.agility

    def dashleft(self):
        self.right_inertia = dude.agility


class Enemy1(object):

    def __init__(self, slowness, init_speed, x, y, image):
        self.slowness = slowness
        self.gravity = 0
        self.speed = init_speed
        self.x = x
        self.y = y
        self.image = image
        self.rect = image.get_rect(midbottom = (self.x,self.y))
        self.dodge_timer = 0

    def update(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.left < L_BORDER: 
            self.rect.left = R_BORDER
        if self.rect.bottom > FLOOR: 
            self.rect.bottom = FLOOR
            self.dodge_timer += 1
        if self.dodge_timer == 120:
            # self.gravity = -20
            self.jump()
            self.dodge_timer = 0
        screen.blit(self.image, self.rect)

    def jump(self):
        self.gravity = -20

'''
THE WORLD, by ATUL.
'''
# ATUL'S WORK START
tile_size = 50

#load images
sn_img = pygame.image.load('gamegraphics/moon.png')
sun_img = pygame.transform.scale(sn_img, (50, 50))
b_img = pygame.image.load('gamegraphics/sky.png')
bg_img = pygame.transform.scale(b_img, (1000, 700))

def draw_grid():
    for line in range(0, 20):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (SCRWIDTH, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, SCRHEIGHT))

class World():
    def __init__(self, data):
        self.tile_list = []

        # load image of dirt
        dit_img = pygame.image.load("gamegraphics/dirt.png")
        dirt_img = pygame.transform.scale(dit_img, (50, 50))

        # load image of grass
        gras_img = pygame.image.load("gamegraphics/grass.png")
        grass_img = pygame.transform.scale(gras_img, (50, 50))

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                    # if img_rect.colliderect(dude.rect):
                    #     dude.rect.left
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

world_data = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
]

world = World(world_data)

# ATUL'S WORK END

'''
THE GAME(STATES), by NOLAN.
'''
gamestate = "startscreen"

while gamestate == "startscreen":

    screen.blit(bluesky, (-200,0))
    screen.blit(land, (0,600))
    world.draw()
    screen.blit(toolbar, (1000,0))

    welcometext = font.render("WELCOME TO:", True, (255,255,255))
    screen.blit(welcometext, (100,150))

    titletext = titlefont.render("BEAN THING!", True, (255,255,255))
    screen.blit(titletext, (100,185))

    parenthesestext = font.render("(working title)", True, (255,255,255))
    screen.blit(parenthesestext, (100,250))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:          # If the window is exited, the game quits.
            pygame.quit()
            exit()

        x,y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and 0<x<1000 and 0<y<800:
            gamestate = "play"

    pygame.display.update()
    clock.tick(60)    

dude = Player(20, 80, 80, 650, playerscaled)
villain = Enemy1(120, 5, 800, 650, enemy1scaled)

while gamestate == "play":

    screen.blit(bg_img, (0, 0))
    screen.blit(sun_img, (100, 100))
    world.draw()
    # draw_grid()

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

    # Different levels/Speeds
    if dude.score < 3:
        villain.rect.left -= villain.speed

    elif dude.score >= 3:
        villain.rect.left -= villain.speed + 5

    # pygame.draw.rect(screen, (255,0,0), dude.rect) #(UN-COMMENT TO ACCESS HITBOXES)
    # pygame.draw.rect(screen, (255,0,0), enemy_rect)
    dude.update()
    villain.update()

    screen.blit(toolbar, (1000,0))

    # Score
    scoretext = font.render(f"SCORE:{dude.score}", True, (0,0,0))
    screen.blit(scoretext, (1015, 600))

    dashcooldown -= 1
    if dashcooldown < 0:
        dashcooldown = 0
    if dashcooldown == 0:
        screen.blit(dash_icon,dash_rect)

    if villain.rect.colliderect(dude.rect):
        # if dude.right_inertia != 0 or dude.left_inertia != 0:  # Collision 
        #     pass
        # else:
            gamestate = "gameover"

    pygame.display.update()
    clock.tick(60)                            # FPS Ceiling - Cannot run faster than 60 FPS.



while gamestate == "gameover":

    restartbutton = pygame.Surface((500, SCRHEIGHT)) 
    restartbutton.fill(PASTELGREEN) 
    screen.blit(restartbutton, (0,0))

    exitbutton = pygame.Surface((500, SCRHEIGHT))
    exitbutton.fill(PASTELRED)
    screen.blit(exitbutton, (500,0))

    finalscoretext = font.render(f"FINAL SCORE:{dude.score}", True, (0,0,0))
    screen.blit(finalscoretext, (90,200))

    restarttext = titlefont.render("RESTART?", True, (255,255,255))
    screen.blit(restarttext, (100,600))

    quittext = titlefont.render("QUIT?", True, (255,255,255))
    screen.blit(quittext, (650,600))

    screen.blit(enemy, (625,50))

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:          # If the window is exited, the game quits.
            pygame.quit()
            exit()

        x,y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 0<x<500 and 0<y<800:
                dude.score = 0
                gamestate = "play"

            if 500<x<1000 and 0<y<800:
                pygame.quit()
                exit()

    pygame.display.update()
    clock.tick(60) 


    '''
    THE GLOSSARY.



    '''
