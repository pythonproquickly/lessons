# First I am gonna define the list of dog types
student_id = ["AOL639", "XIH373", "ZXE280", "JLA010", "ZFS378", "CQC968"]
choice = 0


def menu():
    print("What would you like to do? (select the number you want to do) ")
    print("1.)    Show the list of student IDs ")
    print("2.)    See how many IDs are on the list ")
    print("3.)    See if the student ID exists on the list ")
    print("4.)    Show the index number of a requested ID")
    print("5.)    Add an ID to the list")
    print("6.)    Remove an ID from a list")
    print("7.)    Sort the ID list")
    print("8.)    Find the lowest ID")
    print("9.)    Find the highest ID")
    print("10.)   Copy the list")
    print("11.)   End")
    choice = int(input("Please enter your selection here: "))
    print()
    return choice


choice = menu()


def print_list():
    # Here is an if statement used to seperate our menu items. it loops through the list, printing each item in the list until there arent any more items left to print.
    print("")
    print("This is a list of the student IDs")
    print("---------------------------------")

    for student in student_id:
        print(student)

    print()


def list_length():
    print("There are ", len(student_id), " student IDs")


def search_list():
    search = input("Enter a student ID: ")
    print("")

    if search in student_id:
        print(f"{search} was found in the list.")
    else:
        print(f"{search} was not found in the list.")
    print("")


def find_list_index():
    # This choice uses the 'in' command to search for the item in the list, then uses the .index() to print the index number, if it wasnt in the list, it would return a response saying so
    y = input("What ID do you want your index for?:")
    print("")
    if y in student_id:
        print("The IDs index number is ", student_id.index(y))
    else:
        print("That ID is not in the list")
        print("")


def add_to_list():
    # Here we add an item onto the list by appending the list. It would add an item to the end of the list, then it would print the list in the same format as choice 1
    z = input("Add an ID: ")
    student_id.append(z)
    print(z, " was added to the list")
    print("")
    x = 0
    for index in student_id:
        print(student_id[x])
        x = x + 1


# here is a while loop used to allow the user to select multiple items from the list
while choice != 11:

    if choice == 1:
        print_list()
        menu()
    #

    elif choice == 2:
        print("\nShow how many items are in list")
        print("There are ", len(student_id), " in the list\n ")
        # Here we are telling the user how long the list is by calling the length of the list

    elif choice == 3:
        print("\nShow if student id is in the list")
        search = input("Enter a student id to find: ")
        if search in student_id:
            print("Student id found")
        else:
            print("Student id not found")
        print()
        # Here is where we take an input from a user and search for the input in the list yielding 2 returns. One if the input was in the list, and one otherwise.

    elif choice == 4:
        print("\nShow index number of requested student id")
        search = input("Find the index of the student id: ")
        if search in student_id:

            print("The index number of ", search, " is ", student_id.index(search))
        else:
            print("Index number not found")
        print()

    elif choice == 5:
        print("\nAdd a student id to the list")
        search = input("What student id would you like to add: ")
        student_id.append(search)
        print_list()

    elif choice == 6:
        # by using ".remove()" we remove an ID on the list, and if the input is not on the list, we print a statement saying that the ID entered was not ont the list, Then it prints the list
        z = input("Delete an ID: ")
        if z in student_id:

            student_id.remove(z)
            print(z, " was removed to the list")
            print("")
            x = 0
            for index in student_id:
                print(student_id[x])
                x = x + 1
        else:
            print("That ID is not in the List")

    elif choice == 7:
        # Here we sort the list alphabetically
        student_id.sort()
        print("The list is sorted now")
        print(student_id)

    elif choice == 8:

        # This prints the lowest index in the list (the first item)
        print("\nShow the student id that is the minimum")
        print("The lowest student id", min(student_id), " in the list\n ")

    elif choice == 9:

        # This prints the highest index on the list
        print("\nShow the student id that is the maximum")
        print("The highest student id", max(student_id), " in the list\n ")

    elif choice == 10:
        # This code copys our original list into "new_list", then we print the original and the new list.

        new_list = student_id.copy()

        print("Here is the new list")
        print(new_list)
        print("Here is the first list")
        print(student_id)

    choice = menu()
