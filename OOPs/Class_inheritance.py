# Class Inheritance Instructions:

# Create a base class Animal with methods like eat and sleep.
# Create a subclass Dog that inherits from Animal and adds a method bark.
# Create instances of both classes and demonstrate method inheritance.

class Animal:
    def eat(self):
        print("It is eating")
    def sleep(self):
        print("it is sleeping")

class Dog(Animal):
    def bark(self):
        print("Woolf Woolf")

dog = Dog()
animal = Animal

dog.eat()