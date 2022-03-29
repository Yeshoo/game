from numpy import size
import pygame
import os
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
select = 0

pygame.mixer.init

cwd = '.\games'

# The functions that get the names and roots of all the games
def get_dir_list():
  return next(os.walk(cwd))[1]

def get_dir_root_list():
  roots = []
  for game in next(os.walk(cwd))[1]:
    roots.append(os.path.join(cwd, game))
  return roots

def get_game_text_roots():
  roots = []
  for root in get_dir_root_list():
    roots.append(os.path.join(root, 'text.txt'))
  return roots

def get_game_python_script():
  roots = []
  for root in get_dir_root_list():
    roots.append(os.path.join(root, "main.py"))
  return roots

def get_game_image_roots():
  roots = []
  for root in get_dir_root_list():
    roots.append(os.path.join(root, 'image.png'))
  return roots

# The lists of all our games, their roots, etc...
list_of_games = list((get_dir_list()))
list_of_game_python_script = list((get_game_python_script()))
list_of_game_roots = list((get_dir_root_list()))
list_of_game_text_root = list((get_game_text_roots()))
list_of_game_image_roots = list((get_game_image_roots()))

# Set the width and height of the screen [width, height]

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 700
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
SCREEN = pygame.display.set_mode(SIZE)

pygame.display.set_caption("Selection Screen")

SCREEN_SURFACE = pygame.image.load(r".\BK.jpg")

SCREEN_SURFACE = pygame.transform.scale(SCREEN_SURFACE, SIZE)

# Loop until the user clicks the close button.
done = False
pygame.init()
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

font = pygame.font.Font('font.ttf', 32)
Description_font = pygame.font.SysFont('Arial', 16)

# Creating the list of all the text surfaces that will be used
TEXT_SURFACES = []

TEXT_DESCRIPTION_SURFACES = []

GAME_IMAGE_SURFACES = []

# Adding each a surface that will write each games name to the list
for game in list_of_games:
  TEXT_SURFACES.append(font.render(game, True, WHITE))

for desc in list_of_game_text_root:
  f = open(desc, "rt")
  text = f.read()
  TEXT_DESCRIPTION_SURFACES.append(Description_font.render(text, True, WHITE))

for img_root in list_of_game_image_roots:
 GAME_IMAGE_SURFACES.append(pygame.image.load(img_root))
  

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # the selection mechanism which will be used to select a rectangle
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and select > 0:
                select = select - 1
                pygame.mixer.Sound("Change.mp3").play()
            if event.key == pygame.K_DOWN and select < len(TEXT_SURFACES) - 1:
                select = select + 1
                pygame.mixer.Sound("Change.mp3").play()
            if event.key == pygame.K_SPACE:
               pygame.mixer.Sound("Selected.mp3").play()
               os.system("python ." + list_of_game_python_script[select][1:])
    SCREEN.blit(SCREEN_SURFACE, (0, 0))
    
    

    # Drawing all the text surfaces and their borders according to the selected game
    for i in range(len(TEXT_SURFACES)):
      SCREEN_SURFACE.blit(TEXT_SURFACES[i], (70, 100*i + 100))
      if select == i:
        [h, w] = TEXT_SURFACES[i].get_size()
        pygame.draw.rect(SCREEN_SURFACE, WHITE, pygame.Rect((70, 100*i + 100), (h, w+3)),2)  
      else:
        [h, w] = TEXT_SURFACES[i].get_size()
        pygame.draw.rect(SCREEN_SURFACE, BLACK, pygame.Rect((70, 100*i + 100), (h, w+3)),2)
    SCREEN.blit(TEXT_DESCRIPTION_SURFACES[select], (SCREEN_WIDTH/2,50))
    SCREEN.blit(pygame.transform.scale(GAME_IMAGE_SURFACES[select], (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)),((SCREEN_WIDTH/2) - 70, (SCREEN_HEIGHT/2) - 50))


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
