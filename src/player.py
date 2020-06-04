# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player():
# pass an object of class Room to the class constructor
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def __str__(self):
        return "The Hero is in " + self.room

    def move(self, direction):
        if self.room.connections[direction] is not None:
            self.room = self.room.connections[direction]
        else:
            print("You cannot move in that direct")
