import random

def number_guessing_game():
    # Define the range for the random number
    lower_bound = 1
    upper_bound = 100
    
    # Generate a random number within the range
    secret_number = random.randint(lower_bound, upper_bound)
    
    # Set the maximum number of attempts
    max_attempts = 10
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
    
    while attempts < max_attempts:
        try:
            # Get the player's guess
            guess = int(input("Take a guess: "))
            
            # Check if the guess is within the range
            if guess < lower_bound or guess > upper_bound:
                print(f"Please guess a number between {lower_bound} and {upper_bound}.")
                continue
            
            # Increment the attempt count
            attempts += 1
            
            # Provide feedback
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")
    
    if attempts == max_attempts and guess != secret_number:
        print(f"Sorry, you've run out of attempts. The number was {secret_number}.")

# Start the game
number_guessing_game()
