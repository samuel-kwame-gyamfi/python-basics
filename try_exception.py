try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter Second number: "))
    result = num1 /num2
    print(f"The division of {num1} and {num2} is {result}")
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("Enter a valid number")