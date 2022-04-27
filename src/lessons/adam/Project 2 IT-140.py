#Declaration
rooms = {
    'Room 1' : {'East' : 'Room 2', 'Item': 'Map', 'North' : 'Wall', 'West' : 'Wall', 'South' : 'Wall'},
    'Room 2' : {'North': 'Room 3', 'Item': 'flashlight', 'East': 'Wall', 'West': 'Room 1', 'South': 'Wall'},
    'Room 3' : {'West': 'Room 4', 'Item': 'Health Pack', 'South': 'Room 2', 'East': 'Wall', 'North': 'Wall'},
    'Room 4' : {'West': 'Room 5', 'Item': 'Camouflage', 'East': 'Room 3', 'North': 'Wall', 'South': 'Wall'},
    'Room 5' : {'West': 'Room 6', 'Item': 'Steel Ball', 'North': 'Wall', 'South': 'Wall', 'East': 'Room 4'},
    'Room 6' : {'West': 'Room 7', 'Item': 'Baseball Bat', 'North': 'Wall', 'South': 'Wall', 'East': 'Room 5'},
    'Room 7' : {'West': 'Room 8', 'Item:': 'Picnic Basket', 'North': 'Wall', 'South': 'Wall', 'East': 'Room 6'},
    'Room 8': {'Item':'kidnapper'}
}
state = 'Room 1'
def get_new_state(states, directions):
    new_state = states
    for i in rooms:
        if i == states and directions in rooms[i]:
            new_state=rooms[i] [directions]

    return new_state

def get_items(state):
    return rooms [state] ['Items']

def show_instructions():
    print('Rescue Sister from a Kidnapper')
    print('Collect 6 items and face the kidnapper')
    print('Move commands: Go East, Go North, Go West')
    print(f'{item_name} was added to your inventory')
show_instructions()
inventory=[]
while 1:
    print('You are in ', state)
    print('Inventory: ', inventory)
    item = get_items(state)
    print('You see a', item)
    if item == 'kidnapper':
        print('Kidnapper noticed you, killed you and your sister, Game Over!')
        exit(0)
    direction = input('Enter your move: ')
    direction = direction[3:]
    new_state = get_new_state(state, direction)
    if new_state == state:
        print('The room has a wall in that direction, enter another direction!')
    else:
        state = new_state
    elif direction == str('get '+item):
    else:
    print('Invalid Direction!')

    if item in inventory:
        print('Item already taken, go to another room')
    else:
        inventory.append(item)

if len(inventory) == 6:
    print('Congratulations! You have collected all items and defeated the kidnapper')
    exit(0)

def play():

def main():
    play()

if __name__ == "__main__":
        main()
