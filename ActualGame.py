import pygame
import os
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
select = 1

games = 'C:\Users\pc\game\games'

f = ( games,'r')

for file in f:
  print(file)

pygame.init()

# Set the width and height of the screen [width, height]
SIZE = (700, 500)
SCREEN = pygame.display.set_mode(SIZE)

pygame.display.set_caption("BEANS")

SCREEN_SURFACE = pygame.image.load(r"C:\Users\pc\game\BEANS.jpg")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 32)
TEXTSURFACE = font.render('THESE ARE BEANS!!!!!!!!', False, (0, 0, 0))
TEXTSURFACE2 = font.render('THERE ARE EVEN MORE BEANS!!!', False, BLACK)
TEXTSURFACE3 = font.render('THE TEXT IS WHITE NOW', False, WHITE)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # the selection mechanism which will be used to select a rectangle
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and select > 1:
                select = select - 1
            if event.key == pygame.K_DOWN and select < 3:
                select = select + 1

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    SCREEN.blit(SCREEN_SURFACE, (0, 0))
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    SCREEN.blit(TEXTSURFACE, (0, 50))
    SCREEN.blit(TEXTSURFACE2, (0, 100))
    SCREEN.blit(TEXTSURFACE3, (170, 200))
    if select == 1:
      pygame.draw.rect(SCREEN_SURFACE, WHITE, pygame.Rect((0, 50), TEXTSURFACE.get_size()),2)
      pygame.draw.rect(SCREEN_SURFACE, BLACK, pygame.Rect((0, 100), TEXTSURFACE2.get_size()),2)
      pygame.draw.rect(SCREEN_SURFACE, BLACK, pygame.Rect((170, 200), TEXTSURFACE3.get_size()),2)
    if select == 2:
      pygame.draw.rect(SCREEN_SURFACE, BLACK, pygame.Rect((0, 50), TEXTSURFACE.get_size()),2)
      pygame.draw.rect(SCREEN_SURFACE, WHITE, pygame.Rect((0, 100), TEXTSURFACE2.get_size()),2)
      pygame.draw.rect(SCREEN_SURFACE, BLACK, pygame.Rect((170, 200), TEXTSURFACE3.get_size()),2)
    if select == 3:
      pygame.draw.rect(SCREEN_SURFACE, BLACK, pygame.Rect((0, 50), TEXTSURFACE.get_size()),2)
      pygame.draw.rect(SCREEN_SURFACE, BLACK, pygame.Rect((0, 100), TEXTSURFACE2.get_size()),2)
      pygame.draw.rect(SCREEN_SURFACE, WHITE, pygame.Rect((170, 200), TEXTSURFACE3.get_size()),2)
    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
