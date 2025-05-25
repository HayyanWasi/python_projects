#Creating class
class Student:
    #creating constructor
    def __init__ (self, name ,marks):
        self.name = name
        self.marks = marks

    #using self to get the instance of the class
    def display(self):
            print( "Name:{self.name}, Marks:{self.marks}")

    
student1 = Student("Hayyan",76)
student2 = Student("Sudais", 79)
student3 = Student("alis",78)

student1.display()
student2.display()
student3.display()

