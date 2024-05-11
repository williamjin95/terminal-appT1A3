def main_menu():
    while True:
        print("\nAFL Team Tracker")
        print("1. View Team Stats")
        print("2. View Upcoming Games")
        print("3. List Players")
        print("4. View Player Stats")
        print("5. Exit")

        choice = input("Enter your choice [1-5]: ")

        if choice == '1':
            view_team_stats()
        elif choice == '2':
            view_upcoming_games()
        elif choice == '3':
            list_players()
        elif choice == '4':
            player_name = input("Enter the name of the player to view stats: ")
            show_player_stats(player_name)
        elif choice == '5':
            print("Exiting... Thank you for using the Saints Team Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")

def view_team_stats():
    stats = {'St Kilda Saints': {'Wins': 3, 'Losses': 5}}
    for team, record in stats.items():
        print(f"{team}: Wins: {record['Wins']}, Losses: {record['Losses']}")

import json

def view_upcoming_games():
    try:
        with open('upcoming_matches.json', 'r') as file:
            games = json.load(file)
        print("\nUpcoming Games:")
        for game in games:
            print(f"{game['date']}: {game['match']}")
    except FileNotFoundError:
        print("The data file is missing.")
    except json.JSONDecodeError:
        print("Data file is not in proper JSON format.")

if __name__ == "__main__":
    main_menu()

