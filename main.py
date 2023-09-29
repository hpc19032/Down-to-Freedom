#Importing functions
import sys
import pygame
import time
from pygame.locals import QUIT, KEYDOWN, K_RETURN, K_BACKSPACE
import pygame.font
import pygame_textinput  #https://github.com/Nearoo/pygame-text-input

# Initializing pygame
pygame.init()
pygame.font.init()

# Setting screen
screen = pygame.display.set_mode((280, 343))
screen.fill((243, 255, 255))

# Setting title
pygame.display.set_caption("Down to Freedom")

# Loading background image
bg_surface = pygame.image.load('Assets/Background.png')
r_keycard = pygame.image.load('Assets/Red_Keycard.jpg')
o_keycard = pygame.image.load('Assets/Orange_Keycard.jpg')
crowbar = pygame.image.load('Assets/Crowbar.png')

#settinginput box variables
font = pygame.font.SysFont("dejavusans", 13)  
global textOutput
textoutput = ""
textinput = pygame_textinput.TextInputVisualizer(font_object=font)
clock = pygame.time.Clock()
textinput.cursor_width = 0
pygame.key.set_repeat(200, 25)

#setting inventory
global inventory
inventory = []

#keeping track of amount of time in each room
meeting_time = 0
reception_time = 0
closet_time = 0
office_time = 0
m_office_time = 0
lobby_time = 0


def getInputText():

	#setting event/updating if event
	global events
	events = pygame.event.get()
	textinput.update(events)

	#blitting typed toext to screen
	screen.blit(textinput.surface, (17, 290, 140, 32))

	for event in events:
		
		#quitting if x pressed
		if event.type == pygame.QUIT:
			exit()

			#clearing if enter pressed
		if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and textinput.value != "":
			global textoutput
			textoutput = textinput.value
			textinput.value = ""
			screen.blit(bg_surface, (0, 0))

		#removing last letter if backspace pressed
		if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
			screen.blit(bg_surface, (0, 0))

	pygame.display.update()
	clock.tick(30)


# Rendering text
def write(text):
	
  font = pygame.font.SysFont("dejavusans", 9)  
	
  #Clearing the previous text
  screen.blit(bg_surface, (0, 0))

  #setting position of each line
  y = 45
  x = 20

  #Splitting text iinto lines so next bit works
  lines = text.split('\n')

  #Rendering each line
  for line in lines:
    text_surface = font.render(line, True, (0, 0, 0))
    screen.blit(text_surface, (x, y))
    y += 9
  pygame.display.update()

	
def play_game():
	
	while True:

		#setting input box to work
		getInputText()
		global textoutput
		play = textoutput

		write("""Welcome to Down 
to Freedom, would 
you like to begin your 
adventure?""")

		# Removing spaces and upper cases.
		play = play.strip().lower()

		if play == 'yes'or play == 'y':
			textoutput = ""
			write("""Within this 
adventure your 
keyboard is your guide. 

To journey from room to 
room use one of the
following commands. 
            
  - To venture westward, type 
    "Move West". 
  - For a southern path, enter 
    "Move South". 
  - To tread northward, simply 
    type 
    "Move North". 
  - For an eastward direction, 
    type 
    "Move East".""")

    	#waiting for key press to move on
			waiting_for_keypress = True
			while waiting_for_keypress:
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						waiting_for_keypress = False

			write("""Furthermore, to pick 
up an item, use the 
command:"Pick up" 
followed by the name 
of the item as it is 
described in the 
description of the room.

In your journey through this text 
adventure, items will prove their 
worth without your explicit 
command. When you work to 
move in the correct direction, 
carrying the fitting items in 
your inventory, their usage will 
come into play seamlessly.""")

			#waiting for key press to move on
			waiting_for_keypress = True
			while waiting_for_keypress:
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						waiting_for_keypress = False
			break

		elif play == 'n' or play == 'no':
			textoutput = ""
			write("""You gaze into the 
light as your one 
chance of escaping 
leaves.""")

    	#waiting for key press to move on
			pygame.time.wait(4000)

    	#Quitting game
			pygame.quit()
			sys.exit()


def meeting_room(inventory):

  #varible used to determine if player has been in room before
  global meeting_time
  if meeting_time == 0:

    #text for entering room first time
  	write("""You come to find 
yourself in a dimly 
lit meeting room. Tall, 
imposing windows stretch
from floor to ceiling along 
one wall. A city skyline is 
visible beyond the glass. The 
room is dominated by a large, 
dusty wooden meeting table. 
The table's surface smooth, 
reflecting the dim light from 
the ceiling above. On the table 
lies a “red keycard”, its edges 
catching what little light is 
available. Across the room to 
the east a majestic set of 
double doors are seamlessly 
embedded in the pale off-white 
of the surrounding walls. Next 
to this door, a card reader 
is affixed to the wall, a 
pulsating red light upon it, 
signals the need for a
card's presence.
 """)
  	
  	meeting_time = 1

