class Multiplier:
    def __init__(self, facor1):
        self.factor1 = facor1

    def __call__(self, x):
        return self.factor1 * x
    

m = Multiplier(5)
print(callable(m))
print(m(10))