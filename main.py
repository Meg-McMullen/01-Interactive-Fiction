#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "uuid": "C16DC756-14A1-45B3-A378-F6CBFB7A3E26",
  "name": "Toad",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631191510207,
  "passages": [
    {
      "name": "Meadow",
      "tags": "",
      "id": "1",
      "text": "You are a toad in a meadow surrounded on all sides by tall grasses. It is dusk and nocturnal predators will be out soon. You should not be out in the open.\n\n[[NORTH->North of Meadow]]\n[[STRAIGHT->Forest]]\n[[WEST->Firefly Bog]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "North of Meadow",
          "original": "[[NORTH->North of Meadow]]"
        },
        {
          "linkText": "STRAIGHT",
          "passageName": "Forest",
          "original": "[[STRAIGHT->Forest]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Firefly Bog",
          "original": "[[WEST->Firefly Bog]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are a toad in a meadow surrounded on all sides by tall grasses. It is dusk and nocturnal predators will be out soon. You should not be out in the open."
    },
    {
      "name": "Mossy Log",
      "tags": "",
      "id": "2",
      "text": "This log is Mr. and Mrs. Frog's home. Between the cracks in the wood, you can see that the lights are on.\n\n[[WEST->Firefly Bog]]\n[[EAST->Street]]\n[[IN->Inside Mossy Log]]",
      "links": [
        {
          "linkText": "WEST",
          "passageName": "Firefly Bog",
          "original": "[[WEST->Firefly Bog]]"
        },
        {
          "linkText": "EAST",
          "passageName": "Street",
          "original": "[[EAST->Street]]"
        },
        {
          "linkText": "IN",
          "passageName": "Inside Mossy Log",
          "original": "[[IN->Inside Mossy Log]]"
        }
      ],
      "hooks": [],
      "cleanText": "This log is Mr. and Mrs. Frog's home. Between the cracks in the wood, you can see that the lights are on."
    },
    {
      "name": "Sewer Grate",
      "tags": "",
      "id": "3",
      "text": "You are standing on top of the sewer. A faint light glows mysteriously below you. \n\n[[EAST->Street two]]\n[[DOWN->Inside Sewer Grate]]",
      "links": [
        {
          "linkText": "EAST",
          "passageName": "Street two",
          "original": "[[EAST->Street two]]"
        },
        {
          "linkText": "DOWN",
          "passageName": "Inside Sewer Grate",
          "original": "[[DOWN->Inside Sewer Grate]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are standing on top of the sewer. A faint light glows mysteriously below you."
    },
    {
      "name": "Inside Mossy Log",
      "tags": "",
      "id": "4",
      "text": "Mrs. Frog opens the door, \"Good evening, Toad! Isn't it a bit late to be out? I'm sorry, but we don't have anymore beds to spare. The tadpoles just grew legs and have graduated to bed time on land.\" You politely thank her for her company and leave.\n\n[[OUT->Mossy Log]]",
      "links": [
        {
          "linkText": "OUT",
          "passageName": "Mossy Log",
          "original": "[[OUT->Mossy Log]]"
        }
      ],
      "hooks": [],
      "cleanText": "Mrs. Frog opens the door, \"Good evening, Toad! Isn't it a bit late to be out? I'm sorry, but we don't have anymore beds to spare. The tadpoles just grew legs and have graduated to bed time on land.\" You politely thank her for her company and leave."
    },
    {
      "name": "North of Meadow",
      "tags": "",
      "id": "5",
      "text": "You are North of the meadow. It is scary at night, and there is not much to cover you from lurking predators.\n\n[[SOUTH->Meadow]]\n[[EAST->Street]]\n[[WEST->Firefly Bog]]",
      "links": [
        {
          "linkText": "SOUTH",
          "passageName": "Meadow",
          "original": "[[SOUTH->Meadow]]"
        },
        {
          "linkText": "EAST",
          "passageName": "Street",
          "original": "[[EAST->Street]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Firefly Bog",
          "original": "[[WEST->Firefly Bog]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are North of the meadow. It is scary at night, and there is not much to cover you from lurking predators."
    },
    {
      "name": "Forest",
      "tags": "",
      "id": "6",
      "text": "You enter a forest. It is not much safer in here. The owls lurk nearby.\n\n[[NORTH->Meadow]]\n[[EAST->Street]]\n[[WEST->Firefly Bog]]\n[[SOUTH->Mushroom Houses]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "Meadow",
          "original": "[[NORTH->Meadow]]"
        },
        {
          "linkText": "EAST",
          "passageName": "Street",
          "original": "[[EAST->Street]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Firefly Bog",
          "original": "[[WEST->Firefly Bog]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "Mushroom Houses",
          "original": "[[SOUTH->Mushroom Houses]]"
        }
      ],
      "hooks": [],
      "cleanText": "You enter a forest. It is not much safer in here. The owls lurk nearby."
    },
    {
      "name": "Firefly Bog",
      "tags": "",
      "id": "7",
      "text": "You have found firefly Bog. You are sitting on a lilly pad, and there is water in all directions around you. It is a cool summer night and the fireflies light up the water. \n\n[[LOG->Mossy Log]]\n[[BOG->Firefly Bog]]\n[[SHORE->Shore]]",
      "links": [
        {
          "linkText": "LOG",
          "passageName": "Mossy Log",
          "original": "[[LOG->Mossy Log]]"
        },
        {
          "linkText": "BOG",
          "passageName": "Firefly Bog",
          "original": "[[BOG->Firefly Bog]]"
        },
        {
          "linkText": "SHORE",
          "passageName": "Shore",
          "original": "[[SHORE->Shore]]"
        }
      ],
      "hooks": [],
      "cleanText": "You have found firefly Bog. You are sitting on a lilly pad, and there is water in all directions around you. It is a cool summer night and the fireflies light up the water."
    },
    {
      "name": "Street",
      "tags": "",
      "id": "8",
      "text": "You are standing in a dimly lit street. There is a car coming, but you are too slow to be able to hop all the way accross the road.\n\n\n[[ESCAPE->Sewer Grate]]\n[[RISK IT->You died]]",
      "links": [
        {
          "linkText": "ESCAPE",
          "passageName": "Sewer Grate",
          "original": "[[ESCAPE->Sewer Grate]]"
        },
        {
          "linkText": "RISK IT",
          "passageName": "You died",
          "original": "[[RISK IT->You died]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are standing in a dimly lit street. There is a car coming, but you are too slow to be able to hop all the way accross the road."
    },
    {
      "name": "Inside Sewer Grate",
      "tags": "",
      "id": "9",
      "text": "You slip through the grate and splash into the water below. The soft current carries you towards a fork in the tunnel. On the right the current appears to speed up, but on the left the water appears a murky green.\n\n[[RIGHT->Right Tunnel]]\n[[LEFT->Left Tunnel]]",
      "links": [
        {
          "linkText": "RIGHT",
          "passageName": "Right Tunnel",
          "original": "[[RIGHT->Right Tunnel]]"
        },
        {
          "linkText": "LEFT",
          "passageName": "Left Tunnel",
          "original": "[[LEFT->Left Tunnel]]"
        }
      ],
      "hooks": [],
      "cleanText": "You slip through the grate and splash into the water below. The soft current carries you towards a fork in the tunnel. On the right the current appears to speed up, but on the left the water appears a murky green."
    },
    {
      "name": "Right Tunnel",
      "tags": "",
      "id": "10",
      "text": "The current is too strong for you to keep up. Rolling over and under the waves you feel a drop as you're pulled over the edge of a waterfall.\n\n[[YOU DIED->You died]]",
      "links": [
        {
          "linkText": "YOU DIED",
          "passageName": "You died",
          "original": "[[YOU DIED->You died]]"
        }
      ],
      "hooks": [],
      "cleanText": "The current is too strong for you to keep up. Rolling over and under the waves you feel a drop as you're pulled over the edge of a waterfall."
    },
    {
      "name": "Left Tunnel",
      "tags": "",
      "id": "11",
      "text": "The water around becomes viscous with algae, but the current is slow enough you could turn back now.\n\n[[ONWARD->Sewer City]]\n[[BACK->Inside Sewer Grate]]",
      "links": [
        {
          "linkText": "ONWARD",
          "passageName": "Sewer City",
          "original": "[[ONWARD->Sewer City]]"
        },
        {
          "linkText": "BACK",
          "passageName": "Inside Sewer Grate",
          "original": "[[BACK->Inside Sewer Grate]]"
        }
      ],
      "hooks": [],
      "cleanText": "The water around becomes viscous with algae, but the current is slow enough you could turn back now."
    },
    {
      "name": "Mushroom Houses",
      "tags": "",
      "id": "12",
      "text": "You come upon small mushroom houses. They're cute, but you are much too large to hide under one.\n\n[[BACK->Forest]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Forest",
          "original": "[[BACK->Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "You come upon small mushroom houses. They're cute, but you are much too large to hide under one."
    },
    {
      "name": "You died",
      "tags": "",
      "id": "13",
	  "score":10,
      "text": "You have passed on to the toady beyond. Congrats you will be reincarnated.\n\n[[REINCARNATE->Meadow]]",
      "links": [
        {
          "linkText": "REINCARNATE",
          "passageName": "Meadow",
          "original": "[[REINCARNATE->Meadow]]"
        }
      ],
      "hooks": [],
      "cleanText": "You have passed on to the toady beyond. Congrats you will be reincarnated."
    },
    {
      "name": "Street two",
      "tags": "",
      "id": "14",
      "text": "You are back on the street and the car is gone. You don't think staying here is a great idea. Where next?\n\n[[NORTH->North of Meadow]]\n[[STRAIGHT->Forest]]\n[[WEST->Firefly Bog]]\n[[EAST->Construction site]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "North of Meadow",
          "original": "[[NORTH->North of Meadow]]"
        },
        {
          "linkText": "STRAIGHT",
          "passageName": "Forest",
          "original": "[[STRAIGHT->Forest]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Firefly Bog",
          "original": "[[WEST->Firefly Bog]]"
        },
        {
          "linkText": "EAST",
          "passageName": "Construction site",
          "original": "[[EAST->Construction site]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are back on the street and the car is gone. You don't think staying here is a great idea. Where next?"
    },
    {
      "name": "Shore",
      "tags": "",
      "id": "15",
      "text": "You hopped to shore. Maybe there is a nice empty hole nearby to hide in?\n\n[[STRAIGHT->Forest]] \n[[SOUTH->Mushroom Houses]] \n[[EAST->Street]]",
      "links": [
        {
          "linkText": "STRAIGHT",
          "passageName": "Forest",
          "original": "[[STRAIGHT->Forest]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "Mushroom Houses",
          "original": "[[SOUTH->Mushroom Houses]]"
        },
        {
          "linkText": "EAST",
          "passageName": "Street",
          "original": "[[EAST->Street]]"
        }
      ],
      "hooks": [],
      "cleanText": "You hopped to shore. Maybe there is a nice empty hole nearby to hide in?"
    },
    {
      "name": "Construction site",
      "tags": "",
      "id": "16",
      "text": "You have stumbled upon a dusty construction site. There are no humans here and plenty of dry holes to hide in. Which hole will you choose?\n\n[[HOLE ONE->Hole one]]\n[[HOLE TWO->Hole two]]\n[[HOLE THREE->Hole three]]",
      "links": [
        {
          "linkText": "HOLE ONE",
          "passageName": "Hole one",
          "original": "[[HOLE ONE->Hole one]]"
        },
        {
          "linkText": "HOLE TWO",
          "passageName": "Hole two",
          "original": "[[HOLE TWO->Hole two]]"
        },
        {
          "linkText": "HOLE THREE",
          "passageName": "Hole three",
          "original": "[[HOLE THREE->Hole three]]"
        }
      ],
      "hooks": [],
      "cleanText": "You have stumbled upon a dusty construction site. There are no humans here and plenty of dry holes to hide in. Which hole will you choose?"
    },
    {
      "name": "Hole one",
      "tags": "",
      "id": "17",
      "text": "There is a turtle in this hole. Maybe you should go somewhere else?\n\n[[BACK->Construction site]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Construction site",
          "original": "[[BACK->Construction site]]"
        }
      ],
      "hooks": [],
      "cleanText": "There is a turtle in this hole. Maybe you should go somewhere else?"
    },
    {
      "name": "Hole two",
      "tags": "",
      "id": "18",
      "text": "You don't see anybody in this hole. Its not the lap of luxery but it'll do.\n\n[[STAY->YOU WIN]]",
      "links": [
        {
          "linkText": "STAY",
          "passageName": "YOU WIN",
          "original": "[[STAY->YOU WIN]]"
        }
      ],
      "hooks": [],
      "cleanText": "You don't see anybody in this hole. Its not the lap of luxery but it'll do."
    },
    {
      "name": "Hole three",
      "tags": "",
      "id": "19",
      "text": "You see glowing green eyes coming towards you slowly. EEEK!!! SNAKE! Aaaand its too late.\n\n[[YOU DIED->You died]]",
      "links": [
        {
          "linkText": "YOU DIED",
          "passageName": "You died",
          "original": "[[YOU DIED->You died]]"
        }
      ],
      "hooks": [],
      "cleanText": "You see glowing green eyes coming towards you slowly. EEEK!!! SNAKE! Aaaand its too late."
    },
    {
      "name": "Sewer City",
      "tags": "",
      "id": "20",
      "text": "You have stumbled upon a froggy Venice. String lights illuminate the dark tunnel to show a small city within. A small frog passes by on a gondola.\n\n[[GO->Firefly Bog]] \n[[ASK TO STAY->Venice]]",
      "links": [
        {
          "linkText": "GO",
          "passageName": "Firefly Bog",
          "original": "[[GO->Firefly Bog]]"
        },
        {
          "linkText": "ASK TO STAY",
          "passageName": "Venice",
          "original": "[[ASK TO STAY->Venice]]"
        }
      ],
      "hooks": [],
      "cleanText": "You have stumbled upon a froggy Venice. String lights illuminate the dark tunnel to show a small city within. A small frog passes by on a gondola."
    },
    {
      "name": "Venice",
      "tags": "",
      "id": "21",
      "text": "You ask a frog if there is a place to stay and he takes you to the inn. You walk in to a cozy wooden foyer and get your keys. CONGRATS! You have found a place to stay!\n\n[[YOU WIN->YOU WIN]]",
      "links": [
        {
          "linkText": "YOU WIN",
          "passageName": "YOU WIN",
          "original": "[[YOU WIN->YOU WIN]]"
        }
      ],
      "hooks": [],
      "cleanText": "You ask a frog if there is a place to stay and he takes you to the inn. You walk in to a cozy wooden foyer and get your keys. CONGRATS! You have found a place to stay!"
    },
    {
      "name": "YOU WIN",
      "tags": "",
      "id": "22",
	  "score":20,
      "text": "Would you like to play again?\n\n[[YES->Meadow]]",
      "links": [
        {
          "linkText": "YES",
          "passageName": "Meadow",
          "original": "[[YES->Meadow]]"
        }
      ],
      "hooks": [],
      "cleanText": "Would you like to play again?"
    }
  ]
}


# ----------------------------------------------------------------

def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

# ----------------------------------------------------------------

def render(current_location, score, moves):
	if "name" in current_location and "cleanText" in current_location:
		print("Moves: " + str(moves) + ", Score: " + str(score))
		print(str(current_location["name"]))
		print(current_location["cleanText"] + "\n")

def get_input():
	response = input("What do you want to do? ")
	response = response.upper().strip()
	return response

def update(current_location, location_label, response):
	if response == "":
		return location_label
	for link in current_location["links"]:
		if link["linkText"] == response:
			return link["passageName"]
	print("I don't understand what you are trying to do. Please try again.")
	return location_label


# ----------------------------------------------------------------

location_label = "Meadow"
current_location = {}
response = ""
score = 0
moves = 0

while True:
	if response == "QUIT":
		break
	moves += 1
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
	if "score" in current_location:
		score = score + current_location["score"]
	render(current_location, score, moves)
	response = get_input()


print("Thanks for playing!")