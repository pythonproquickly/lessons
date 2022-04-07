from constants import TEAMS, PLAYERS

import copy

teams = copy.deepcopy(TEAMS)
players = copy.deepcopy(PLAYERS)


def start():
    print("Basketball Team Stats Tool")
    print("----MENU----")
    print("Here are your choices:")
    print("1: Display Team Stats")
    print("2: Quit")


def first_menu():
    selection = input("Enter An Option:  ")
    if (selection == "1"):
        # print(teams_with_players[])
        # I also want each of the teams with players to be a choice
        print("Please select a team to view:")
        print(f'''
        1) {TEAMS[0]}   
        2) {TEAMS[1]}
        3) {TEAMS[2]}''')
        select_team()
    elif (selection == "2"):
        print("Have a nice day!")
        # break
    else:
        print("Please select 1 or 2.")
        # continue


# Create a clean_data function
def clean_constants():
    for player in players:
        player["height"] = player['height'].split()
        player['height'] = int(player['height'][0])
        player['guardians'] = player['guardians'].split(" and ")
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
    return players, teams


def assign_players(players, teams):
    Panthers = []
    Bandits = []
    Warriors = []
    # all_players_list = copy.deepcopy(PLAYERS)
    experienced_players = len([player['experience'] for player in players if
                               player['experience'] == True])
    inexperienced_players = len([player['experience'] for player in players if
                                 player['experience'] == False])
    guardians = [", ".join(player['guardians']) for player in team]

    players_lists = [Panthers, Bandits, Warriors]

    num_teams = len(teams)
    for num in range(len(players)):
        players_lists[num % num_teams].append(players[num])

    return Panthers, Bandits, Warriors, players


# I need something that tells to show stats for the appropriate team
def select_team():
    choice = input("Please select a team from the list")
    if choice == '1':
        display_stats(Panters, "Pathers")
    elif choice == '2':
        display_stats(Bandits, "Bandits")
    elif choice == '3':
        display_stats(Warriors, "Warriors")
    else:
        print("Please choose 1, 2 or 3")


def display_stats(team, team_name):
    while True:
        try:
            players_on_team = [player['name'] for player in team]
            average_height = round(
                sum([player["height"] for player in team]) / len(
                    players_on_team), 2)
            print("TEAM: {} Stats".format(team_name))
            # above is not right- I want it to use the correct team
            print("-" * 20, "\n")
            print("Total Players: {}".format(len(team)))
            print("Player on Team: ", end="")
            print(", ".join(players_on_team))
            for player in players_on_team:
                if player == players_on_team[1]:
                    # something goes in []
                    print(player, ",")
                else:
                    # what does it do- not print player?
                    print("Guardians: ", end="")
            for guardian in guardians:
                if guardian == guardians():
                    # again identify team []
                    print(guardian, end="\n\n")
                else:
                    print(guardian, end=", ")
                    print("Number of Experienced Players: {}".format(
                        experienced_players))
                    print("Number of Inexperienced Players: {}".format(
                        inexperienced_players))
                    print(
                        "Average Height: {} inches\n\n".format(average_height))
                    input("Press Enter to continue.")
                    first_menu()


if __name__ == "__main__":
    Panthers, Bandits, Warriors, teams_list = assign_players(
        *clean_constants())
    start()
    first_menu()


