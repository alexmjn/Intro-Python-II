# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player():
# pass an object of class Room to the class constructor
    def __init__(self, name, room, inventory=[]):
        self.name = name
        self.room = room
        self.inventory = inventory

    def __str__(self):
        return "The Hero is in " + self.room

    def move(self, direction):
        if self.room.connections[direction] is not None:
            self.room = self.room.connections[direction]
        else:
            print("You cannot move in that direction! Try again.")

    def pickup(self, item):
        if item in self.room.items:
            self.inventory.append(item)
            print(f"You have picked up {item.name}")
        else:
            print("That item is not in the room")

    def print_inventory(self):
        for item in self.inventory:
            print(item.name + "\n" + item.description)
