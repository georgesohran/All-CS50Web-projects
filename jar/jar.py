class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        if self.capacity < 0:
            raise ValueError
        self.size = 0

    def __str__(self):
        return "🍪"*self.size

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError
        self.size -= n

    @property
    def capacity(self):
        return self._house

    @property
    def size(self):
        return self._size

