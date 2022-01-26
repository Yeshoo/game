import pygame
import os
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
select = 0

cwd = '.\games'

# The function that gets the names of all the games
def get_dir_list():
  return next(os.walk(cwd))[1]
print (get_dir_list())

# The list of all our games
list_of_games = list((get_dir_list()))

# Set the width and height of the screen [width, height]
SIZE = (700, 500)
SCREEN = pygame.display.set_mode(SIZE)

pygame.display.set_caption("BEANS ")

SCREEN_SURFACE = pygame.image.load(r".\BEANS.jpg")

# Loop until the user clicks the close button.
done = False
pygame.init()
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

font = pygame.font.SysFont('Comic Sans', 32)
Description_font = pygame.font.SysFont('Arial', 16)

# Creating the list of all the text surfaces that will be used
TEXT_SURFACES = []

# Adding each a surface that will write each games name to the list
for game in list_of_games:
  TEXT_SURFACES.append(font.render(game, True, BLACK))

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
            if event.key == pygame.K_DOWN and select < len(TEXT_SURFACES) - 1:
                select = select + 1

    # above this, or they will be erased with this command.
    SCREEN.blit(SCREEN_SURFACE, (0, 0))
    

    # Drawing all the text surfaces and their borders according to the selected game
    for i in range(len(TEXT_SURFACES)):
      SCREEN_SURFACE.blit(TEXT_SURFACES[i], (0, 100*i))
      if select == i:
        pygame.draw.rect(SCREEN_SURFACE, WHITE, pygame.Rect((0, 100*i), TEXT_SURFACES[i].get_size()),2)  
      else:
        pygame.draw.rect(SCREEN_SURFACE, BLACK, pygame.Rect((0, 100*i), TEXT_SURFACES[i].get_size()),2)


    

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
