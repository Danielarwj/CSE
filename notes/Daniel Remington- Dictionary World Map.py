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
            'EAST': 'HOBO ATTACKS YOU'
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
            'UP': '2030',
            'DOWN': 'CHERNOBYL',
            'EAST': 'HOBO ATTACKS YOU',
            'WEST': 'QUAD'
        }
    },
    'QUAD': {
        'NAME': 'The Quad',
        'DESCRIPTION': 'The main area. There is an ampitheatre here. There is also a couple of lamp posts',
        'PATHS': {
            'WEST': 'W BUILDING',
            'EAST': 'R BUILDING'
        }
    },
    'W BUILDING': {
        'NAME': 'W Building',
        'DESCRIPTION': 'This is the W Building. It is a two story masterpiece of a building. '
                       'It,conveniently, is the building for languages',
        'PATHS': {
            'UP': 'LPDE',
            'DOWN': 'TFP'

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
            'NORTH': 'NIGHTMARE EDISON'
        }
    },
    'R BUILDINGS': {
        'NAME': 'The R buildings',
        'DESCRIPTION': 'This is a row of buildings. You can only go North, however. The other areas are blocked off.',
        'PATHS': {
            'NORTH': 'THE ESSAY TYPING SESSION'
        }
    },
    'HOBO WORLD': {
        'NAME': 'Hobo World',
        'DESCRIPTION': 'YoU haVe DECidEd tO Go SoUtH! Welcome to Hobo World, the realm of the desolate and the weak'
                       'Here, you must complete one of'
                       ' three challenges- Garbage collecting, tent folding, and the hardest one of '
                       'all, finding 4 pieces of food. After you face these challenges, you win the game!',
        'PATHS':{
            'NORTH': 'THE CHALLENGE AREA'
        }
    },
    'POOL': {
        'NAME': 'POOL'
    },
    'THE CHALLENGE AREA':{
        'NAME': 'THE CHALLENGE AREA',
        'DESCRIPTION': 'If you go north, you collect garbage. If you go south, you fold tents. If you go east, '
                   'you find food',
        'PATHS': {

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
