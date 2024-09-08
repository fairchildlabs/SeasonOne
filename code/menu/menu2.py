import pygame
import button
import subprocess

pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Scootcam")

#game variables
game_paused = True
menu_state = "stop"

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)

#load button images
record_img = pygame.image.load("images/rec-button.png").convert_alpha()
stop_img = pygame.image.load("images/stop-button.png").convert_alpha()


#create button instances
record_button = button.Button(250, 125, record_img, .75)
stop_button = button.Button(250, 125, stop_img, .75)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop
run = True
process = None
while run:

  screen.fill((255, 255, 255))

  if menu_state == "stop":
    #draw pause screen buttons
     if record_button.draw(screen):
        menu_state = "record"
        if not (process is None):
            process.kill()
            output, error = process.communicate()
            process = None
        
  else: 
     if stop_button.draw(screen):
        #git update-index --chmod=+x

        #bashCommand = ".\record.sh"
        process = subprocess.Popen("./record.sh", stdout=subprocess.PIPE)
        #output, error = process.communicate()
        menu_state = "stop"



 
  #event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()