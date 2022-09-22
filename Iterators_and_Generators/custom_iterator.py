# implement an iterator in a custom class:

class Counter:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.low < self.high:
            num = self.low
            self.low += 1
            return num
        raise StopIteration


for num in Counter(0, 10):
    print(num)
