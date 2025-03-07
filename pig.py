import random

def roll():
    return random.randint(1, 6)

# Get the number of players
while True:
    num_of_players = input("Enter the number of players (2-4): ")
    if num_of_players.isdigit():
        num_of_players = int(num_of_players)
        if 2 <= num_of_players <= 4:
            break
        else:
            print("Must be between 2 to 4 players.")
    else:
        print("Invalid input. Try again.")

# Set max score (optional customization)
while True:
    max_score = input("Enter the winning score (default is 50): ")
    if max_score.isdigit():
        max_score = int(max_score)
        if max_score > 10:
            break
        else:
            print("Winning score should be greater than 10.")
    else:
        print("Invalid input. Using default value of 50.")
        max_score = 50
        break

# Initialize player scores
player_scores = [0] * num_of_players

# Game loop
while max(player_scores) < max_score:
    for i in range(num_of_players):
        print(f"\n🎲 Player {i+1}'s turn! 🎲")
        print(f"Your total score: {player_scores[i]}")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll? (yes/no): ").strip().lower()
            if should_roll not in ["yes", "y"]:
                break

            value = roll()
            print(f"You rolled: {value}")

            if value == 1:
                print("Oops! You rolled a 1, turn over!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"Your current round score: {current_score}")

        # Add current score to total
        player_scores[i] += current_score
        print(f"Your total score: {player_scores[i]}")

        # Check for a winner
        if player_scores[i] >= max_score:
            print(f"\n🎉 Player {i+1} wins with a score of {player_scores[i]}! 🎉")
            exit()

