#Use the abc module to create an abstract class Shape with an abstract method area().
#Inherit a class Rectangle that implements area().

from abc import abstractmethod, ABC
class Shape(ABC):
    @abstractmethod
    def add(self):
        pass

class Rectangle(Shape):                     #instantiate Rectangle from shape
    def __init__(self, width, length):
        self.length = length
        self.width = width
    def add(self):                          #implementation for abstract add amthd for reactangle
       return self.length * self.width      #Calc for reactangle
    

rect = Rectangle(3, 3)
print(rect.add())


        

