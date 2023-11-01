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
bg_surface = pygame.image.load('Assets/Background .bmp')
r_keycard = pygame.image.load('Assets/Red Key Card.bmp')
o_keycard = pygame.image.load('Assets/Orange Keycard.bmp')
crowbar = pygame.image.load('Assets/CrowBar.bmp')
note = pygame.image.load('Assets/Note.bmp')
m_office_map = pygame.image.load('Assets/Managers office map.bmp')
closet_map = pygame.image.load('Assets/Janitors closet map.bmp')
l_meeting_map = pygame.image.load('Assets/Large Meeting Room Map.bmp')
office_map = pygame.image.load('Assets/Office map .bmp')
reception_map = pygame.image.load('Assets/Reception Map.bmp')
lobby_map = pygame.image.load('Assets/Lobby Map.bmp')
break_map = pygame.image.load('Assets/Break Room map.bmp')
hallway_map = pygame.image.load('Assets/Hallway Map.bmp')
meeting_map_one = pygame.image.load('Assets/Small Meeting Room One.bmp')
meeting_map_two = pygame.image.load('Assets/Small Meeting Room Two map.bmp')
Main_map = pygame.image.load('Assets/Main Map Circle.bmp')

#Setting title
pygame.display.set_caption("Down to Freedom")
screen.blit(bg_surface, (0, 0))
screen.fill((243,255,255))

font_name = "dejavusans"  # Font name
font_size = 18  # Font size

# Create a font object
font = pygame.font.Font(None, font_size)
clock = pygame.time.Clock()
user_text = ''
active = ''
input_rect = pygame.Rect(15,288,224,39)
colour_passive = (170,170,170)
colour_active = (200,200,200)
colour_incorrect = (255,64,64)

# keeping track of room for game loop
room = "play_game"

loop = 1

#setting inventory
global inventory
inventory = []

#keeping track of amount of time in each room
l_meeting_time = 0
reception_time = 0
closet_time = 0
office_time = 0
m_office_time = 0
lobby_time = 0
break_time = 0
meeting_one_time = 0
meeting_two_time = 0
hallway_time = 0

#Rendering text
def write(text):
	
	font_name = "dejavusans"  # Font name
	font_size = 9  # Font size

	# Create a font object
	font = pygame.font.Font(None, font_size)

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
		#write('\033[1m Your Name \033[0m')


while True:
	
	# taking input from input box/ making it work
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:				
			pygame.quit()
			sys.exit()

		elif event.type == pygame.MOUSEBUTTONDOWN:
			if input_rect.collidepoint(event.pos):
				active = True
			else:
				active = False

		elif event.type == pygame.KEYDOWN:
			if active == True:
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
			if loop == 1:
				loop = 2
				screen.blit(Main_map, (158,20))
				screen.blit(bg_surface, (0, 0))
				write("""Welcome to Down 
to Freedom, would 
you like to begin your 
adventure?

(Enter your answer into the 
box below)""")

			if input == 'yes'or input == 'y':
				screen.blit(bg_surface, (0, 0))
				write("""Within this 
adventure your 
keyboard is your 
guide. 

To journey from room to 
room use one of the
following commands. 

- "Move West"

- "Move South"

- "Move North"

- "Move East"

or if these directions are
not enough for your exploration
throughout this adventure use.

- "Move South West"
 
(Press space to continue)""")

					# waiting for key press to move on
				waiting_for_keypress = True
				while waiting_for_keypress:
					for event in pygame.event.get():
						if event.type == pygame.KEYDOWN:	
							if event.key == pygame.K_SPACE:
								waiting_for_keypress = False
								screen.blit(bg_surface, (0, 0))
							
				write("""Furthermore, to 
pickup an item, use 
the command:

"Pickup" 

followed by the name 
of the item exactly as 
it is described in the 
room description.

Throughout this adventure, 
items will come into play 
automatically; When moving
in the correct direction.

If you need a refresher of 
these rules at any point
simply type 

"Rules".

(Press Space to continue)""")

				# waiting for key press to move on
				waiting_for_keypress = True
				while waiting_for_keypress:
					for event in pygame.event.get():
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_SPACE:
								waiting_for_keypress = False
								screen.blit(bg_surface, (0, 0))

				loop = 1
				room = "l_meeting_room"

			elif input == 'n' or input == 'no':
				screen.blit(bg_surface, (0, 0))
				write("""You gaze into the 
distance as your one 
chance of escaping 
leaves.""")

				# waiting for user to read
				pygame.time.wait(4000)

				# Quitting game
				pygame.quit()
				sys.exit()


	
	# Meeting room
	if room == "l_meeting_room":
		# varible used to determine if player has been in room before
		if loop == 1:
			loop = 2
			screen.blit(l_meeting_map, (158,20))
			screen.blit(bg_surface, (0, 0))
			if l_meeting_time == 0:
		
				# text for entering room first time
				write("""You come to find 
yourself in a dimly 
lit meeting room. Tall, 
imposing windows 
stretch from floor to 
ceiling along one wall. 
A city skyline is visible 
beyond the glass. The room 
is dominated by a large, 
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
card's presence.""")

			#	Alternative text when entering room for second time
			else:
				screen.blit(bg_surface, (0, 0))
				write("""You once more  
find yourself in a large 
dimly lit meeting 
room. The room remains 
dominated by the 
large, wooden table a 
smudge of dust missing
from the courner where
the Red Keycard once 
rested.""")
				
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:

				# attempting to pick up an invalid item
				if input in ['move west', 'move south', 'move north', 'pickup crowbar', 'pickup orange keycard', 'move north east', 'move north west', 'move south east', 'move south west', 'pickup note', '']:
					colour == colour_incorrect

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
for another solution.

