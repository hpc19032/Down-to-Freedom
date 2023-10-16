#Importing functions
import sys
import pygame
import time

# Initializing pygame
pygame.init()
pygame.font.init()

# Setting screen
screen = pygame.display.set_mode([280, 343])

#Loading images
bg_surface = pygame.image.load('Assets/Background.png')
r_keycard = pygame.image.load('Assets/Red_Keycard.jpg')
o_keycard = pygame.image.load('Assets/Orange_Keycard.jpg')
crowbar = pygame.image.load('Assets/Crowbar.png')
m_office_map = pygame.image.load('Assets/Managers Office.png')
closet_map = pygame.image.load('Assets/Closet.png')
meeting_room_map = pygame.image.load('Assets/Meeting Room.png')
office_map = pygame.image.load('Assets/Office.png')
reception_map = pygame.image.load('Assets/Reception.png')
lobby_map = pygame.image.load('Assets/Lobby.png')

#Setting title
pygame.display.set_caption("Down to Freedom")
screen.blit(bg_surface, (0, 0))
screen.fill((243,255,255))

#settinginput box variables
font = pygame.font.SysFont("dejavusans", 20)  
clock = pygame.time.Clock()
user_text = ''
input_rect = pygame.Rect(15,288,244,39)
colour = (170,170,170)

# keeping track of room for game loop
room = "play_game"

#setting inventory
global inventory
inventory = []

#keeping track of amount of time in each room
global meeting_time
meeting_time = 0
global reception_time
reception_time = 0
global closet_time
closet_time = 0
global office_time
office_time = 0
global m_office_time
m_office_time = 0
global lobby_time
lobby_time = 0

#Rendering text
def write(text):
	
	font = pygame.font.SysFont("dejavusans", 9)  

 	#setting position of each line
	y = 45
	x = 20

 	#Splitting text iinto lines so next bit works
	lines = text.split('\n')

	# Rendering each line
	for line in lines:
		story_surface = font.render(line, True, (0, 0, 0))
		screen.blit(story_surface, (x, y))
		y += 9
		pygame.display.update()
			
	
# meeting_room
def meeting_room():

	screen.blit(meeting_room_map, (158,20))
		
	# varible used to determine if player has been in room before
	global meeting_time
	if meeting_time == 0:
		
  	#text for entering room first time
		screen.blit(bg_surface, (0, 0))
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

	#	Alternative text when entering room for second time
	else:
		screen.blit(bg_surface, (0, 0))
		write("""You have just 
entered the Meeting 
Room, Nothing has 
changed since you 
were last in here.""")


#Defining reception
def reception(inventory):

	screen.blit(reception_map, (158,20))


 	#varible to determine if player has been in room before
	global reception_time
	if reception_time == 0:


   	#Text for entering room for first time
		write("""After using the red 
key card on the door, 
you find yourself 
standing in a basic 
reception area. The 
room is modestly lit, with 
a single overhead light 
casting a glow upon a reception 
desk that stands before you. 
 
Four doors stand out from the 
off-white of each wall:
 - To the north, a door, slightly 
   ajar, sits within the center of 
   the wall, giving you a glimps 
   of an office inside.
 - In the opposite direction, to 
   the south, an extremely worn 
   door sits shrouded in shadows.
 - On the east wall, a large lobby 
   like hallway sits.
 - To the west is the wide 
   open door that leads back to 
   the meeting room.""")

		reception_time = 1

  	#Alternative text when entering room for second time
	else:

		write("""You have just 
entered the 
Reception, Nothing 
has changed since 
you were last here.""")

	while True:
		#setting input box to work

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
		elif movement not in ['move east', 'move west', 'move south', 'move north', '']:
			write("""You look around 
confused as to what 
you were trying to do.""")

		pygame.display.update()
	return inventory


def closet(inventory):

	screen.blit(closet_map, (158,20))


		
 	#Determining if player has been in room before
	global closet_time
	if closet_time == 0:

   	#text for entering room for first time.
		write("""A faint scent of 
cleaning supplies 
greets your senses 
as you push open the 
worn door to the room. The 
door bangs against 
something plastic as you 
step into the room, the sound 
echoing through the small 
room. The room is dimly lit, 
with a solitary overhead bulb 
casting elongated shadows 
across the cluttered shelves. 
Among the clutter, a 
“crowbar” seems both out of 
place and yet perfectly at 
home; a juxtaposition that 
beckons your consideration. 
Its promise of strength and 
adaptability hints at its 
potential usefulness in your 
journey, a silent companion in 
the midst of this unexpected 
adventure.""")

		closet_time = 1

 	#Alternative text when entering room for second time.
	else:

		write("""You have just entered 
the Janitors Closet, 
Nothing has changed 
since you were last 
in here.""")

	while True:
		#setting input box to work

		movement = movement.strip().lower()

   	#attempting to move an invalid direction
		if movement == "move east" or movement == "move south" or movement == "move west":

			write("""As much as you may 
wish to go in that 
direction, there is 
no door there.""")

   	#Moving back to reception
		elif movement == "move north":

			reception(inventory)

   	#picking up crowbar
		elif movement == "pickup crowbar":

			inventory.append("crowbar")
			screen.blit(crowbar, (193, 130))
			write("""Reaching down you 
pick up the crow bar 
from where it rests 
on the ground, the 
worn metal rests 
heavy in your hands as 
you stand up once more 
ready to continue your 
adventure. """)

   	#incorrect input
		elif movement not in ['move east', 'move west', 'move south', 'move north', 'pickup crowbar','']:

			write("""You look around 
confused as to what 
you were trying to do.""")

		pygame.display.update()
	return inventory


