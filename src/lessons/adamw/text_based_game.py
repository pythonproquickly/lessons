# Adam W


def show_item(rooms, state):
    return rooms[state]["Item"]


def show_status(room, inventory, room_content):
    print(f"Currently in room: {room}")
    print(f"Inventory: [{', '.join(inventory)}]")
    print(f"You see a: {room_content}")


def show_instructions():
    print("Rescue Sister from a Kidnapper")
    print("Collect 6 items and face the kidnapper")
    print("Move commands: Go East, Go North, Go West")
    print("Add to Inventory: get 'item name'")


def main():
    rooms = {
        "Room 1": {
            "East": "Room 2",
            "Item": "Map",
            "North": "Wall",
            "West": "Wall",
            "South": "Wall",
        },
        "Room 2": {
            "North": "Room 3",
            "Item": "Flashlight",
            "East": "Wall",
            "West": "Room 1",
            "South": "Wall",
        },
        "Room 3": {
            "West": "Room 4",
            "Item": "Health Pack",
            "South": "Room 2",
            "East": "Wall",
            "North": "Wall",
        },
        "Room 4": {
            "West": "Room 5",
            "Item": "Camouflage",
            "East": "Room 3",
            "North": "Wall",
            "South": "Wall",
        },
        "Room 5": {
            "West": "Room 6",
            "Item": "Steel Ball",
            "North": "Wall",
            "South": "Wall",
            "East": "Room 4",
        },
        "Room 6": {
            "West": "Room 7",
            "Item": "Baseball Bat",
            "North": "Wall",
            "South": "Wall",
            "East": "Room 5",
        },
        "Room 7": {
            "West": "Room 8",
            "Item": "Picnic Basket",
            "North": "Wall",
            "South": "Wall",
            "East": "Room 6",
        },
        "Room 8": {"Item": "kidnapper"},
    }
    state = "Room 1"
    inventory = []
    while True:
        show_instructions()
        print()
        show_status(state, inventory, show_item(rooms, state))
        print()
        item = show_item(rooms, state)
        if item == "kidnapper":
            print("Kidnapper noticed you, killed you and your sister, " "Game Over!")
            exit(0)
        while True:
            command = input("Enter command: ")
            if command[:3].lower() == "get":
                new_item = rooms[state]["Item"]
                if command[4:].title() != new_item:
                    print(f"Sorry, I don't have a {command[4:]}")
                    continue
                if new_item in inventory:
                    print(f"{new_item} already taken")
                    continue
                inventory.append(new_item)
                print(f"{new_item} added to inventory")
                if len(inventory) == 6:
                    print(
                        "Congratulations! You have collected all items and "
                        "defeated the kidnapper"
                    )
                    exit(0)
                continue
            elif command[:2].lower() == "go":
                direction = command[3:].lower()
                if direction not in ("north", "south", "east", "west"):
                    print("Can only go North, South, East, and West")
                    continue
                new_state = rooms[state][direction.title()]
                if new_state == "Wall":
                    print("Can't move that way; it's a wall!")
                    continue
                state = new_state.title()
                break


if __name__ == "__main__":
    main()
