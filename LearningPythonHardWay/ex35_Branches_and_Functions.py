from sys import exit

def cthulhe_room():
	print("""Here you see the great evil Cthulhu.
		He, it, whatever stares at you and you go insane.
		Do you flee for your life or eat your head?""")
	next = input("flee or head?> ")
	if "flee" in next: # This in a new way to use if-statement
		start()
	elif "head" in next:
		print("Well that was tasty!")
		exit(0)
	else:
		cthulhe_room()

def bear_room():
	print("""
		There is a bear here.
		The bear has a bunch of honey.
		The fat bear is in front of another door.
		How are you going to move the bear?
		""")
	bear_moved = False

	while True:
		next = input("> ")
		if next == "take honey":
			dead("The bear looks at you then slap your face off.")
		elif next == "taunt bear" and not bear_moved: # This line is tricky
			print("The bear moved from the door. You can go through it now.")
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			print("The bear gets pissed off and chews your leg off.")
			exit(0)
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print("I got no idea what that means.")

def gold_room():
	print("This room is full of gold. How much do you take?")
	next = input("> ")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man, learn to be type a number.")
		gold_room()

	if how_much < 50:
		print("Great! you're not greedy, you win!")
		exit(0)
	else:
		print("You greedy bastard!")
		exit(0)

def dead(i):
	print(i ,"Good job!")
	exit(0) #

def start():
	print("""You are in a dark room.
		There is a door to your right and left.
		Which one do you take?""")
	next = input("> ")
	if next == "right":
		cthulhe_room()
	elif next == "left":
		bear_room()
	else:
		dead("You trap in the room, and no one will come to save you.")

start()