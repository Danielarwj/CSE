world_map = {
    'R19A': {
        'NAME': "Mr. Wiebe's room",
        'DESCRIPTION': "This is the classroom you are in right now. "
                       "There are two doors on the north wall",
        'PATHS': {
            'NORTH': 'PARKING_LOT',
            'EAST': 'DRAMA BUILDING',
            'WEST': 'SCIENCE BUILDING',
            'SOUTH': 'QUAD'

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
        'DESCRIPTION': "There is a homeless person here. He does not like you. He hits you!",
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
                       'It,conveniently, is the building for languages'
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