#Office
def office(inventory):

	screen.blit(office_map, (158,20))
	
		
	#been in room before?
	global office_time
	if office_time == 0:


   	#entering room for first time
		write("""Shoving the door 
open as it resists 
your effort, you step 
into a cluttered 
office, where the air 
is tinged with the 
scent of paper, ink,
and a hint of abandoned 
coffee cups. The room is 
dimly lit by the glow of 
fluorescent lights hanging 
overhead, casting a pale 
illumination over the chaos 
that surrounds you. Desk 
spaces are strewn with 
stacks of paper, half-empty 
notebooks, and forgotten 
office supplies.  A lone door 
to the west beckons your 
attention, its surface covered 
with various notes and memos, 
a testament to the hurried pace 
of office life.""")

		office_time = 1

 	#Alternative text wehn entering room not for first time
	else:

		write("""You have just 
entered the Office, 
Nothing has changed 
since you were last 
here.""")

	while True:
		#setting input box to work

		movement = movement.strip().lower()

		#attempting to move in invalid direction
		if movement == "move north" or movement == "move east":

			write("""As much as you may 
wish to go in that 
direction, there is 
no door there.""")

  	#moveing to managers office
		elif movement == "move west":

			m_office(inventory)

   	#moveing back to reception
		elif movement == "move south":

			reception(inventory)

   	#invalid input
		elif movement not in ['move east', 'move west', 'move south', 'move north', '']:

			write("""You look around 
confused as to what 
you were trying to do.""")

		pygame.display.update()
	return inventory


def m_office(inventory):

	screen.blit(m_office_map, (158,20))
	

		
 	#Varible to determind if player been in roome before
	global m_office_time
	if m_office_time == 0:


   	#enterng room for first time
		write("""Pushing the door 
open you step into 
the room that seems 
to be a manager or 
supervisors office, the air 
is thick with a mix of aged 
leather, paper, and a faint 
hint of stale coffee. Dim light 
filters through partially
closed blinds, casting elongated 
shadows across stacks of 
documents and half-opened file 
cabinets. The manager's desk is 
a chaotic symphony of organized 
chaos. Piles of paperwork 
intermingle with scattered 
stationery and tangled cords 
from various electronic devices. 
Amidst the clutter, a worn 
“orange key card” stands out 
on the corner of the desk.""")

		m_office_time = 1


#entering room for secnd time
	else:

		write("""You have just 
entered the Manager's 
Office, nothing has 
changed since you were 
last in here.""")

	while True:
		#setting input box to work

		movement = movement.strip().lower()

   	#attempting to move in invalid direction
		if movement == "move north" or movement == "move south" or movement == "move west":

			write("""As much as you may 
wish to go in that 
direction, there is 
no door there.""")

   	#Moving back to office
		elif movement == "move east":

			office(inventory)

   	#Picking up keycard
		elif movement == "pickup orange keycard":

			inventory.append("orange_keycard")
			screen.blit(o_keycard, (193, 200))
			write("""Carefully avoiding 
the chaos on the 
desk you pick up the 
worn orange keycard 
and place it in your 
pocket. Perhaps it could 
be useful in the future.""")

   	#incorrect input
		elif movement not in ['move east', 'move west', 'move south', 'move north', 'pickup orange keycard','']:

			write("""You look around 
confused as to what 
you were trying to do.""")

		pygame.display.update()
	return inventory


