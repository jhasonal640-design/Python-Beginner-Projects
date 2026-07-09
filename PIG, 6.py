import random

def roll():
    return random.randint(1, 6)

# Get number of players
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid input. Please enter a number.")

target_score = 50
player_scores = [0 for _ in range(players)]

# Game loop
winner_found = False
while not winner_found:
    for player_idx in range(players):
        print("\nPlayer", player_idx + 1, "turn just started.")
        print("Your total score is", player_scores[player_idx], "\n")
        current_score = 0 

        while True:
            should_roll = input("Would you like to roll the dice? (y/n): ")
            if should_roll.lower() != "y":
                break
                
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a", value, "Current turn score:", current_score)
        
        # Update score after turn
        player_scores[player_idx] += current_score
        print("End of turn. Your total score is", player_scores[player_idx])

        # Check for winner immediately
        if player_scores[player_idx] >= target_score:
            winner_found = True
            print("\nPlayer", player_idx + 1, "wins with a score of", player_scores[player_idx], "!")
            break
