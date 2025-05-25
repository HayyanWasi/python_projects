class Person:
    def __init__(self, name):
        self.name = name
    
class Teacher(Person):
    def __init__(self, name, subject):
        self.subject = subject
        super().__init__(name)
        

person = Teacher("Zayn", "python")
print(f"Teacher is {person.name} and he teaches {person.subject}" )






























# class Car:
#     color = 'red'
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("Car stopped")

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("fortuner")
# car2 = ToyotaCar("prius")

# print(car1.name)
# print(car1.color)
# print(car1.start())