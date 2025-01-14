# Prompt the user to enter the number of teams
num_teams = int(input("Enter the number of teams: "))

# Prompt the user to enter the fixed amount for all teams
fixed_amount = float(input("Enter the fixed amount for all teams: "))

# Initialize a dictionary to store team names, their fixed amounts, and players
teams = {input(f"Enter the name of team {i + 1}: "): {"fixed_amount": fixed_amount, "players": []} for i in range(num_teams)}

# Function to display the updated team list with players and remaining amount
def display_teams():
    print("\nUpdated Team List:")
    for team, details in teams.items():
        print(f"Team: {team} (Remaining Amount: ${details['fixed_amount']:.2f})")
        if details["players"]:
            print("  Players:")
            for player in details["players"]:
                print(f"    - {player['name']} (${player['amount_paid']:.2f})")
        else:
            print("  No players assigned yet.")

# Start player assignment loop
while True:
    # Prompt the user for player details
    player_name = input("\nEnter the name of the player (or type 'exit' to stop): ")
    if player_name.lower() == "exit":
        break

    # Display team options with numbers
    print("\nAvailable teams:")
    team_list = list(teams.keys())
    for idx, team in enumerate(team_list, start=1):
        print(f"{idx}. {team}")

    # Prompt the user to select a team by number
    while True:
        try:
            team_choice = int(input("Enter the number corresponding to the team where the player will go: "))
            if 1 <= team_choice <= len(team_list):
                team_name = team_list[team_choice - 1]
                break
            else:
                print("Invalid choice. Please select a valid team number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Enter the amount paid for the player
    while True:
        amount_paid = float(input(f"Enter the amount paid for {player_name}: "))
        if amount_paid > teams[team_name]["fixed_amount"]:
            print(f"Insufficient funds! {team_name} only has ${teams[team_name]['fixed_amount']:.2f} remaining.")
        else:
            break

    # Assign player to the selected team and update the team's fixed amount
    teams[team_name]["players"].append({"name": player_name, "amount_paid": amount_paid})
    teams[team_name]["fixed_amount"] -= amount_paid

    # Display the updated team list
    display_teams()

print("\nAuction completed!")
