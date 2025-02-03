# Static Method for Utility Calculation Instruction:

# Create a class Calculator with static methods for basic mathematical operations like addition and multiplication.
# Implement static methods add() and multiply() to perform these operations.


class Calculator:
    @staticmethod
    def add(x,y):
        return x+y
    def mul(x,y):
        return x*y
    
print(Calculator.add(4,5))