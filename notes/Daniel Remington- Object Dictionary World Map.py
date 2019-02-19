class Room(object):
    def __init__(self, north, south, east, west, name, description, up, down):
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.name = name
        self.description = description
        self.up = up
        self.down = down

# Blueprint for room
# Ex. R-19A =(North-Parking lot, South-etc.)
# Each room follows attributes set by object Room
# Ex. (North,South,East,West) = R-19A =(Parking Lot, ....)


R19A = Room("PARKING LOT", "QUAD", "DRAMA BUILDING", "SCIENCE BUILDING", "R19A",
            "This is the classroom you are in right now. There are two doors on the north wall. There are two doors on"
            " the north wall. There is a big mailbox in the sky for some reason", "MAILBOX", None)
print(R19A.description)
