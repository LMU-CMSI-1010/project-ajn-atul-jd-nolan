import pygame
from sys import exit

pygame.init()                                 # Initialize pygame.
SCRWIDTH = 1200
SCRHEIGHT = 1000
L_BORDER = -50
R_BORDER = 1000
FLOOR = 950
screen = pygame.display.set_mode((SCRWIDTH, SCRHEIGHT))  # Set bounds of window/display surface.
pygame.display.set_caption('Frijole Fiasco!') 
clock = pygame.time.Clock()

# Colors
SAND = (156, 117, 82)

# Objects
bluesky = pygame.Surface((SCRWIDTH, SCRHEIGHT)) 
bluesky.fill("SKYBLUE") 

toolbar = pygame.Surface((200, SCRHEIGHT))
toolbar.fill("WHITE")

font = pygame.font.SysFont("Consolas", 40, True, False)

land = pygame.Surface((SCRWIDTH, SCRHEIGHT))          # Normal surface.
land.fill(SAND)

player = pygame.image.load('gamegraphics/hero.png')
playerscaled = pygame.transform.scale(player, (100,150))
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
        if dude.rect.bottom > FLOOR: 
            dude.rect.bottom = FLOOR
        screen.blit(self.image, self.rect)
        
        # # code atul is adding to check for collision
        # for tile in world.tile_list:
        #         #check for collision in x direction
        #         if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
        #             dx = 0
        #         #check for collision in y direction
        #         if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
        #             #check if below the ground i.e. jumping
        #             if self.vel_y < 0:
        #                 dy = tile[1].bottom - self.rect.top
        #                 self.vel_y = 0
        #             #check if above the ground i.e. falling
        #             elif self.vel_y >= 0:
        #                 dy = tile[1].top - self.rect.bottom
        #                 self.vel_y = 0

    def jump(self):
        if self.rect.bottom == 950:
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


    def update(self):
        screen.blit(self.image, enemy_rect)

    def jump(self):
        self.gravity = -10


# ATUL'S WORK START
tile_size = 50

#load images
sn_img = pygame.image.load('gamegraphics/moon.png')
sun_img = pygame.transform.scale(sn_img, (50, 50))
b_img = pygame.image.load('gamegraphics/sky.png')
bg_img = pygame.transform.scale(b_img, (1000, 1000))

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
    [0, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1],
    [0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

world = World(world_data)

# ATUL'S WORK END

gamestate = "startscreen"


while gamestate == "startscreen":

    dude = Player(20, 60, 80, 950, playerscaled)
    villain = Enemy1(120, 5, 800, 1000, enemy1scaled)

    screen.blit(bluesky, (0,0))
    screen.blit(land, (0,600))

    # Integrate Atul's start screen and according buttons.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:          # If the window is exited, the game quits.
            pygame.quit()
            exit()

        x,y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and 0<x<1500 and 0<y<800:
            gamestate = "play"

    pygame.display.update()
    clock.tick(60)    


while gamestate == "play":


    screen.blit(bg_img, (0, 0))
    screen.blit(sun_img, (100, 100))
    world.draw()
    draw_grid()

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
        enemy_rect.left -= villain.speed

    elif dude.score >= 3 and dude.score < 10:
        enemy_rect.left -= villain.speed + 5

    # pygame.draw.rect(screen, (255,0,0), dude.) #(UN-COMMENT TO ACCESS HITBOXES)
    # pygame.draw.rect(screen, (255,0,0), enemy_rect)
    
    dashcooldown -= 1
    if dashcooldown < 0:
        dashcooldown = 0

    dude.update()

    # Our deplorable enemy.

    enemy_gravity += 1
    enemy_rect.y += enemy_gravity
    if enemy_rect.left < L_BORDER: 
        enemy_rect.left = R_BORDER
    if enemy_rect.bottom > FLOOR: 
        enemy_rect.bottom = FLOOR
    enemy_dodge_timer += 1
    if enemy_dodge_timer == 120:
        enemy_gravity = -20
        villain.jump()
        enemy_dodge_timer = 0
    villain.update()

    screen.blit(toolbar, (1000,0))
    if dashcooldown == 0:
        screen.blit(dash_icon,dash_rect)

    # Score
    scoretext = font.render(f"SCORE:{dude.score}", True, (0,0,0))
    screen.blit(scoretext, (1000, 800))

    if enemy_rect.colliderect(dude.rect):
        if dude.right_inertia != 0 or dude.left_inertia != 0:
            pass
        else:
            print("GAME OVER! FINAL SCORE:", dude.score)
            gamestate = "gameover"
            # pygame.quit()
            # exit()

    pygame.display.update()
    clock.tick(60)                            # FPS Ceiling - Cannot run faster than 60 FPS.

while gamestate == "gameover":
    pygame.quit()
    exit()



    '''
    THINGS TO IMPLEMENT:
    - GAME-OVER GAME STATE

    - PRINT SCORE

    
    - HOW TO IMPLEMENT GAMESTATE:
        - Standardize screen size
        - Include background code and print accordingly
        - Shrink sprites
        - Spawn multiple enemies
    '''
