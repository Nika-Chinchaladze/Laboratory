"""
Abstract Base class defines the main structure for derived class, that must
have implementations for abstractmethod -> methods that are defined in parent
abstract class. if not we won't be able to execute the program, because TypeError
exception will be raised with message that derived class can't be instantiated
without method that exists in abstract class, but not exists in derived class.
Also, we can't create object directly from Abstract Based Class.

ABC is a helper class that has ABCMeta as its metaclass. With ABC class,
an abstract base class can be created by simply deriving from ABC avoiding
sometimes confusing metaclass usage - during multiple inheritance.

ABC acts as a parent class, that can be subclassed and is visible with __mro__, but ABCMeta is not visible.
"""

from abc import ABC, ABCMeta, abstractmethod


# Abstract Base Class
class Fruit(ABC):

    @abstractmethod
    def get_color(self):
        pass

    @abstractmethod
    def get_shape(self):
        pass

    @abstractmethod
    def get_taste(self):
        pass


# Common class that inherits from Abstract Based Class
class Apple(Fruit):
    def __init__(self, color, shape, taste):
        super().__init__()
        self.color = color
        self.shape = shape
        self.taste = taste

    def get_color(self):
        return self.color

    def get_shape(self):
        return self.shape

    def get_taste(self):
        return self.taste


obj = Apple(color="red", shape="cycle", taste="sweet")
print(obj.get_shape())

print(isinstance(ABC, ABCMeta))  # returns --> True
