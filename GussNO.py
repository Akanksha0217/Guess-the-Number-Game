import random

def guess_the_number():
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100
    
    # Generate a random number
    target_number = random.randint(lower_bound, upper_bound)
    max_attempts = 5
    attempts = 0

    print("Welcome to 'Guess the Number'!")
    print(f"I have selected a number between {lower_bound} and {upper_bound}. Can you guess it?")

    while True:
        # Get the player's guess
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number {target_number} in {attempts} attempts.")
            break
        if attempts == max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {target_number}.")
            break

# Run the game
guess_the_number()
