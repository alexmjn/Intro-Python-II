from room import Room
from player import Player
from room_setup import setup_rooms
import textwrap
# Declare all the rooms

room_map = setup_rooms()

#dictionary earlier sets up a bunch of room objects,
# we call the room object we need
player = Player("Alex", room_map["outside"])

user_is_playing = True
while user_is_playing:
    print(player.room.name)
    for line in textwrap.wrap(player.room.description):
        print(line)

    user_input = input("""
    The following actions are available:
    1) Move directions (n/s/e/w)
    2) Pick up items (pickup)
    3) Quit (q)
    """)
    if user_input.lower() in ['n', 's', 'e', 'w']:
        if player.room.connections is not None:
            player.move(user_input)
            print("you have moved to ", player.room.name)
            print("The items here are", player.room.items)
        else:
            print("There's no room there!")
    elif user_input.lower() == 'q':
        print("See you next time!")
        user_is_playing = False
    elif user_input.lower() == "pickup":
        item_check = input("Which item to pick up? ")
        player.pickup(item_check)
    else:
        print("Please enter a valid command! Press q to quit. ")


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
