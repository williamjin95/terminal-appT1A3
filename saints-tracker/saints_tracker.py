def main_menu():
    while True:
        print("\nAFL Team Tracker\n")
        print("1. View Team Stats")
        print("2. View Upcoming Games")
        print("3. Exit")

        choice = input("Enter your choice [1-3]: ")

        if choice == '1':
            view_team_stats()
        elif choice == '2':
            view_upcoming_games()
        elif choice == '3':
            print("Exiting... Thank you for using the AFL Team Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")

def view_team_stats():
    print("Team Stats will be displayed here.")

def view_upcoming_games():
    print("Upcoming games will be displayed here.")

if __name__ == "__main__":
    main_menu()