#Alternative text when entering room for second time
  else:
    write("""You have just entered the Meeting 
Room, Nothing has changed since you 
were last in here.""")

  while True:

		#setting input box to work
    getInputText()
    global textoutput
    movement = textoutput
    movement = movement.strip().lower()

    #attempting to move an invalid direction
    if movement == "move north" or movement == "move south" or movement == "move west":
      write("""As much as you may wish to go in 
that direction, there is no door 
there.""")

  #attempting to leave without a keycard.
    elif movement == "move east" and "red_keycard" not in inventory:
      write("""You walk over the door, ignoring 
the keypad and attempt to pull 
open the door. Despite your 
best efforts it refuses to budge, 
giving up, you look around the room 
for another solution.""")

  #Picking up keycard
    elif movement == "pickup red keycard":
      inventory.append("red_keycard")
      screen.blit(r_keycard, (213, 255))
      write("""You slide the red key card off the 
table and into your hand 
disturbing the dust as you pick 
it up and place it in your 
pocket for future use.""")

  #moving to reception when requirements met
    elif movement == "move east" and "red_keycard" in inventory:
      reception(inventory)

#invailid input
    elif movement not in ['move east', 'move west', 'move south', 'move north', 'pickup red keycard','']:
      write("""You look around 
confused as to what 
you were trying to do.""")
			
	
  return inventory


#Defining reception
def reception(inventory):

  #varible to determine if player has been in room before
  global reception_time
  if reception_time == 0:

    #Text for entering room for first time
    write("""After using the red key card on 
the door, you find yourself 
standing in a basic reception 
area, the dusty air swirling 
in the light coming from 
the open door to the meeting 
room. The room is modestly lit, 
with a single overhead light 
casting a glow upon a reception desk 
that stands before you. The desk is 
dusty and disorderly as though those 
who were once here had left in great hurry.
 
Four doors stand out from the off-white of each 
wall:
	- To the north, a door, slightly ajar, sits 
    within the center of the wall, giving you 
		a glimps of what seems to be office 
    cubicles inside.
	- In the opposite direction, to the 
    south, an extremely worn door sits 
		shrouded in shadows.
	- On the east wall, a large hallway 
    sits with large metal doors on each side.
	- To the west is the wide open door that 
    leads back to the meeting room.""")

    reception_time = 1

  #Alternative text when entering room for second time
  else:
    write("""You have just entered the Reception, 
Nothing has changed since you were last here.""")

  while True:
    movement = input("")
    movement = movement.strip().lower()

    #Moveing to closet
    if movement == "move south":
      closet(inventory)

    #Moveing to lobby
    elif movement == "move east":
      lobby(inventory)

    #moving back to meeting room
    elif movement == "move west":
      meeting_room(inventory)

    #moving to the office
    elif movement == "move north":
      office(inventory)

    #invailid input
    else:
      write("""You look around confused as to 
what you were trying to do.""")

  return inventory


def closet(inventory):

  #Determining if player has been in room before
  global closet_time
  if closet_time == 0:

    #text for entering room for first time.
    write(
        """A faint scent of cleaning supplies greets your senses as you push open the worn door to the room. The door bangs against something plastic as you step into the room, the sound echoing through the small room. The room is dimly lit, with a solitary overhead bulb casting elongated shadows across the cluttered shelves. Among the clutter, a “crowbar” seems both out of place and yet perfectly at home – a juxtaposition that beckons your consideration. Its promise of strength and adaptability hints at its potential usefulness in your journey, a silent companion in the midst of this unexpected adventure."""
    )

    closet_time = 1

  #Alternative text when entering room for second time.
  else:
    write(
        """You have just entered the Janitors Closet, Nothing has changed since you were last in here."""
    )

  while True:
    movement = input("")
    movement = movement.strip().lower()

    #attempting to move an invalid direction
    if movement == "move east" or movement == "move south" or movement == "move west":
      write("""As much as you may wish to go in 
that direction, there is no door 
there.""")

    #Moving back to reception
    elif movement == "move south":
      reception(inventory)

    #picking up crowbar
    elif movement == "pickup crowbar":
      inventory.append("crowbar")
      screen.blit(crowbar, (213, 170))
      write("""Reaching down you pick 
up the crow bar from 
where it rests on the ground, 
the worn metal rests heavy 
in your hands as you stand 
up once more ready to continue 
your adventure. """)

    #incorrect input
    else:
      write("""You look around confused as to 
what you were trying to do.""")

  return inventory


#Office
def office(inventory):

  #been in room before?
  global office_time
  if office_time == 0:

    #entering room for first time
    write(
        """Shoving the door open as it resists your effort, you step into a cluttered office, where the air is tinged with the scent of paper, ink, and a hint of abandoned coffee cups. The room is dimly lit by the glow of fluorescent lights hanging overhead, casting a pale illumination over the chaos that surrounds you. Desk spaces are strewn with stacks of paper, half-empty notebooks, and forgotten office supplies.  A lone door to the west beckons your attention, its surface covered with various notes and memos, a testament to the hurried pace of office life.    """
    )

    office_time = 1

  #Alternative text wehn entering room not for first time
  else:
    write("""You have just entered the 
Office, Nothing has changed 
since you were last here.""")

  while True:
    movement = input("")
    movement = movement.strip().lower()

    #attempting to move in invalid direction
    if movement == "move north" or movement == "move east":
      write("""As much as you may wish to go in 
that direction, there is no door 
there.""")

    #moveing to managers office
    elif movement == "move west":
      m_office(inventory)

    #moveing back to reception
    elif movement == "move south":
      reception(inventory)

    #invalid input
    else:
      write("""You look around confused as to 
what you were trying to do.""")

  return inventory


