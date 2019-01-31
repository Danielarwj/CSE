world_map = {
    'R19A': {
        'NAME': "Mr. Wiebe's room",
        'DESCRIPTION': "This is the classroom you are in right now. "
                       "There are two doors on the north wall",
        'PATHS': {
            'NORTH': 'PARKING_LOT'

        }
    },
    'PARKING_LOT': {
        'NAME': "The North Parking Lot",
        'DESCRIPTION': "There are a couple cars parked here",
        'PATHS': {
            'SOUTH': 'R19A'
        }
    },
    'R19B': {
        'NAME': "",
        'DESCRIPTION': "",
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
