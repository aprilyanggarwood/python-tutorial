class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name} Age: ({self.age})"

    def greet(self):
        print("Hi")
        for i in range(1, 10):
            print("hi")

    def greet(self):
        print("Hi")
        for i in range(1, 10):
            print("hi")



class Dog:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Bark")

class Shape:
    
    def __init__(self, color):
        self.color = color

class Rectangle(Shape):
    
    def __init__(self, width, length):
        super().__init__("Blue")
        self.width=width
        self.length=length

class Circle(Shape):
    
    def __init__(self, diameter):
        super().__init__("Green")
        self.diameter = diameter
        