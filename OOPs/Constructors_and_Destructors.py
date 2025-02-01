# Create a Person class with attributes like name and age. Implement a constructor (__init__) to initialize these attributes.
# Also, implement a destructor (__del__) method to print a farewell message when an object is deleted

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print (f" My name is {self.age} and I am {self.age} years old")
    def __del__(self):
        print("User info is being deleted")
    
person1 = Person("samuel",21)
person1.info()