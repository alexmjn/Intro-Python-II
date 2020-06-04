from room import Room
from player import Player
import textwrap
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].connections["n"] = room['foyer']
room['foyer'].connections["s"] = room['outside']
room['foyer'].connections["n"] = room['overlook']
room['foyer'].connections["e"] = room['narrow']
room['overlook'].connections["s"] = room['foyer']
room['narrow'].connections["w"] = room['foyer']
room['narrow'].connections["n"] = room['treasure']
room['treasure'].connections["s"] = room['narrow']

#dictionary earlier sets up a bunch of room objects,
# we call the room object we need
player = Player("Alex", room["outside"])

user_is_playing = True
while user_is_playing:
    print(player.room.name)
    for line in textwrap.wrap(player.room.description):
        print(line)

    user_input = input("Which direction would you like to go? (n/e/s/w)")
    if user_input.lower() in ['n', 's', 'e', 'w']:
        if player.room.connections is not None:
            player.move(user_input)
            print("you have moved to " + player.room.name)
            print("The items here are" + player.room.items)
        else:
            print("There's no room there!")
    elif user_input.lower() == 'q':
        print("See you next time!")
        user_is_playing = False
    else:
        print("Please enter a valid command!")


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
