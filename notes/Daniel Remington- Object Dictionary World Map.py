# Option 2- Set all at once, modify controller
class Room(object):
    def __init__(self, north=None, south=None, east=None, west=None, name=None, description=None, up=None, down=None,
                 characters=None):
        self.description = description
        self.up = up
        self.down = down
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.name = name
        self.characters = characters


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []

    def move(self, new_location):
        """ This moves the player to a new room

        :param new_location: The rooms object of which you are going to
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """ This method searches the current room to see if a room exists in that direction

        :param direction: The direction that ypu want to move to
        :return: The room object if it exists, or none if it does not
        """
        name_of_room = getattr(self.current_location, direction)
        return globals()[name_of_room]


class Hobo(object):
    def __init__(self, personality, cleanliness, clothing, appearance, items):
            self.items = items
            self.personality = personality
            self.cleanliness = cleanliness
            self.health = 100
            self.appearance = appearance
            self.clothing = clothing


Krishang = Hobo("NICE", "CLEAN", "PLAID_SHIRT", "Scruffy yet, well kept", ["Sword", "Health_potion", "Roman_Candle"])

# Blueprint for room
# Ex. R-19A =(North-Parking lot, South-etc.)
# Each room follows attributes set by object Room
# Ex. (North,South,East,West) = R-19A =(Parking Lot, ....)
# Presets-(like name=None)- must be applied to all attributes within the constructor


R19A = Room("PARKING_LOT", "QUAD", "DRAMA_BUILDING", "SCIENCE_BUILDING", "R19A",
            "This is the classroom you are in right now. There are two doors on the north wall. There are two doors on"
            " the north wall. There is a big mailbox in the sky for some reason", "MAILBOX", None)

PARKING_LOT = Room(None, "R19A", "HOBO_ATTACKS", "GYM_PORTAL", "Parking Lot", "There are a couple cars parked here. ",
                   None, "FLOOR")

HOBO_ATTACKS = Room(None, "HOBO_WORLD", None, None, "Hobo Attacks you", "There is a homeless person here. He does not"
                    "like you. He hits you! You also can't seem to go back", "CEILING", "FLOOR")

GYM_PORTAL = Room(None, None, None, None, "Gym Portal", "This is the gym. It is dark and extremely musty. "
                  "I do not like it", "THE_REALM_OF_HEISENWEIBE", "THE_TRENCHES_OF_PAPA_PEARSON")

SCIENCE_BUILDING = Room("POOL", "W_BUILDING", "HOBO_ATTACKS_YOU", "QUAD", "The Science Building", "This is the science "
                        "building. I suppose you know what they teach in this, given the name.", "CEILING", "FLOOR")

QUAD = Room(None, None, "R_BUILDINGS", "W_BUILDINGS", "The Quad", "The main area. There is an ampitheatre here. There "
            "is also a couple of lamp posts.You can only go East and West, for some reason. ", "CEILING", "FLOOR")

W_BUILDING = Room("PARKING_LOT", "R_BUILDING", "QUAD", "PARKING_LOT", "W Building", "This is the W Building. It is a "
                  "two story masterpiece of a building. It,conveniently, is the building for languages.",
                  "THE SPANISH DILEMMA", "FLOOR")

MAILBOX = Room(None, None, None, None, "THE HOLY MAILBOX WELCOMES YOU!", "WELCOME TO SCHOOL WARRIOR, THE HIGHEST "
               "QUALITY GAME IN SCHOOL BASED" "CHOOSE YOUR OWN ADVENTURE GAMES! DEFEAT ONE BOSS AND COLLECT 20 ITEMS TO"
               "WIN THE GAME!", None, "R19A")

DRAMA_BUILDING = Room("NIGHTMARE_EDISON", "SHAKESPEARE_WORLD", "W_BUILDING", "PARKING_LOT", "The Drama Building", "This"
                      "is a long winding hallway. At the end there is a large telephone box. Paintings cover the wall",
                      "CEILING", None, Krishang)

R_BUILDINGS = Room("THE_ESSAY_TYPING", "GYM_PORTAL", "PARKING_LOT", "QUAD", "The R Buildings", "This is a row of "
                   "buildings. You can only go North, however. The other areas are blocked off.", "CEILING", None)

HOBO_WORLD = Room("CHALLENGE_AREA", None, None, None, "Hobo World", "YoU haVe DECidEd tO Go SoUtH! Welcome to Hobo "
                  "World, the realm of the desolate and the weak. Here, you must complete one of  three challenges- "
                  "Garbage collecting, tent folding, and the hardest one of all, finding 4 pieces of food. After you "
                  "face these challenges, you win the game!", None, None)

POOL = Room("POOL", "POOL", "POOL", "POOL", "The Pool", "CONGRATULATIONS, YOU'VE MADE IT TO THE POOL!", "POOL", "POOL")

THE_REALM_OF_HEISENWEIBE = Room("THE_MAZE", "THE_MAZE", "THE_MAZE", "THE_MAZE", " The Realm of Heisenwiebe", "Welcome"
                                " to a world unlike any other- THE REALM OF HEISENWIEBE. This place is a maze. Once you"
                                "enter the realm, you can not get out. Reach the end of the realm,fight the Heisenwiebe"
                                " himself, then you win.", "THE MAZE", "THE MAZE")

THE_DARK_TRENCHES_OF_PAPA_PEARSON = Room("THE_LONG_WINDING_HALLWAY", "LABYRINTH", "LABYRINTH", "LABYRINTH", "The Dark "
                                         "Trenches of Papa Pearson", "Welcome. There really is not much to say about "
                                         "this place. There is a jar of Jolly Ranchers. and Popcorn in the corner. In "
                                         "front of you is a long winding hallway that goes only north. It is dark. "
                                         "Really dark. Also, any other direction you go seems to drop you in sometime "
                                         "of labyrinth ", "CEILING", "FLOOR")

NIGHTMARE_EDISON = Room("NIGHTMARE_W_BUILDING", "NIGHTMARE_R19A", "NIGHTMARE_PARKING_LOT", "NIGHTMARE_SCIENCE_BUILDING",
                        "NiGhTmArE EDiSon.", "WELCOME! This is Nightmare Edison. It is the same map as before only "
                        "SPOOKY! Get back to the normal world to win the game.", "NIGHTMARE_CEILING", None)

CEILING = Room("CEILING", "CEILING", "CEILING", "CEILING", "The Ceiling", "This is the ceiling. Do not go up, again!",
               "CEILING", None)


SHAKESPEARE_WORLD = Room("HAMLET", "OTHELLO", "TAMING_OF_THE_SHREW", "ROMEO_AND_JULIET", "Shakespeare World", "You are "
                         "now in a medieval area. The buildings are that of 16th century.Everyone around you is wearing"                   
                         "some type of Victorian clothing. In this world, you must act on a play. Essentially, You are"
                         " dropped into the world of the play and must find the way out.", "THE_GENTLEMEN_OF_VERONA",
                         "THE_MERCHANT_OF_VENICE")

THE_SPANISH_DILEMMA = Room("PROBLEMA_CUATRO", "PROBLEMA_UNO", "PROBLEMA_TRES", "UN PROBLEMA DIFICIL",
                           "THE_SPANISH_DILEMMA", "Este cuarto tiene una problema ese necesita resolver. Tu necesecitas"
                           " resolver la problema rapidamente. Si tu resuelves en tiempo, tu seras GANAR!", "CEILING",
                           "PROBLEMA_DOS")

FLOOR = Room("FLOOR", "FLOOR", "FLOOR", "FLOOR", "FLOOR", "This is the floor", "FLOOR", "FLOOR")

CHALLENGE_AREA = Room("PATH_1", "HOBO_WORLD", "PATH_3", "PATH_2", "The Challenge Area", "Welcome to the Challenge area."
                      "This is a very dark and musty cave. From what it seems,in the cave there are walls that block "
                      "off certain areas. Kind of like a maze?", "CEILING", "FLOOR")

PATH_1 = Room("MINI_PATH_1", "HOBO_WORLD", "MINI_PATH_2", "DEAD_END", "The North Path", "This part of the challenge "
              "area is quite large. I don't like it. North and East seem to both have something", "CEILING", "FLOOR")

PATH_2 = Room("MINI_PATH_3", "DEAD_END", "MINI_PATH_4", "MINI_PATH_5", "The Western Path", "This part of the challenge "
              "is strange. Odd paintings cover the walls. South seems to go somewhere... or does it?", "CEILING",
              "FLOOR")

NIGHTMARE_PARKING_LOT = Room("NIGHTMARE_CEILING", None, "NIGHTMARE_W_BUILDING", "NIGHTMARE_FLOOR", "Nightmare Floor",
                             "Welcome to the Nightmare Version of the parking lot. All the cars are Hummers.Get spooked"
                             " by their carbon emissions and their excessive gas prices!", "NIGHTMARE_GYM_PORTAL",
                             "NIGHTMARE_R19A")

NIGHTMARE_W_BUILDING = Room("NIGHTMARE_EDISON", "NIGHTMARE_CEILING", "NIGHTMARE_R_BUILDINGS", "NIGHTMARE_EDISON", "The "
                            "Nightmare W Buildings", "The building in a never ending staircase. It's almost like... a "
                            "maze. But it isn't. However, there are a lot of signs that just say- Look out for the "
                            "start.", "NIGHTMARE_CEILING", "NIGHTMARE_EDISON")

NIGHTMARE_R19A = Room("NIGHTMARE_GYM_PORTAL", "NIGHTMARE_HOBO_WORLD", "NIGHTMARE_DRAMA_BUILDING", "NIGHTMARE_QUAD",
                      "Nightmare R19A", "This is a SpOoOky computer room. All of the computers are Windows 98 and are "
                      "slower than paces of snails. ", "NIGHTMARE_CEILING", "NIGHTMARE_EDISON")

NIGHTMARE_SCIENCE_BUILDING = Room("NIGHTMARE_QUAD", "NIGHTMARE_HOBO_WORLD", "NIGHTMARE_EDISON", "NIGHTMARE_FLOOR", "The"
                                  "Nightmare Science Buildings", "The classes are terrifying! They're taught by "
                                  "flat-earthers and people who are against vaccines. What has this world come to?!",
                                  "NIGHTMARE_FLOOR", None)

HAMLET = Room("NORTH_ROOM", "SOUTH_ROOM", "HALLWAY", "GROVE", "Hamlet", "Considered to be his best play, Hamlet is "
              "play in which Hamlet's father dies and it tells of his slow descent into madness. Get to the last scene "
              "to win", "CEILING", "FLOOR")

OTHELLO = Room("VENITIAN_STREET", "COUNCIL_CHAMBER", "SEA_PORT", "THE_CASTLE", "Othello", "Welcome to othello- The "
               "play, not the game. The play is about a Venetian soldier who passed over promotion by Othello and the "
               "story of how Othello undermines him, causing him to get revenge. Get to the last scene to win",
               "CEILING", "FLOOR")

PROBLEMA_UNO = ("SECCION_UNO", "SECCION_DOS", "SECCION_TRES", "SECCION_QUATRO", "Problema Uno", "Es el primero problema"
                ". You need to solve one puzzle and ten queestions", "CEILING", "FLOOR")

PROBLEMA_DOS = ("SECCION_CINCO", "SECCION_SEIS", "SECCION_SIETE", "SECCION_OCHO", "Problema Dos", " Es el segundo "
                "problema. This challenges requires you to complete four mazes and code in spanish ", None, None)

PROBLEMA_TRES = ("LOS_PANQUEQUES", "EL_FUTURO", "EL_PRETERITO", "PRESENTE-PROGRESIVO", "Problema Tres", "Es el trecero"
                 " problema. In this one, you have to answer high intensity questions on verbs and vocabulary",
                 "VOCABULARIO_UNO", None)

THE_MAZE = ("NULL_PATH", "IMPORT_GOD_PATH", "__INIT__PATH", "BAD_JOKE_PATH", "The Maze", "Welcome to the Heisenwiebe "
            "Maze. This maze has each path leading to a different aspect of the Heisenwiebe. Reach the center to win",
            "SPAAAACE_PATH", "LUCKY_7'S_PATH")

THE_LONG_WINDING_HALLWAY = ("MATH_JESUS", "2019'S_CANCEL_OUT", "2019^2", "THE_INTEGRAL_OF_THE_SIN_OF_THE_COSINE_OF_THE"
                            "_DERIVATIVE_OF_INTEGRAL_OF_THE_LOG_OF_X_SQUARED_CUBED_SQUARED", "The Long Winding Hallway",
                            "It's... just... It'sj really difficult. Complete all 4 to win","CEILING","FLOOR")

print(GYM_PORTAL. description)
print(R19A.north)

player = Player(R19A)

# Controller
playing = True
directions = ['north', 'south', "west", "east", "up", "down"]
while playing:
    print(player.current_location.name)  # player- indicates the instantiated object. current_location- refers to the
    # variable. .name = refers to the attribute of the location
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in ["q", "quit", 'exit']:
        playing = False
        print("GAME OVER.")
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command)
            player.move(next_room)

        except KeyError:
            print("I can't go that way!")
    else:
        print("Command not found")
