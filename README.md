# Terminal App T1A3 #

## R4 ##

https://github.com/williamjin95/terminal-appT1A3

## R5 ##

This project follows the guidelines outlined in [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code styling and conventions.

## R6 ##

1. View Team Stats
Description: Displays wins and losses for each AFL team.
Logic: Retrieves team data from a source (e.g. JSON or CSV). Iterates over the data and displays each team's stats.

2. View Upcoming Games
Description: Lists the dates and matchups of upcoming games.
Logic: Reads game details from upcoming_matches.json. Parses and displays each game in a list.

3. List Players
Description: Shows a list of players and their teams.
Logic: Loads player data from players_stats.json. Outputs each player's name alongside their team.

4. View Player Stats
Description: Displays detailed statistics for a specified player.
Logic: Prompts for a player name. Searches and displays detailed stats if the player is found.

5. Compare Two Players
Description: Compares statistics between two specified players.
Logic: User inputs names of two players. Searches for and displays stats side-by-side for comparison.

6. Exit
Description: Terminates the application.
Logic: Breaks the main menu loop, closing the program.

Overall Workflow
Users interact with a main menu that loops continuously for navigation.
Selections trigger appropriate data handling and display functions.
Error handling is integrated to ensure smooth operation and clear user feedback.

## R7 ##

1. View Team Stats
Priority: High
Duration: 0.5 day
Checklist:

- Design the data model for team stats.
- Implement function to load team stats from JSON.
- Create display logic in the application.
- Add to the main menu.
- Test team stats display functionality.

2. View Upcoming Games
Priority: High
Duration: 1 day
Checklist:

- Design data model for storing game schedules.
- Implement function to read upcoming games from JSON.
- Develop logic to display games clearly.
- Add to the main menu.
- Conduct testing with various game scenarios.

3. List Players
Priority: Medium
Duration: 1 day
Checklist:

- Define player data structure.
- Load player information from JSON.
- Implement player listing in the UI.
- Test for correct player data display.
- Ensure the names are correct.

4. View Player Stats
Priority: Medium
Duration: 1 day
Checklist:

- Ensure player stats are properly structured.
- Create function to search and display stats.
- Integrate player search into the main menu.
- Test searching and viewing functionality.
- Verify the accuracy of the numbers.

5. Compare Two Players
Priority: Low
Duration: 1 day
Checklist:

- Design comparison logic for two players.
- Create UI for selecting and comparing players.
- Implement comparison display format.
- Add the comparison feature to the main menu.
- Test comparison for accuracy and usability.

6. Exit
Priority: Low
Duration: 0.5 day
Checklist:

- Implement exit functionality in the main menu.
- Ensure clean shutdown of the app.
- Test exit under various conditions.
- Check exit code to optimize performance.

[Trello Board](https://trello.com/b/34bz64G8)

## R8 ##

System Requirements
OS: Windows 10/8/7, macOS, or Linux.
Python: Version 3.7+.
RAM: Minimum 256 MB.
Storage: At least 100 MB free.

- Download python from python.org.
- Download the AFL Team Tracker from the provided source.
- Extract files to a desired location.
- Navigate to the app's folder in a command prompt or terminal.
- Start the app with: python or python3 afl_tracker.py
- Main Menu Options: View Team Stats, View Upcoming Games, List Players, View Player Stats, Search for Player, Compare Two Players & Exit
- Type the option number and press Enter.
- Follow prompts for specific actions.
