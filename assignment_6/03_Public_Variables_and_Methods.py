class Car:
    brand: str

    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        return f"{self.brand}'s Engine started! "

my_car = Car("toyota")
print(my_car.start())