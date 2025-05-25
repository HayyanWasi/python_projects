class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"total books created: {cls.count}")
        

obj1 = Counter()
obj2 = Counter()

Counter.display_count()