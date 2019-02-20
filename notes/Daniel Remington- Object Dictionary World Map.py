# Option 2- Set all at once, modify controller
class Room(object):
    def __init__(self, north=None, south=None, east=None, west=None, name=None, description=None, up=None, down=None):
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
# Presets-(like name=None)- must be applied to all attributes within the constructor


R19A = Room("PARKING_LOT", "QUAD", "DRAMA_BUILDING", "SCIENCE_BUILDING", "R19A",
            "This is the classroom you are in right now. There are two doors on the north wall. There are two doors on"
            " the north wall. There is a big mailbox in the sky for some reason", "MAILBOX", None)

PARKING_LOT = Room(None, "R19A", "HOBO_ATTACKS", "GYM PORTAL", "Parking Lot", "There are a couple cars parked here",
                   None, "FLOOR")

HOBO_ATTACKS = Room(None,"HOBO_WORLD", None, None, "Hobo Attacks you", "There is a homeless person here. He does not"
                    "like you. He hits you! You also can't seem to go back", "CEILING", "FLOOR")

GYM_PORTAL = Room(None, None, None, None, "Gym Portal", "This is the gym. It is dark and extremely musty. "
                  "I do not like it", "THE REALM OF HEISENWEIBE", "THE TRENCHES OF PAPA PEARSON")

SCIENCE_BUILDING = Room()

# 'EAST': 'HOBO ATTACKS YOU' 'WEST': 'QUAD','NORTH': 'POOL','SOUTH': 'W BUILDING','UP': 'CEILING','DOWN': 'FLOOR'

print(GYM_PORTAL. description)
print(R19A.north)
