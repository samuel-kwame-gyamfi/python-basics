# Import the random module to generate random numbers
# Generate a list of random numbers between 1 and 10
# Convert the list to a set to remove any duplicate numbers
# Display the list of generated random numbers (including duplicates)
# Display the unique numbers after removing duplicates using the set

import random

numbers = [random.randint(1,10) for i in range(20)]

unique_numbers = set(numbers)

print(f"The random numbers are {numbers}")

print(f"The dublicate numbers are {unique_numbers}")
