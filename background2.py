import pygame

pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))

# define game variables
tile_size = 50
main_menu = True

# load images
sn_img = pygame.image.load('gamegraphics/moon.png')
sun_img = pygame.transform.scale(sn_img, (50,50))
b_img = pygame.image.load('gamegraphics/sky.png')
bg_img = pygame.transform.scale(b_img, (1000,1000))

# start and end image
start_img = pygame.image.load('gamegraphics/start button')
exit_img = pygame.image.load('gamegraphics/exit button')


class Buttons:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

        # def draw(self):
        # action = False
        # get button to click
        posx, posy = pygame.mouse.get_pos()
        # if mouse over button
        # FIND A WAY TO CLICK START AND EXIT BUTTONS THROUGH MOUSE HOVER OVER THE BUTTON


"""
        if posx > 0 and posx < 500:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        # draw button
        screen.blit(self.image, self.rect)
        return action
        """


def draw_grid():
    for line in range(0, 20):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))


class World:
    def __init__(self, data):

        self.tile_list = []

        # load image of dirt
        dit_img = pygame.image.load("gamegraphics/dirt.png")
        dirt_img = pygame.transform.scale(dit_img, (50,50))

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

# buttons
start_button = Buttons(screen_width // 2 - 350, screen_height // 2, start_img)
exit_button = Buttons(screen_width // 2 + 150, screen_height // 2, exit_img)

# to keep the game running
run = True
while run:
    # put images on the game screen
    screen.blit(bg_img, (0, 0))
    screen.blit(sun_img, (100, 100))
"""
    if main_menu:
        # if exit_button.draw():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                main_menu = False
    else:
        world.draw()
        draw_grid()
        print(world.tile_list)
"""
    # a false statement to allow to quit the run
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False

    pygame.display.update()

pygame.quit()
