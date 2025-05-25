class Logger:
    def __init__(self):
        print("Logger created")

    def __del__(self):
                print("Logger destroyed")
        

obj1 = Logger()
del obj1    #explicitly destroyed
obj2 = Logger()
del obj2  #explicitly destroyed