(Press space to coninue)""")

					waiting_for_keypress = True
					while waiting_for_keypress:
						for event in pygame.event.get():
							if event.type == pygame.KEYDOWN:
								if event.key == pygame.K_SPACE:
									waiting_for_keypress = False
									screen.blit(bg_surface, (0, 0))

					screen.blit(bg_surface, (0, 0))
					write("""You remain
in a dimly 
lit meeting room. Tall, 
imposing windows 
stretch from floor to 
ceiling along one wall. 
The room is dominated 
by a large, dusty 
wooden meeting table. 
On the table lies a 
“red keycard”, 
its edges catching what 
little light is available. 
Across the room to the 
east a majestic set of 
double doors are seamlessly 
embedded in the pale off-white 
of the surrounding walls. Next 
to this door, a card reader 
is affixed to the wall, a 
pulsating red light upon it, 
signals the need for a
card's presence.""")

				# Picking up keycard
				elif input == "pickup red keycard":

					inventory.append("red_keycard")
					screen.blit(r_keycard, (287, 238.5))
					screen.blit(bg_surface, (0, 0))
					write("""You slide the red 
keycard off the table 
and into your hand 
disturbing the dust as 
you pick it up and place 
it in your pocket for future 
use.

(Press Space to continue)""")

					waiting_for_keypress = True
					while waiting_for_keypress:
						for event in pygame.event.get():
							if event.type == pygame.KEYDOWN:
								if event.key == pygame.K_SPACE:
									waiting_for_keypress = False
									screen.blit(bg_surface, (0, 0))

					screen.blit(bg_surface, (0, 0))
					write("""You remain
in a dimly 
lit meeting room. Tall, 
imposing windows 
stretch from floor to 
ceiling along one wall. 
The room is dominated 
by a large, dusty 
wooden meeting table. 
On the table lies a 
“red keycard”, 
its edges catching what 
little light is available. 
Across the room to the 
east a majestic set of 
double doors are seamlessly 
embedded in the pale off-white 
of the surrounding walls. Next 
to this door, a card reader 
is affixed to the wall, a 
pulsating red light upon it, 
signals the need for a
card's presence.""")

				# moving to reception when requirements met
				elif input == "move east" and "red_keycard" in inventory:
					l_meeting_time = 1
					loop = 1
					input = ""
					room = "reception"



	# Reception
	if room == "reception":
		
		#varible to determine if player has been in room before
		if loop == 1:
			loop = 2
			screen.blit(reception_map, (158,20))
			screen.blit(bg_surface, (0, 0))
			if reception_time == 0:

				#Text for entering room for first time
				screen.blit(bg_surface, (0, 0))
				write("""After using the red 
key card on the door, 
you find yourself 
standing in a basic 
reception area. A single 
overhead light casting a 
glow upon a reception desk 
that stands before you. 

Five doors stand out from the 
off-white of the walls:

- To the north, a door is slightly 
  ajar, giving you a glimps 
  of the office beyond.
- To the south, an extremely 
  worn door sits in shadows.
- On the east wall, large glass
  doors are set into the wall, 
  showing the lobby beyond.
- To the west the large wooden 
  doors remain open.
- To the south west a door sits 
  slightly ajar showing a 
  hallway beyond.""")			

			#Alternative text when entering room for second time
			else:
				screen.blit(bg_surface, (0, 0))
				write("""You once more find
yourself in the 
reception.

Five doors continue
to lead from the room:

- To the north, a door 
  is slightly ajar, 
  giving you a glimps 
  of the office beyond.
- To the south, an 
  extremely worn door sits 
	in shadows.
- On the east wall, large glass
  doors are set into the wall, 
  showing the lobby beyond.
- To the west the large wooden 
  doors remain open.
- To the south west a door sits 
  slightly ajar showing a 
  hallway beyond.""")
				
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:

				if input in ['pickup crowbar', 'pickup orange keycard', 'pickup red keycard', 'move north east', 'move north west', 'move south east', 'pickup note', '']:
					colour == colour_incorrect

				# Moveing to closet
				elif input == "move south":
					input = ""
					reception_time = 1
					loop = 1
					room = "closet"

				#Moveing to lobby
				elif input == "move east":
					input = ""
					reception_time = 1
					loop = 1
					room = "lobby"

				#moving back to meeting room
				elif input == "move west":
					input = ""
					reception_time = 1
					loop = 1
					room = "l_meeting_room"

				#moving to the office
				elif input == "move north":
					input = ""
					reception_time = 1
					loop = 1
					room = "office"

				# moving to hallway
				elif input == "move south west":
					input = ""
					reception_time = 1
					loop = 1
					room = "hallway"



	# Hallway
	if room == "hallway":
		if loop == 1:
			loop = 2
			screen.blit(Hallway_map, (158,20))
			screen.blit(bg_surface, (0, 0))
			if hallway_time == 0:

				#	text for entering room for first time.
				screen.blit(bg_surface, (0, 0))
				write("""You stand in an old, 
dimly lit hallway, 
its worn-out carpet 
muffled underfoot as 
you survey your 
surroundings. The walls, 
once a vibrant color, have 
faded over time, and the 
ceiling tiles are stained 
and sagging. To the east and 
west, there are double doors 
leading to old, forgotten 
meeting rooms. The glass doors 
of these rooms are dusty, and 
their interiors are shrouded in
a gloomy stillness. As you 
approach the end of the hallway, 
you spot a final door, seemingly 
impossible to open. It appears 
to have been broken from the 
other side, ensuring no escape. 
A chilling thought creeps in
— perhaps it was the work of the 
one who trapped you in this 
eerie place.""")

			# Alternative text when entering room for second time.
			else:
				screen.blit(bg_surface, (0, 0))
				write("""You stand once more, 
in the hallway, 
To the east and west, 
there are double doors 
leading to small 
meeting rooms.""")

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:

				# attempting to pickup random item
				if input in ['move east', 'move south','pickup crowbar', 'pickup orange keycard', 'pickup red keycard', 'move north east', 'move north west', 'move south east', 'move south west' 'pickup note', '']:
					colour == colour_incorrect

				# Moving back to reception
				elif input == "move north":
					input = ""
					hallway_time = 1
					loop = 1
					room = "reception"

				# Moving to meeting room 1
				elif input == "move west":
					input = ""
					hallway_time = 1
					loop = 1
					room = "meeting_room_one"

				# Moving to meeting room 1
				elif input == "move east":
					input = ""
					hallway_time = 1
					loop = 1
					room = "meeting_room_two"


	# meeting room one
	if room == "meeting_room_one":
		
		if loop == 1:
			loop = 2
			screen.blit(Meeting_map_one, (158,20))
			screen.blit(bg_surface, (0, 0))
			if meeting_one_time == 0:
				write("""You step into 
a small, abandoned 
meeting room, its 
decaying charm 
immediately evident. Dust 
hangs in the air like a 
spectral mist, and faded 
sunlight filters through grimy 
windows, casting feeble beams 
on a once-polished wooden table 
at the room's center. The 
chairs surrounding it are 
tattered and their upholstery 
worn, bearing witness to years 
of forgotten discussions. The 
glass double doors that stand 
at one end are cloudy, their 
frosted surface obscuring any 
view beyond.""")

			# Alternative text when entering room for second time.
			else:
				screen.blit(bg_surface, (0, 0))
				write("""You step into 
a small, meeting 
room, a once-polished 
wooden table at the 
room's center.""")

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:

				# attempting to pickup random item
				if input in ['move west', 'move north' 'move south','pickup crowbar', 'pickup orange keycard', 'pickup red keycard', 'move north east', 'move north west', 'move south east', 'move south west', 'pickup note', '']:
					colour == colour_incorrect

				# Moving back to reception
				elif input == "move east":
					input = ""
					closet_time = 1
					loop = 1
					room = "hallway"



	# meeting room one
	if room == "meeting_room_two":
		
		if loop == 1:
			loop = 2
			screen.blit(Meeting_map_two, (158,20))
			screen.blit(bg_surface, (0, 0))
			if meeting_two_time == 0:
				
				write("""You cautiously 
enter a small, 
forsaken meeting 
room. The air is 
stagnant, as if the room's 
stories have been trapped 
inside for ages. Dominating 
the space, an old wooden table 
rests in the center. The 
chairs surrounding it are worn 
and frayed, silent observers 
of forgotten gatherings. The 
glass double doors that led 
you here are misted, making the 
world beyond appear distant 
and detached. On the table, a 
singular item draws your 
attention — a "note", its crisp 
edges contrasting with the 
room's decay. The room, devoid 
of windows, seems to focus 
your attention even more 
intentlyon this mysterious 
piece of paper, beckoning you 
to discover its message.""")

			elif "note" in inventory:
				screen.blit(bg_surface, (0, 0))
				write("""You once more 
enter one of the 
small meeting rooms,
The air is a little
less stagnet that it
was. The table remains
in the center of the
room """)
				
			# Alternative text when entering room for second time.
			else:
				screen.blit(bg_surface, (0, 0))
				write("""You once more 
enter one of the 
small meeting rooms,
The air is a little
less stagnet that it
was. The table remains
in the center of the
room. On the table, a 
singular item draws your 
attention — a "note", its crisp 
edges contrasting with the 
room's decay. The room, devoid 
of windows, seems to focus 
your attention even more 
intentlyon this mysterious 
piece of paper, beckoning you 
to discover its message.""")

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:

				# attempting to pickup random item
				if input in ['move east', 'move north' 'move south','pickup crowbar', 'pickup orange keycard', 'pickup red keycard', 'move north east', 'move north west', 'move south east', 'move south west', '']:
					colour == colour_incorrect

				# Moving back to hallway
				elif input == "move west":
					input = ""
					meeting_two_time = 1
					loop = 1
					room = "hallway"

				elif input == "pickup note":
					input = ""
					screen.blit(note, (287, 159.5))
					screen.blit(bg_surface, (0, 0))
					write("""You slide the 
note off the table 
into the palm of your 
hand, feeling the sharp 
spike of pain as the paper 
stabs you, reminding you 
once more just how out of 
place it is. Curiosity 
getting the better of you, 
you begin to read.

“You thought I had forgotten 
what you did, you thought it 
no longer mattered, but I never 
forgot, never stopped thinking 
about how you ruined my life. 
Were it not for you I would be 
off living a happy life, but no 
you had to interfere. So here I 
leave you to be forgotten, to die 
a slow and painful death like you 
deserve. 

Bitterly yours,
The one who never forgot.” """)
					
					

	# closet
	if room == "closet":
		
		if loop == 1:
			loop = 2
			screen.blit(closet_map, (158,20))
			screen.blit(bg_surface, (0, 0))
			if closet_time == 0:

				#	text for entering room for first time.
				
				write("""A strong scent of 
cleaning supplies 
greets your senses 
as you push open the 
worn door to the room. The 
door bangs against 
something plastic as you 
step into the room, the sound 
echoing through the small 
space. A solitary overhead bulb 
casting elongated shadows 
across the cluttered shelves. 
Among the clutter, a 
“crowbar” seems both out of 
place and yet perfectly at 
home; a juxtaposition that 
beckons your consideration.""")

			# Alternative text when entering room for second time.
			else:
				screen.blit(bg_surface, (0, 0))
				write("""You have just 
entered the Janitors 
Closet, Nothing has 
changed since you were 
last in here.""")
				
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:

				# attempting to pickup invalid item
				if input == "pickup orange keycard" or input == "pickup red keycard" or input == "pickup note":
					screen.blit(bg_surface, (0, 0))
					write("""You look around but
				there seems to be no
				such object in this room""")

				# attempting to move an invalid direction
				elif input == "move east" or input == "move south" or input == "move west" or input == "move north east" or input == " move north west" or input == "move south west" or input == "move south west":

					screen.blit(bg_surface, (0, 0))
					write("""As much as you may 
wish to go in that 
direction, there is 
no door there.""")

				# Moving back to reception
				elif input == "move north":
					input = ""
					closet_time = 1
					loop = 1
					room = "reception"
					
				# picking up crowbar
				elif input == "pickup crowbar":

					inventory.append("crowbar")
					screen.blit(crowbar, (287, 120))
					screen.blit(bg_surface, (0, 0))
					write("""Reaching down you 
pick up the crow bar 
from where it rests 
on the ground, the 
worn metal rests 
heavy in your hands as 
you stand up once more 
ready to continue your 
adventure. """)



	# Break Room:
	if room == "break_room":

		if loop == 1:
			loop = 2
			screen.blit(break_map, (158,20))
			screen.blit(bg_surface, (0, 0))
			if break_time == 0:

				# entering room for first time
				
				write("""You nuge the door 
open and step into 
the worn and dusty 
room, now just a 
shadow of the haven it 
once was, It's small, worn, 
and dusty. The linoleum floor 
is scuffed, lockers are dented, 
and chairs are mismatched and 
shabby. A bulletin board 
displays outdated office memos, 
and a neglected plastic plant 
sits on a windowsill. There's 
a cracked table with crumbs 
and coffee stains, and a 
humming refrigerator adorned 
with old stickers. A grimy
window offers a glimpse of the 
bustling office world outside, 
the room forgotten by all those 
who once graced its halls.""")

			# Alternative text when entering room not for first time
			else:
				screen.blit(bg_surface, (0, 0))
				write("""You have just 
entered the Break
room, Nothing has 
changed since you 
were last here.""")

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:

				# attempting to pickup random item
				if input == "pickup orange keycard" or input == "pickup crowbar" or input == "pickup red keycard" or input == "pickup note":
					screen.blit(bg_surface, (0, 0))
					write("""You look around but
there seems to be no
such object in this room""")

				# attempting to move in invalid direction
				elif input == "move north" or input == "move east" or input == "move south" or input == "move north east" or input == " move north west" or input == "move south west" or input == "move south west":
					screen.blit(bg_surface, (0, 0))
					write("""As much as you may 
wish to go in that 
direction, there is 
no door there.""")

				# moveing to office
				elif input == "move west":
					input = ""
					break_time = 1
					loop = 1
					room = "office"


	
	# office
	if room == "office":

		if loop == 1:
			loop = 2
			screen.blit(office_map, (158,20))
			screen.blit(bg_surface, (0, 0))
			if office_time == 0:

				# entering room for first time
				
				write("""Shoving the door 
open, you step into 
a cluttered office, 
where the air is 
tinged with the scent 
of paper, ink, and a hint 
of abandoned coffee cups. 
The room is dimly lit by the 
glow of fluorescent lights 
hanging overhead, casting a 
pale illumination over the chaos 
that surrounds you. Desk 
spaces are strewn with 
stacks of paper, half-empty 
notebooks, and forgotten 
office supplies. The two 
doors present within the office
seemingly counterbalance 
eachother as they sit perfectly 
opposite. The one to the east 
showing the clutter of a break 
room, while the other continues 
to show the hectic life of the
office, on the desk within.""")

			# Alternative text when entering room not for first time
			else:
				screen.blit(bg_surface, (0, 0))
				write("""You have just 
entered the Office, 
Nothing has changed 
since you were last 
here.""")

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:

				# attempting to pick up invalid item
				if input == "pickup orange keycard" or input == "pickup crowbar" or input == "pickup red keycard" or input == "pickup note":
					screen.blit(bg_surface, (0, 0))
					write("""You look around but
there seems to be no
such object in this room""")
				
				# attempting to move in invalid direction
				elif input == "move north" or input == "move north east" or input == " move north west" or input == "move south west" or input == "move south west":
					screen.blit(bg_surface, (0, 0))
					write("""As much as you may 
wish to go in that 
direction, there is 
no door there.""")

				# moveing to managers office
				elif input == "move west":
					input = ""
					office_time = 1
					loop = 1
					room = "m_office"

				# moveing back to reception
				elif input == "move south":
					input = ""
					office_time = 1
					loop = 1
					room = "reception"

				# moving to break room
				elif input == "move east":
					input = ""
					office_time = 1
					loop = 1
					room = "break_room"


	
	# managers office
	if room == "m_office":

		if loop == 1:
			loop = 2
			screen.blit(m_office_map, (158,20))
			screen.blit(bg_surface, (0, 0))
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

			# entering room for secnd time
			else:
				screen.blit(bg_surface, (0, 0))
				write("""You have just 
entered the Manager's 
Office, nothing has 
changed since you were 
last in here.""")

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:

				# attempting to pickup invalid item
				if input == "pickup red keycard" or input == "pickup crowbar" or input == "pickup note":
					screen.blit(bg_surface, (0, 0))
					write("""You look around but
				there seems to be no
				such object in this room""")
				
				#attempting to move in invalid direction
				elif input == "move north" or input == "move south" or input == "move west" or input == "move north east" or input == " move north west" or input == "move south west" or input == "move south west":
					screen.blit(bg_surface, (0, 0))
					write("""As much as you may 
wish to go in that 
direction, there is 
no door there.""")

				# Moving back to office
				elif input == "move east":
					input = ""
					m_office_time = 1
					loop = 1
					room = "office"

				# Picking up keycard
				elif input == "pickup orange keycard":
					inventory.append("orange_keycard")
					screen.blit(o_keycard, (287, 199))
					screen.blit(bg_surface, (0, 0))
					write("""Carefully avoiding 
the chaos on the 
desk you pick up the 
worn orange keycard 
and place it in your 
pocket. Perhaps it could 
be useful in the future.""")



	# Lobby
	if room == "lobby":

		if loop == 1:
			loop = 2
			screen.blit(lobby_map, (158,20))
			screen.blit(bg_surface, (0, 0))

			if "orange_keycard" in inventory and "crowbar" in inventory:
				
				write("""Anticipation hangs 
in the air as you 
stand in the elevator 
lobby for the final time.
The boarded-up elevator
door before you seems 
like the final hurdle.

Gripping the crowbar tightly, 
you bring it down with 
determined force against the 
wooden boards splintering them. 
Moving to your left as you pull 
the green keycard out of where 
it resided in your pocket.
As you swipe the keycard it 
beeps with a finality that 
resonates throught you. A 
sense of anticipation entering 
the air as you step into the 
elevator. 

(Press space to continue)""")

				# waiting for key press to move on
				waiting_for_keypress = True
				while waiting_for_keypress:
					for event in pygame.event.get():
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_SPACE:
								waiting_for_keypress = False
								screen.blit(bg_surface, (0, 0))

				write("""With a gentle jolt, 
the elevator comes 
to a stop and your 
adventure come to an 
end.

Thank you for playing, I hope 
you enjoyed your 
adventure""")

				# waiting for user to read
				pygame.time.wait(8000)

				# Quitting game
				pygame.quit()
				sys.exit()
			
			if lobby_time == 0:

				#first time in room
				screen.blit(bg_surface, (0, 0))
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
														
			else:
				screen.blit(bg_surface, (0, 0))
				write("""You have just 
entered the
Elevator Lobby, 
Nothing has changed 
since you were last 
in here.""")

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:

				# attempting to pickup an item not in room
				if input == "pickup orange keycard" or input == "pickup crowbar" or input == "pickup red keycard" or input == "pickup note":
					screen.blit(bg_surface, (0, 0))
					write("""You look around but
				there seems to be no
				such object in this room""")

				if input == "move south" or input == "move north" or input == "move east":
					screen.blit(bg_surface, (0, 0))
					write("""As much as you may 
wish to go in that 
direction, there is 
no door there.""")

				#Moving back to reception
				elif input == "move west":
					input = ""
					lobby_time = 1
					loop = 1
					room = "reception"



	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_RETURN and room != "play_game":
			#incorrect input
			if input not in ['move east', 'move west', 'move south', 'move north', 'pickup crowbar', 'pickup red keycard', 'pickup orange keycard', 'move north east', 'move north west', 'move south east', 'move south west', 'pickup note', '']:
				screen.blit(bg_surface, (0, 0))
				write("""You look around 
confused as to what 
you were trying to do.""")

	if active == True:
		colour = colour_active
	else:
		colour = colour_passive

	pygame.draw.rect(screen,colour,input_rect)
	
	text_surface = font.render(user_text, True, (0,0,0))
	screen.blit(text_surface,(input_rect.x + 5, input_rect.y + 7))
  #Update the screen
	pygame.display.update()

	clock.tick(60)