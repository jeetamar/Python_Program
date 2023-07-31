# Encapsulation
"""
    Encapsulation is the process of hiding the internal implementation details of an object and exposing only the necessary information.
     It helps in achieving data security and code maintainability.
"""
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def start_engine(self):
        print("Engine started.")
my_car = Car("Ford", "Mustang")
print(my_car.brand)

my_car.start_engine()


# Inheritance

"""
    Inheritance is a mechanism where a class inherits properties and methods from a parent class.
     It allows code reuse and the creation of specialized classes based on more general classes.
"""
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Animal speaks.")
class Dog(Animal):
    def speak(self):
        print("Woof!")
my_dog = Dog("Buddy")
print(my_dog.name)
my_dog.speak()


#   Polymorphism:
"""
   
Polymorphism allows objects of different classes to be treated as objects of a common base class.
 It provides flexibility and extensibility in handling objects of different types.
"""

class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print(shape.area())



# Abstraction
"""
    Abstraction involves representing essential features of an object while hiding the unnecessary details.
    It allows programmers to work with high-level concepts without worrying about implementation specifics.
"""
from abc import ABC, abstractmethod
class Shape(ABC):
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
my_rectangle = Rectangle(4, 5)
my_circle = Circle(3)
print(my_rectangle.area())  #Output: 20
print(my_circle.area())