def m_office(inventory):

  #Varible to determind if player been in roome before
  global m_office_time
  if m_office_time == 0:

    #enterng room for first time
    write(
        """Pushing the door open you step into the room that seems to be a manager or supervisors office, the air is thick with a mix of aged leather, paper, and a faint hint of stale coffee. Dim light filters through partially closed blinds, casting elongated shadows across stacks of documents and half-opened file cabinets. The manager's desk is a chaotic symphony of organized chaos. Piles of paperwork intermingle with scattered stationery and tangled cords from various electronic devices. 
Amidst the clutter, a worn “orange key card” stands out on the corner of the desk."""
    )

    m_office_time = 1


#entering room for secnd time
  else:
    write("""You have just entered the Manager's 
 Office, Nothing has changed since 
 you were last in here.""")

  while True:
    movement = input("")
    movement = movement.strip().lower()

    #attempting to move in invalid direction
    if movement == "move north" or movement == "move south" or movement == "move west":
      write("""As much as you may wish to go in 
that direction, there is no door 
there.""")

    #Moving back to office
    elif movement == "move east":
      office(inventory)

    #Picking up keycard
    elif movement == "pickup orange keycard":
      inventory.append("orange_keycard")
      screen.blit(o_keycard, (213, 200))
      write(
          """Carefully avoiding the chaos on the desk you pick up the worn orange keycard and place it in your pocket. Perhaps it could be useful in the future."""
      )

    #incorrect input
    else:
      write("""You look around confused as to 
what you were trying to do.""")

  return inventory


def lobby(inventory):

  #has player been in roome before
  global lobby_time
  if lobby_time == 0:

    #first time in room
    write(
        """You stand in a basic elevator lobby, the air stagnant with a faint scent of old machinery and dust. Dim overhead lights cast a feeble glow, revealing a scene of contrast and desolation. Two elevators occupy the space before you. One stands silently, its doors wide open, revealing a hollow shaft beyond. This elevator appears to be out of commission, its buttons unlit and its interior shrouded in darkness. Beside it, the second elevator is a stark juxtaposition. Its doors are tightly boarded up, secured with weathered wooden planks that hint at an effort to keep it sealed off, perhaps you could get them off if you had a tool of some sort. Despite its appearance, a subtle hum emanates from behind the barricade, suggesting that it's still operational, if inaccessible. Beside both elevators sits two more keypads, these one emanating a subtle green glow."""
    )

    lobby_time = 1

  else:
    write(
        """You have just entered the Elevator Lobby, Nothing has changed since you were last in here."""
    )

  while True:
    movement = input("")
    movement = movement.strip().lower()

    if movement == "move south" or movement == "move north" or movement == "move east":
      write("""As much as you may wish to go in 
that direction, there is no door 
there.""")

    #Meving back to reception
    elif movement == "move west":
      reception(inventory)

    elif "orange_keycard" in inventory and "crowbar" in inventory:
      write(
          """Anticipation hangs in the air as you stand in the elevator lobby for the final time, your heart pounding in tandem with the hum of the operational elevator. The boarded-up elevator door before you seems like the final hurdle, and the crowbar you found has proven invaluable.
Gripping the crowbar tightly, you bring it down with determined force against the wooden boards. The sound of splintering wood sends a rush of triumph through you as the path to the operational elevator is now clear.
Moving to your left as you pull the green keycard out of where it resided in your pocket, picking it up was one of the best decisions you have ever made. As you swipe the keycard it beeps with a finality that resonates throught you. A sense of anticipation entering the air as you step into the elevator. As you press the button for the ground floor, the elevator begins its descent. 
With a gentle jolt, the elevator comes to a stop. The doors slide open, revealing a world beyond the building's confines. The fresh breeze on your face is invigorating, and the expanse of the outside world seems impossibly vast.
You've overcome challenges, collected key cards, and used your resourcefulness to escape. As you step out of the elevator, you realize that your journey through the building was more than just a series of obstacles – it was a testament to your determination and problem-solving skills.
With the building's mysteries behind you, you step into the daylight, ready to embrace the possibilities of what lies ahead. The taste of freedom is sweeter than ever, a reward for your unwavering resolve and the choices you made in this daring adventure.
""")

    #invailid input
    else:
      write("""You look around confused as to 
what you were trying to do.""")

  return inventory


# Game not started (Making sure bg appears first)
game_started = False

# Game loop
while True:
  if not game_started:
    # Making sure bg appears first
    #pygame.display.update()
    game_started = True
    screen.blit(bg_surface, (0, 0))

	#setting up text input
  getInputText()

  #Begining the loop of def functions
  play_game()
  meeting_room(inventory)

  #Update the screen
  pygame.display.update()
