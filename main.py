#Importing functions
import sys
import pygame
import time
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

#setting inventory
global inventory
inventory = []


# Rendering text
def write(text):

  #Clearing the previous text
  screen.blit(bg_surface, (0, 0))

  # Setting font
  font = pygame.font.SysFont("Montserrat", 12)

  #setting position of each line
  y = 40
  x = 25

  #Splitting text iinto lines so next bit works
  lines = text.split('\n')

  #Rendering each line
  for line in lines:
    text_surface = font.render(line, True, (183, 183, 183))
    screen.blit(text_surface, (x, y))
    y += 9
    pygame.display.update()


# Defining the play_game function
def play_game():
  play = input(
      write("""Welcome to Down to Freedom,
would you like to begin your
adventure?"""))

  #removing spaces and upper cases.
  play = play.strip().lower()

  if play == 'y' or play == 'yes':
    write("""Within this adventure your 
keyboard is your guide. 

To journey from room to room use 
one of the following commands. 
   - To venture westward, type 
     "Move West". 
   - For a southern path, enter 
     "Move South". 
   - To tread northward, simply type 
     "Move North". 
   - For an eastward direction, type 
     "Move East".""")

    #Ensuring the player has time to read
    pygame.time.wait(13000)

    write("""Furthermore, to pick up an item, 
use the command:
"Pick up" followed by the name 
of the item as it is described in the
description of the room.

In your journey through this text 
adventure, items will prove their 
worth without your explicit command. 
When you work to move in the correct 
direction, carrying the fitting items in your 
inventory, their usage will come into 
play seamlessly.
""")
  elif play == 'n' or play == 'no':
    write("""You gaze into the light as your one chance of escaping leaves.""")
    #letting player read
    pygame.time.wait(4000)

    #quitting game
    pygame.quit()
    sys.exit()


def meeting_room(inventory):
  #varible used to determine if player has been in room before
  time_meeting_room = None
  if time_meeting_room == 0:

    #Reading time
    pygame.time.wait(13000)

    #text for entering room first time
    write(
        """You come to find yourself in a dimly lit meeting room. Tall, imposing windows stretch from the floor to the ceiling along one wall.  A city skyline is visible beyond the glass, its shapes softened by the fading light of day. The room is dominated by a massive, dusty wooden table that occupies the center. The table's surface is smooth, reflecting the dim light from the ceiling above. On the table lies a “blue key card” , its edges catching what little light is available."""
    )

    time_meeting_room == 1

  #Alternative text when entering room for second time
  else:
    write(
        """You have just entered the Meeting Room, Nothing has changed since you were last in here."""
    )

  while True:
    input = input("")
    input = input.strip().lower()

    #attempting to move an invalid direction
    if input == "movenorth" or input == "movesouth" or input == "movewest":
      write(
          """As much as you may wish to go in that direction there is no door in that direction."""
      )

#attempting to leave without a keycard.
    elif input == "moveeast" and "red_keycard" not in inventory:
      write(
          "You walk over the door, ignoring the keypad and attempt to pull open the door. Despite your best efforts it refuses to budge, giving up, you look around the room for another solution."
      )

#Picking up keycard
    elif input == "pickupredkeycard":
      inventory.append("red_keycard")

#moving to reception when requirements met
    elif input == "moveeast" and "red_keycard" in inventory:
      reception(inventory)

    #invailid input
    else:
      write("You look around confused as to what you were trying to do.")

  return input, inventory


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

#Begining the loop of def functions
  play_game()
  meeting_room(inventory)

  loop = '2'

  # Update the screen
  pygame.display.update()
