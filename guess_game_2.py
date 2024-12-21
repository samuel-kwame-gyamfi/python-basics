import random

# Generate a random secret number between 1 and 10
secret_number = random.randint(1, 10)

# Initialize the guess count and the initial guess
guess_count = 0
guess = 0

# Start the guessing loop
while guess != secret_number:
    # Ask the user for a guess
    guess = int(input("Enter your guess (between 1 and 10): "))
    
    # Increase the guess count
    guess_count += 1
    
    # Check if the guess is too high, too low, or correct
    if guess > secret_number:
        print("Your guess is too high!")
    elif guess < secret_number:
        print("Your guess is too low!")
    else:
        print(f"Congratulations! You guessed the number in {guess_count} tries.")
