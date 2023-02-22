# Michael Williams

#importing time so that if the player decides to not play there is a delay before program exits
import time


def show_instructions():
    # print game instructions
    print("Kraken Text Adventure Game")
    print(' ')
    print("You were just attacked by the mighty Kraken and\ncrash landed on a nearby island!")
    print("Your mission is fix your ship by scavenging items\non the island so you can return to the ocean and slay "
          "the Kraken.")
    print(' ')
    print("Collect 6 items to win the game, or be eaten by the Kraken.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")


def show_status(current_room, inventory, rooms):
    # print current location, inventory, and item in room (if there is one)
    print(f'Your current location is {current_room}')
    print(f'Inventory: {inventory}')

    # if there is an item in the room
    while "item" in rooms[current_room]:
        # if that item is Gun-Powder or Oranges
        if rooms[current_room]['item'] == 'Gun-Powder' or rooms[current_room]['item'] == 'Oranges':
            print(f"You see {rooms[current_room]['item']}")
        # if item is Kraken-Canon or Kraken
        elif rooms[current_room]['item'] == 'Kraken-Canon' or rooms[current_room]['item'] == 'Kraken':
            print(f"You see the {rooms[current_room]['item']}")
        # otherwise
        else:
            print(f"You see a {rooms[current_room]['item']}")
        break

    if current_room != 'Cape Kraken':
        print('-' * 60)


def main():
    # dictionary to map rooms to other rooms and items
    rooms = {
        "Pirate's Graveyard": {'West': 'Ahoy Reef'},
        "Ahoy Reef": {'East': "Pirate's Graveyard", 'South': "Black Beard's Den", 'item': 'Sail'},
        "Black Beard's Den": {'North': "Ahoy Reef", 'East': 'Sea-Sick Bridge', 'South': 'Dead Water Bay',
                              'West': 'Cast Away Peak', 'item': 'Sword'},
        "Cast Away Peak": {'East': "Black Beard's Den", 'item': 'Gun-Powder'},
        "Dead Water Bay": {'North': "Black Beard's Den", 'East': 'Scurvy Lagoon', 'item': 'Compass'},
        "Scurvy Lagoon": {'West': 'Dead Water Bay', 'item': 'Oranges'},
        "Sea-Sick Bridge": {'North': 'Cape Kraken', 'West': "Black Beard's Den", 'item': 'Kraken-Canon'},
        "Cape Kraken": {'South': 'Sea-Sick Bridge', 'item': 'Kraken'}
    }

    # list that stores the acceptable commands for directions
    directions = ['North', 'East', 'West', 'South']
    # list that stores the acceptable commands for items
    dict_items = ['Sail', 'Sword', 'Gun-Powder', 'Compass', 'Oranges', 'Kraken-Canon', 'Kraken']

    # initialize current_room and inventory
    current_room = "Pirate's Graveyard"
    inventory = []
    print("Your current location is Pirate's Graveyard.")
    print(f'Inventory: {inventory}')
    print('-' * 60)

    # take input from user, split, and capitalize each phrase
    command = str(input('Enter command: ')).title().split()

    while True:

        # if location is Sea-Sick Bridge and choose to Go North (direction of final room)
        if current_room == 'Sea-Sick Bridge' and ' '.join(command) == 'Go North':
            show_status(rooms[current_room]['North'], inventory, rooms)

            # If inventory has 6 items
            if len(inventory) == 6:
                print('Congratulations! You have collected all items and defeated the Kraken!')
                print('Thanks for playing the game. Hope you enjoyed it.')
                break

            # If inventory doesn't have 6 items
            else:
                print('NOM NOM...GAME OVER!')
                print('Thanks for playing the game. Hope you enjoyed it.')
                break

        # If at room/location that is not Sea-Sick Bridge
        else:

            # invalidates input if user only presses enter
            if ''.join(command) == '':
                command = str(input("Invalid Command, try again: ")).title().split()
                continue

            # if first word of command is 'Go'
            elif command[0] == 'Go':
                # if second word of command is North, East, South, or West
                if command[1] in rooms[current_room].keys():
                    # move to room in that direction, show player status, and prompt input
                    current_room = rooms[current_room][command[1]]
                    show_status(current_room, inventory, rooms)
                    command = str(input('Enter command: ')).title().split()

                # if user picks a direction that is not in room dictionary
                elif command[1] not in rooms[current_room].keys() and command[1] in directions:
                    command = str(input("Can't go that direction, enter new command: ")).title().split()

                # if second word in command is not North, East, South, or West
                else:
                    command = str(input("Invalid command, try again: ")).title().split()

            # if first word in command is 'Get'
            elif command[0] == 'Get':

                # if second word in command is an item in the room
                if command[1] in rooms[current_room].values():
                    # add item to inventory list
                    inventory.append(rooms[current_room]['item'])
                    print(f"{rooms[current_room]['item']} obtained!")
                    # remove 'item' key phrase from the dictionary of the room you are currently in
                    del rooms[current_room]['item']
                    # show player status, prompt for input
                    show_status(current_room, inventory, rooms)
                    command = str(input('Enter command: ')).title().split()
                    continue

                # if second word not in current_room dictionary AND isn't an item in the game
                elif command[1] not in rooms[current_room].values() and command[1] in dict_items:
                    print(f"Can't get {command[1]}")
                    print('-' * 60)
                    command = str(input("Enter command: ")).title().split()

                # if item is not an item found in dictionary, Invalid, try again.
                else:
                    command = str(input("Invalid command, try again: ")).title().split()
                    continue

            # if user input doesn't satisfy any of those, prompt user for input again.
            else:
                print('-' * 60)
                command = str(input("Invalid Command, try again: ")).title().split()
                continue


# run show_instructions() and main() functions

#gameplay loop

#prompt user
user_input = str(input('Would you like to play my game? (yes/no): ')).title()
print('-' * 60)

while True:
    #if user wants to play
    while user_input != 'No':
        #show game instructions, run game
        if user_input == 'Yes':
            show_instructions()
            print('-' * 60)
            main()
            #once game is finished, ask if player wants to play again and then restart loop
            user_input = input('Would you like to play again?: (yes/no) ').title()
            print('-' * 60)
            continue
        #if user doesn't type in yes or no
        else:
            user_input = input('Invalid response, please type yes or no: ').title()
            break
    #if user types no
    else:
        print('Too bad, play with us some other time!')
        time.sleep(1)
        print("Game terminating in...")
        time.sleep(1)
        print('3...')
        time.sleep(1)
        print('2...')
        time.sleep(1)
        print('1...')
        time.sleep(1)
        break
