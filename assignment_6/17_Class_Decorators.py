def add_greeting(cls):

    def greet(self):
        return "Hello from decorator"

    cls.greet = greet
    return cls


@add_greeting
class Person:
    pass

P = Person()
print(P.greet())


     



