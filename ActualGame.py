from numpy import size
import pygame
import os
import cv2
import  mediapipe as mp
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
select = 0
mp_Hands = mp.solutions.hands
hands = mp_Hands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

vid = cv2.VideoCapture(0)
neutral = True
previous_frame_neutral = True

# The functions that identify the shape the user makes with his hand in order to command the screen
def is_fist(Middle_line, Finger1, Finger2, Finger3, Finger4):
    if Middle_line < Finger1 and Middle_line < Finger2 and Middle_line < Finger3 and Middle_line < Finger4:
        return True
    else:
        return False
def is_certain_shape(Middle_line, Above1, Above2, Below1, Below2):
    if Middle_line > Above1 and Middle_line > Above2 and Middle_line < Below1 and Middle_line < Below2:
        return True
    else:
        return False


pygame.mixer.init
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i).init() for i in range(pygame.joystick.get_count())]
cwd = 'games'

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

SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
SCREEN = pygame.display.set_mode(SIZE)

pygame.display.set_caption("Selection Screen")

SCREEN_SURFACE = pygame.image.load(r"BK.jpg")

SCREEN_SURFACE = pygame.transform.scale(SCREEN_SURFACE, SIZE)

# Loop until the user clicks the close button.
Done = False
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
while not Done:
    # --- Main event loop
    ret, frame = vid.read()
    RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(RGB_frame)
    multiLandMarks = results.multi_hand_landmarks
    
    if multiLandMarks:
        for h in multiLandMarks:
            mpDraw.draw_landmarks(frame, h, mp_Hands.HAND_CONNECTIONS)

        index_finger_tip_y = multiLandMarks[0].landmark[8].y
        middle_finger_tip_y = multiLandMarks[0].landmark[12].y
        ring_finger_tip_y = multiLandMarks[0].landmark[16].y
        pinky_tip_y = multiLandMarks[0].landmark[20].y
        
        index_finger_base_y = multiLandMarks[0].landmark[6].y
        
        hand_center_position_y = multiLandMarks[0].landmark[9].y

        neutral = not is_fist(index_finger_base_y, index_finger_tip_y, middle_finger_tip_y, ring_finger_tip_y, pinky_tip_y)
        
        enter_game = is_certain_shape(index_finger_base_y, index_finger_tip_y, pinky_tip_y, middle_finger_tip_y, ring_finger_tip_y)

        if hand_center_position_y < 0.5:
            hand_height = "high"
        else:
            hand_height = "low"
        
        if enter_game and not previous_frame_entry and previous_frame_neutral:
            pygame.mixer.Sound("./Selected.mp3").play()
            os.chdir(list_of_game_roots[select])
            os.system("python main.py")
            os.chdir("../..")
        elif not neutral and hand_height == "high" and previous_frame_neutral and select > 0:
                select = select - 1
                pygame.mixer.Sound("./Change.mp3").play()
        elif not neutral and hand_height == "low" and previous_frame_neutral and select < len(TEXT_SURFACES) - 1:
                select = select + 1
                pygame.mixer.Sound("./Change.mp3").play()
        
        previous_frame_neutral = neutral
        previous_frame_entry = enter_game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Done = True
        # the selection mechanism which will be used to select a rectangle
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and select > 0:
                select = select - 1
                pygame.mixer.Sound("./Change.mp3").play()
            if event.key == pygame.K_DOWN and select < len(TEXT_SURFACES) - 1:
                select = select + 1
                pygame.mixer.Sound("./Change.mp3").play()
            if event.key == pygame.K_SPACE:
                pygame.mixer.Sound("./Selected.mp3").play()
                os.chdir(list_of_game_roots[select])
                os.system("python main.py")
                os.chdir("../..")
        if event.type == pygame.JOYBUTTONDOWN:
            pygame.mixer.Sound("./Selected.mp3").play()
            os.chdir(list_of_game_roots[select])
            os.system("python main.py")
            os.chdir("../..")
        if event.type == pygame.JOYAXISMOTION:
            if event.axis == 1 and event.value <= -0.1 and select < len(TEXT_SURFACES) - 1:
                select = select + 1
                pygame.mixer.Sound("./Change.mp3").play()
            if event.axis == 1 and event.value > 0 and select > 0:
                select = select - 1
                pygame.mixer.Sound("./Change.mp3").play()
    SCREEN.blit(SCREEN_SURFACE, (0, 0))
    
    

    # Drawing all the text surfaces and their borders according to the selected game
    for i in range(len(TEXT_SURFACES)):
      SCREEN_SURFACE.blit(TEXT_SURFACES[i], (85, 100*i + 100))
      if select == i:
        [h, w] = TEXT_SURFACES[i].get_size()
        pygame.draw.rect(SCREEN_SURFACE, WHITE, pygame.Rect((85, 100*i + 100), (h, w+3)),2)  
      else:
        [h, w] = TEXT_SURFACES[i].get_size()
        pygame.draw.rect(SCREEN_SURFACE, BLACK, pygame.Rect((85, 100*i + 100), (h, w+3)),2)
    SCREEN.blit(TEXT_DESCRIPTION_SURFACES[select], (SCREEN_WIDTH/2,80))
    SCREEN.blit(pygame.transform.scale(GAME_IMAGE_SURFACES[select], (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)),((SCREEN_WIDTH//2) - 84, (SCREEN_HEIGHT//2) - 65))


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
vid.release()
cv2.destroyAllWindows()
pygame.quit()
