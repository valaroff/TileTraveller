import random
# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def is_victory(col, row):
    ''' Return true is player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")
        
def find_directions(col, row):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions


def pull_lever(col,row, coin_list):

    if col == 1 and row == 2 or col == 2 and row == 2 or col == 3 and row == 2 or col == 2 and row == 3:
        yes_no_seq = ['y','n']
        pull_lever = random.choice(yes_no_seq)
        print('Pull a lever (y/n):',pull_lever)
        if pull_lever == 'y':
            coin_list.append(1)
            coin_sum=sum(coin_list)
            print('You received 1 coin, your total is now {}.'.format(coin_sum))
        else:
            coin_sum=sum(coin_list)
    else:
        coin_sum=sum(coin_list)

    return coin_sum

def play_one_move(col, row, valid_directions,coin_list):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    direction_seq = ['n','s','w','e']
    direction = random.choice(direction_seq)
    print('Direction:',direction)
    
    if not direction in valid_directions:
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
    return victory, col, row

def play_again():
    yes_no_seq = ['y','n']
    play_again = random.choice(yes_no_seq)
    print('Play again (y/n):', play_again)

    if play_again == 'y':
        victory = False
        coin_list = []
        col, row = 1,1
    else: 
        victory = True
        coin_list = []
        col,row = 1,1
    return victory, coin_list, col, row

    

# The main program starts here
victory = False
row = 1
col = 1
coin_list=[]

seed = input('Input seed: ')

valid_directions = NORTH
print_directions(valid_directions)

while not victory:
    victory, col, row = play_one_move(col, row, valid_directions,coin_list)
    coin_sum=pull_lever(col,row,coin_list)
    if victory:
        print("Victory! Total coins {}.".format(coin_sum))
        victory, coin_list, col, row = play_again()
        if not victory:
            valid_directions = find_directions(col, row)
            print_directions(valid_directions)
    else:
        valid_directions = find_directions(col, row)
        print_directions(valid_directions)
