class Engine:
    def start(self)-> str:
        print("engine starting")


class Car:
    def __init__(self):
        self.engine = Engine()

    def starting(self):
        self.engine.start()
        print("car starting")


my_car = Car()
my_car.starting()