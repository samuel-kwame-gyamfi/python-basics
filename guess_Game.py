import random

secret_number = random.randint(1,10)

guess = int(input("Enter Number:"))

match guess:
    case high if guess > secret_number:
        print("Your number is too high")
    case low if guess < secret_number:
        print("Your number is too low")
    case correct if guess == secret_number:
        print("Congratulations you had it right🎉🎉🎉")