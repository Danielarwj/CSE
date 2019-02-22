# Option 2- Set all at once, modify controller
class Room(object):
    def __init__(self, north=None, south=None, east=None, west=None, name=None, description=None, up=None, down=None):
        self.description = description
        self.up = up
        self.down = down
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.name = name

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

HOBO_ATTACKS = Room(None, "HOBO_WORLD", None, None, "Hobo Attacks you", "There is a homeless person here. He does not"
                    "like you. He hits you! You also can't seem to go back", "CEILING", "FLOOR")

GYM_PORTAL = Room(None, None, None, None, "Gym Portal", "This is the gym. It is dark and extremely musty. "
                  "I do not like it", "THE_REALM_OF_HEISENWEIBE", "THE_TRENCHES_OF_PAPA_PEARSON")

SCIENCE_BUILDING = Room("POOL", "W_BUILDING", "HOBO ATTACKS YOU", "QUAD", "The Science Building", "This is the science "
                        "building. I suppose you know what they teach in this, given the name.", "CEILING", "FLOOR")

QUAD = Room(None, None, "R BUILDINGS", "W BUILDINGS", "The Quad", "The main area. There is an ampitheatre here. There "
            "is also a couple of lamp posts.You can only go East and West, for some reason. ", "CEILING", "FLOOR")

W_BUILDING = Room("PARKING_LOT", "R_BUILDING", "QUAD", "PARKING_LOT", "W Building", "This is the W Building. It is a "
                  "two story masterpiece of a building. It,conveniently, is the building for languages.",
                  "THE SPANISH DILEMMA", "FLOOR")

MAILBOX = Room(None, None, None, None, "THE HOLY MAILBOX WELCOMES YOU!", "WELCOME TO SCHOOL WARRIOR, THE HIGHEST "
               "QUALITY GAME IN SCHOOL BASED" "CHOOSE YOUR OWN ADVENTURE GAMES! DEFEAT ONE BOSS AND COLLECT 20 ITEMS TO"
               "WIN THE GAME!", "R19A", None)

DRAMA_BUILDING = Room("NIGHTMARE EDISON", "SHAKESPEARE WORLD", "W_BUILDING", "PARKING_LOT", "The Drama Building", "This"
                      "is a long winding hallway. At the end there is a large telephone box. Paintings cover the wall",
                      "CEILING", None)

R_BUILDINGS = Room("THE_ESSAY_TYPING", "GYM_PORTAL", "PARKING_LOT", "QUAD", "The R Buildings", "This is a row of "
                   "buildings. You can only go North, however. The other areas are blocked off.", "CEILING", None)

HOBO_WORLD = Room("THE CHALLENGE AREA", None, None, None, "Hobo World", "YoU haVe DECidEd tO Go SoUtH! Welcome to Hobo "
                  "World, the realm of the desolate and the weak. Here, you must complete one of  three challenges- "
                  "Garbage collecting, tent folding, and the hardest one of all, finding 4 pieces of food. After you "
                  "face these challenges, you win the game!", None, None)

POOL = Room("POOL", "POOL", "POOL", "POOL", "The Pool", "CONGRATULATIONS, YOU'VE MADE IT TO THE POOL!", "POOL", "POOL")

THE_REALM_OF_HEISENWEIBE = Room("THE MAZE", "THE MAZE", "THE MAZE", "THE MAZE", " The Realm of Heisenwiebe", "Welcome"
                                " to a world unlike any other- THE REALM OF HEISENWIEBE. This place is a maze. Once you"
                                "enter the realm, you can not get out. Reach the end of the realm,fight the Heisenwiebe"
                                " himself, then you win.", "THE MAZE", "THE MAZE")

THE_DARK_TRENCHES_OF_PAPA_PEARSON = Room("THE_LONG_WINDING_HALLWAY", "LABYRINTH", "LABYRINTH", "LABYRINTH", "The Dark "
                                         "Trenches of Papa Pearson", "Welcome. There really is not much to say about "
                                         "this place. There is a jar of Jolly Ranchers. and Popcorn in the corner. In "
                                         "front of you is a long winding hallway that goes only north. It is dark. "
                                         "Really dark. Also, any other direction you go seems to drop you in sometime "
                                         "of labyrinth ", "CEILING", "FLOOR")

NIGHTMARE_EDISON = Room("NIGHTMARE_W_BUILDING", "NIGHTMARE R19A", "NIGHTMARE_PARKING_LOT", "NIGHTMARE_SCIENCE_BUILDING",
                        "NiGhTmArE EDiSon.", "WELCOME! This is Nightmare Edison. It is the same map as before only "
                        "SPOOKY! Get back to the normal world to win the game.", "NIGHTMARE_CEILING", None)

CEILING = Room("CEILING", "CEILING", "CEILING", "CEILING", "The Ceiling", "This is the ceiling. Do not go up, again!",
               "CEILING", None)


SHAKESPEARE_WORLD = Room("HAMLET", "OTHELLO", "TAMING OF THE SHREW", "ROMEO AND JULIET", "Shakespeare World", "You are "
                         "now in a medieval area. The buildings are that of 16th century. Everyone around you")

print(GYM_PORTAL. description)
print(R19A.north)
