import json

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
    stats = {'St Kilda Saints': {'Wins': 3, 'Losses': 6}}
    for team, record in stats.items():
        print(f"{team}: Wins: {record['Wins']}, Losses: {record['Losses']}")

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

def load_players():
    try:
        with open('player_stats.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("The players file is missing.")
        return []
    except json.JSONDecodeError:
        print("There was an error decoding the players data.")
        return []
players = load_players()

def list_players():
    print("\nList of Players:")
    for index, player in enumerate(players, start=1):
        print(f"{index}. {player['name']}")

def show_player_stats(player_name):
    player = next((p for p in players if p['name'] == player_name), None)
    if player:
        print(f"\nStats for {player['name']}:")
        print(f"Games Played: {player['games_played']}")
        print(f"Goals: {player['goals']}")
        print(f"Tackles: {player['tackles']}")
    else:
        print("Player not found. Please check the name and try again.")

if __name__ == "__main__":
    main_menu()

