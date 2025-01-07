def odd_even():
    # Ask the user to input a number
    number = int(input("Enter your number to check if it's even or odd: "))
    
    # Check if the number is even or odd
    if number % 2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")

# Call the function to run the code
odd_even()

