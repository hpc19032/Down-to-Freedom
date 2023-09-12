import sys
import pygame
from pygame.locals import QUIT
import pygame.locals

# Initializing pygame
pygame.init()

# Setting screen
screen = pygame.display.set_mode((285, 324))

# Loading background image
bg_surface = pygame.image.load('Assets/Background.png')

# Setting title
pygame.display.set_caption("Down to Freedom")


# Rendering text
def write(text):
  font = pygame.font.SysFont("Montserrat", 15)  #setting font
  lines = text.split(
      '\n')  # Split the text into a different line everytime there is a'\n'
  # Calculate vertical position for each line
  y = 40
  x = 130
  for line in lines:
    text_surface = font.render(line, True, (183, 183, 183))
    screen.blit(text_surface, (x, y))
    y += 10  # vertical spacing
    # ajusting where lines start to make them go around the map
    if line == (lines[0]):
      x += 6
    elif line == (lines[1]):
      x += 2
  pygame.display.update()


# Defining the play_game function
def play_game():
  play = input(
      write(
          "Welcome to Down to \nFreedom, would you like \nto begin your adventure?"
      ))
  play = play.strip().lower()
  if play == 'y' or play == 'yes':
    write(
        "Within this adventure your keyboard is your guide./n To journey from room to room use one of the following commands. /n To venture westward, type Move West./n For a southern path, enter Move South. /n To tread northward, simply type Move North. For an eastward direction, type Move East."
    )


# Game not started (Making sure bg appears first)
game_started = False

# Game loop
loop = '0'
while loop == '0':
  for event in pygame.event.get():
    # Close game when "x" pressed
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  if not game_started:
    # Making sure bg appears first
    screen.blit(bg_surface, (0, 0))
    pygame.display.update()
    game_started = True

  play_game()
  loop = '2'
  # Update the screen
  pygame.display.update()
