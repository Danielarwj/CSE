world_map = {
    'R19A': {
        'NAME': "Mr. Wiebe's room",
        'DESCRIPTION': "This is the classroom you are in right now. "
                       "There are two doors on the north wall. "
                       "There is also doors on the east, west, and south Walls. "
                       "There is a big mailbox in the sky for some reason",
        'PATHS': {
            'NORTH': 'PARKING_LOT',
            'EAST': 'DRAMA BUILDING',
            'WEST': 'SCIENCE BUILDING',
            'SOUTH': 'QUAD',
            'UP': 'MAILBOX'

        }
    },
    'PARKING_LOT': {
        'NAME': "The North Parking Lot",
        'DESCRIPTION': "There are a couple cars parked here",
        'PATHS': {
            'SOUTH': 'R19A',
            'WEST': 'GYM PORTAL',
            'EAST': 'HOBO ATTACKS YOU',
            'DOWN': 'FLOOR'
        }
    },
    'HOBO ATTACKS YOU': {
        'NAME': "Hobo quarters",
        'DESCRIPTION': "There is a homeless person here. He does not like you. He hits you! You also can't seem to go "
                       "back",
        'PATHS': {
            'SOUTH': 'HOBO WORLD'

        }
    },
    'GYM PORTAL': {
        'NAME': 'The Gym portal',
        'DESCRIPTION': 'This is the gym. It is dark and extremely musty. I do not like it',
        'PATHS': {
            'UP': 'THE REALM OF THE HEISENWEIBE',
            'DOWN': 'THE DARK TRENCHES OF PAPA PEARSON'
        }
    },
    'SCIENCE BUILDING': {
        'NAME': 'The science building',
        'DESCRIPTION': 'This is the science building. I suppose you know what they teach in this, given the name.',
        'PATHS': {
            'EAST': 'HOBO ATTACKS YOU',
            'WEST': 'QUAD',
            'NORTH': 'POOL',
            'SOUTH': 'W BUILDING',
            'UP': 'CEILING',
            'DOWN': 'FLOOR'
        }
    },
    'QUAD': {
        'NAME': 'The Quad',
        'DESCRIPTION': 'The main area. There is an ampitheatre here. There is also a couple of lamp posts.'
                       'You can only go East and West, for some reason. ',
        'PATHS': {
            'WEST': 'W BUILDING',
            'EAST': 'R BUILDINGS'
        }
    },
    'W BUILDING': {
        'NAME': 'W Building',
        'DESCRIPTION': 'This is the W Building. It is a two story masterpiece of a building. '
                       'It,conveniently, is the building for languages',
        'PATHS': {
            'UP': 'THE SPANISH DILEMMA',
            'DOWN': 'FLOOR',
            'NORTH': 'PARKING_LOT',
            'EAST': 'QUAD',
            'WEST': 'PARKING LOT',
            'SOUTH': 'R BUILDING',

        }
    },
    'MAILBOX': {
        'NAME': 'THE HOLY MAILBOX WELCOMES YOU!',
        'DESCRIPTION': 'WELCOME TO SCHOOL WARRIOR, THE HIGHEST QUALITY GAME IN SCHOOL BASED CHOOSE YOUR OWN ADVENTURE'
                       'GAMES! DEFEAT ONE BOSS AND COLLECT 20 ITEMS TO WIN THE GAME!',
        'PATHS': {
            'DOWN': 'R19A'
        }
    },
    'DRAMA BUILDING': {
        'NAME': 'The Drama Building',
        'DESCRIPTION': 'This is a long winding hallway. At the end there is a large telephone box. Paintings cover the '
                       'walls',
        'PATHS': {
            'SOUTH': "SHAKESPEARE WORLD",
            'NORTH': 'NIGHTMARE EDISON',
            'EAST': 'W BUILDING',
            'WEST': 'PARKING LOT',
            'UP': 'CEILING'
        }
    },
    'R BUILDINGS': {
        'NAME': 'The R buildings',
        'DESCRIPTION': 'This is a row of buildings. You can only go North, however. The other areas are blocked off.',
        'PATHS': {
            'NORTH': 'THE ESSAY TYPING SESSION',
            'EAST': 'PARKING LOT',
            'WEST': 'QUAD',
            'SOUTH': 'GYM PORTAL',
            'UP': 'CEILING'
        }
    },
    'HOBO WORLD': {
        'NAME': 'Hobo World',
        'DESCRIPTION': 'YoU haVe DECidEd tO Go SoUtH! Welcome to Hobo World, the realm of the desolate and the weak'
                       'Here, you must complete one of'
                       ' three challenges- Garbage collecting, tent folding, and the hardest one of '
                       'all, finding 4 pieces of food. After you face these challenges, you win the game!',
        'PATHS': {
            'NORTH': 'THE CHALLENGE AREA'
        }
    },
    'POOL': {
        'NAME': 'POOL',
        'DESCRIPTION': ' CONGRATULATIONS! YOU HAVE REACHED THE POOL.',
        'PATHS': {
            'NORTH': 'POOL',
            'SOUTH': 'POOL',
            'EAST': 'POOL',
            'WEST': 'POOL',
            'UP': 'POOL',
            'DOWN': 'POOL'
        }
    },
    'THE REALMS OF HEISENWIEBE': {
        'NAME': 'The Realm of the Heisenwiebe',
        'DESCRIPTION': 'Welcome to a world unlike any other- THE REALM OF HEISENWIEBE. This place is a maze.'
                       'Once you enter the realm, you can not get out. Reach the end of the realm, fight the '
                       'Heisenwiebe himself, then you win ',
        'PATHS': {
            'NORTH': 'THE MAZE',
            'SOUTH': 'THE MAZE',
            'UP': 'THE MAZE',
            'DOWN': 'THE MAZE',
            'EAST': 'THE MAZE',
            'WEST': 'THE MAZE'
        }

    },
    'THE DARK TRENCHES OF PAPA PEARSON': {
        'NAME': 'The Dark Trenches of Papa Pearson',
        'DESCRIPTION': 'Welcome. There really is not much to say about this place. There is a jar of Jolly Ranchers'
                       'and Popcorn in the corner. In front of you is a long winding hallway that goes only north. '
                       'It is dark. Really dark. Also, any other direction you go seems to drop you in sometime of'
                       'labyrinth ',
        'PATHS': {
            'NORTH': 'LONG WINDING HALLWAY',
            'SOUTH': 'LABYRINTH',
            'UP': 'CEILING',
            'DOWN': 'FLOOR',
            'EAST': 'LABYRINTH',
            'WEST': 'LABYRINTH'
        }
    },
    'NIGHTMARE EDISON': {
        'NAME': 'NiGhTmArE EDiSon.',
        'DESCRIPTION': 'WELCOME! This is Nightmare Edison. It is the same map as before only SPOOKY! Get back to the '
                       'normal world to finish the game',
        'PATHS': {
            'SOUTH': 'NIGHTMARE R19A',
            'NORTH': 'NIGHTMARE W BUILDING',
            'UP': 'NIGHTMARE CEILING',
            'DOWN': 'NIGHTMARE HOBO QUARTERS ',
            'EAST': 'NIGHTMARE PARKING LOT',
            'WEST': 'NIGHTMARE SCIENCE BUILDING'
        }
    },
    'CEILING': {
        'NAME': 'The Ceiling',
        'DESCRIPTION': 'This is the ceiling. Do not go up, again!',
        'PATHS': {
            'NORTH': 'CEILING',
            'EAST': 'CEILING',
            'WEST': 'CEILING',
            'SOUTH': 'CEILING',
            'UP': 'CEILING'
        }

    },
    'SHAKESPEARE WORLD': {
        'NAME': 'Shakespeare World',
        'DESCRIPTION': 'You are now in a medieval area. The buildings are that of 16th century. Everyone around you'
                       'is wearing some type of Victorian clothing. In this world, you must act on a play. Essentially'
                       'You are dropped into the world of the play and must find the way out.',
        'PATHS': {
            'NORTH': 'HAMLET',
            'SOUTH': 'OTHELLO',
            'UP': 'THE GENTLEMEN OF VERONA',
            'DOWN': 'THE MERCHANT OF VENICE',
            'EAST': 'TAMING OF THE SHREW',
            'WEST': 'ROMEO AND JULIET',

        }
    },
    'THE SPANISH DILEMMA': {
        'NAME': 'LA PROBLEMA DE ESPANOL',
        'DESCRIPTION': 'Este cuarto tiene una problema ese necesita resolver. '
                       'Tu necesecitas resolver la problema rapidamente. '
                       'Si tu resuelves en tiempo, tu seras GANAR!',
        'PATHS': {
            'SOUTH': 'PROBLEMA UNO',
            'DOWN': 'PROBLEMA DOS',
            'UP': 'CEILING',
            'EAST': 'PROBLEMA TRES',
            'WEST': 'DIFICIL'

        }
    },
    'FLOOR': {
        'NAME': " The FLOOR",
        'DESCRIPTION': 'This is the floor',
        'PATHS': {
            'NORTH': 'FLOOR',
            'SOUTH': 'FLOOR',
            'EAST': 'FLOOR',
            'WEST': 'FLOOR',
            'UP': 'FLOOR',
            'DOWN': 'FLOOR'
        }



    }



}

# Controller
playing = True
current_node = world_map['R19A']
directions = ['NORTH', 'SOUTH', 'NORTHEAST', 'SOUTHEAST', 'SOUTHWEST', 'NORTHWEST', "WEST", "EAST", "UP", "DOWN"]
while playing:
    print(current_node["NAME"])
    print(current_node["DESCRIPTION"])
    command = input(">_")
    if command.lower() in ["q", "quit", 'exit']:
        playing = False
        print("GAME OVER.")
    elif command.upper() in directions:
        try:
            room_name = current_node["PATHS"][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way!")
    else:
        print("Command not found")
