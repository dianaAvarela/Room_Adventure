from tkinter import (
    #Widgets 
    Frame, Label, Text, PhotoImage, Entry,

    #Constants
    X, Y, BOTH,
    BOTTOM, RIGHT, LEFT,
    DISABLED, NORMAL, END,

    #Additional stuff from Type Hints
    Tk 
)
from room import Room # from the room.py file
import os  # for building filepaths

class Game(Frame):

    # statuses
    STATUS_DEFAULT = "I don't understand. Try verb noun. Valid verds are go, look, take"
    STATUS_DEAD = "You are dead."
    STATUS_BAD_EXIT = "Invalid Exit."

    STATUS_ROOM_CHANGE = "Room changed."
    STATUS_GRABBED = "Item grabbed."
    STATUS_BAD_GRABBABLE = "I can't grab that."

    STATUS_BAD_ITEM = "I don't see that."

    # exit actions
    EXIT_ACTIONS = ["quit", "exit", "bye", "adios", "q"]

    # game dimensions
    WIDTH = 800
    HEIGHT = 600

    def __init__(self, parent):
        """
        The Game Class.
        There should be only one game class.
        Responsible for the flow of the game.

        parent: Tk - a Tk object representing the window the game runs in.
        """
        self.invetory = []
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=1)

    def setup_game(self):
        """
            Creates the rooms and adds items and exits to the rooms.
        """
        # create rooms
        r1 = Room("Room 1", os.path.join("images", "room1.gif"))
        r2 = Room("Room 2", os.path.join("images", "room2.gif"))
        r3 = Room("Room 3", os.path.join("images", "room3.gif"))
        r4 = Room("Room 4", os.path.join("images", "room4.gif"))

        # create the exits
        r1.add_exit("east", r2)
        r1.add_exit("south", r3)

        r2.add_exit("west", r1)
        r2.add_exit("south", r4)

        r3.add_exit("north", r1)
        r3.add_exit("east", r4)

        r4.add_exit("north", r2)
        r4.add_exit("west", r3)
        r4.add_exit("south", None) # none for death sequence

        #add Items to the rooms
        r1.add.item("chair", "It's made of wicker")
        r1.add_item("bigger_chair", "It's made of more wicker. There is a key on it")

        r2.add.item("smaller_chair", "It's made of less wicker.")
        r2.add_item("fireplace", "It is not a chair. Please don't sit in it.")

        r3.add.item("desk_chair", "It's made of wicker too. So is the desk.")
        r3.add_item("chair", "Yet another chair")

        r4.add.item("crossiant", "It's made of chairs.")

        #add grabbables 
        r1.add_grabbable("key")
        r2.add_grabbable("fire")
        r3.add_grabbable("chair")
   
        #set current room
        self.current_room = r1


    def setup_gui(self):
        # setup the input element 
        self.player_input = Entry(self, bg="white", fg="black")
        self.player_input.bind("<Return>", self.process_inputs)
        self.player_input.pack(side=BOTTOM, fill=X)
        self.player_input.focus()

        # setup the image element
        img = None                          # the actual image
        img_width = Game.WIDTH // 2 
        self.image_container = Label(       # the label element containing the image
            self, 
            width = img_width,
            image = img
        )
        self.image_container.image = img                # persists the image past this function 
        self.image_container.pack(side=LEFT, fill=Y)
        self.image_container.pack_propagate(False)      # prevent image from controlling container

        # setup the info area
        text_container_width = Game.WIDTH // 2
        text_container = Frame(self, width=text_container_width)

        self.text = Text(
            text_container,             # parent element is the text_container this time, not seld (the Game)
            bg="lightgrey",
            fg="black",
            state=DISABLED              # making so the text cannot be changed
        )


    def set_status(self, status):
        pass 

    def set_image(self):
        pass

    def clear_entry(self):
        pass

    def handle_verb_go(self, destination):
        pass

    def handle_verb_look(self, item):
        pass

    def handle_verb_take(self, grababble):
        pass

    def handle_default(self):
        pass

    def play(self):
        self.setup_game()
        self.setup_gui()
        self.setup_image()
        self.set_status("")

    def process_inputs(self, event):
        pass