def lobby(inventory):
	
	screen.blit(lobby_map, (158,20))
	

	#has player been in roome before
	global lobby_time
	if lobby_time == 0:


   	#first time in room
		write("""You stand in a 
elevator lobby, the 
air stagnant with a 
faint scent of old 
machinery and dust. Two 
elevators occupy the 
space before you. One 
stands silently, its doors 
wide open, revealing a hollow 
shaft beyond. This elevator 
appears to be out of commission, 
its buttons unlit and its interior 
shrouded in darkness. Beside it, 
the second elevator is a stark 
juxtaposition. Its doors are 
tightly boarded up, secured with 
weathered wooden planks 
Despite its appearance, 
a subtle hum emanates from 
behind the barricade, suggesting 
that it's still operational. 
Beside both elevators sits two 
more keypads, these one 
emanating a subtle orange 
glow.""")

		lobby_time = 1

	else:

		write("""You have just 
entered the
Elevator Lobby, 
Nothing has changed 
since you were last 
in here.""")

	while True:
		#setting input box to work

		movement = movement.strip().lower()

		if movement == "move south" or movement == "move north" or movement == "move east":

			write("""As much as you may 
wish to go in that 
direction, there is 
no door there.""")

   	#Meving back to reception
		elif movement == "move west":
 
			reception(inventory)

		elif "orange_keycard" in inventory and "crowbar" in inventory:

			write("""Anticipation hangs 
in the air as you 
stand in the elevator 
lobby for the final time, 
your heart pounding in tandem 
with the hum of the operational 
elevator. The boarded-up elevator 
door before you seems like the final 
hurdle, and the crowbar you found has 
proven invaluable.

Gripping the crowbar tightly, 
you bring it down with determined 
force against the wooden boards. The
sound of splintering wood sends a rush 
of triumph through you as the path to 
the operational elevator is now clear.
Moving to your left as you pull the green
keycard out of where it resided in your pocket, 
picking it up was one of the best decisions 
you have ever made. As you swipe the keycard 
it beeps with a finality that resonates 
throught you. A sense of anticipation 
entering the air as you step into the 
elevator. As you press the button for 
the ground floor, the elevator begins 
its descent. 

With a gentle jolt, the elevator 
comes to a stop. The doors slide open, 
revealing a world beyond the building's 
confines. """)

    	#invailid input
		elif movement not in ['move east', 'move west', 'move south', 'move north', '']:

			write("""You look around 
confused as to what 
you were trying to do.""")
			
		pygame.display.update()
	return inventory

while True:
	
	# taking input from input box/ making it work
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:				
			pygame.quit()
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			
			if event.key == pygame.K_BACKSPACE:
				user_text = user_text[:-1]
				
			elif event.key == pygame.K_RETURN:
				input = ""
				user_text = user_text.strip().lower()
				input = user_text
				user_text = ""
				
			else:
				user_text += event.unicode
				if text_surface.get_width() > input_rect.w -20:
					user_text = user_text[:-1]
		
		# would you like to play the game/intro
		if room == "play_game":
			screen.blit(bg_surface, (0, 0))
			write("""Welcome to Down 
to Freedom, would 
you like to begin your 
adventure?""")

			if input == 'yes'or input == 'y':
				screen.blit(bg_surface, (0, 0))
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
  "Move East".
 
(Press any key to continue)""")

				#waiting for key press to move on
				waiting_for_keypress = True
				while waiting_for_keypress:
					for event in pygame.event.get():
						if event.type == pygame.KEYDOWN:
							waiting_for_keypress = False

				screen.blit(bg_surface, (0, 0))
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
come into play seamlessly.

(Press any key to continue)""")

				# waiting for key press to move on
				waiting_for_keypress = True
				while waiting_for_keypress:
					for event in pygame.event.get():
						if event.type == pygame.KEYDOWN:
							waiting_for_keypress = False

				room = "meeting_room"

			elif input == 'n' or input == 'no':
				screen.blit(bg_surface, (0, 0))
				write("""You gaze into the 
light as your one 
chance of escaping 
leaves.""")

				# waiting for user to read
				pygame.time.wait(4000)

				# Quitting game
				pygame.quit()
				sys.exit()
			
	# Meeting room
	if room == "meeting_room":
		meeting_room()
		
		# attempting to move an invalid direction
		if input == "move north" or input == "move south" or input == "move west":

			screen.blit(bg_surface, (0, 0))
			write("""As much as you may 
wish to go in that 
direction, there is 
no door there.""")

	# attempting to leave without a keycard.
		elif input == "move east" and "red_keycard" not in inventory:

			screen.blit(bg_surface, (0, 0))
			write("""You walk over to
the door, ignoring 
the keypad and 
attempt to pull open 
the door. Despite your 
best efforts it refuses 
to budge, giving up, you 
look around the room 
for another solution.""")

		# Picking up keycard
		elif input == "pickup red keycard":

			inventory.append("red_keycard")
			screen.blit(r_keycard, (193, 240))
			screen.blit(bg_surface, (0, 0))
			write("""You slide the red 
keycard off the table 
and into your hand 
disturbing the dust as 
you pick it up and place 
it in your pocket for future 
use.""")

		# moving to reception when requirements met
		elif input == "move east" and "red_keycard" in inventory:
			room = "reception"

		# invailid input
		elif input not in ['move east', 'move west', 'move south', 'move north', 'pickup red keycard', '']:

			screen.blit(bg_surface, (0, 0))
			write("""You look around 
confused as to what 
you were trying to do.""")


	pygame.draw.rect(screen,colour,input_rect)
	
	text_surface = font.render(user_text, True, (0,0,0))
	screen.blit(text_surface,(input_rect.x + 5, input_rect.y + 7))
  #Update the screen
	pygame.display.update()

	clock.tick(60)