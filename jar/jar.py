class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        if self.capacity <= 0:
            raise ValueError
        self.size = 0

    def __str__(self):
        return "🍪"*self.size

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n
        if self.size < 0:
            raise ValueError


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self,capacity):
        self._capacity = capacity
        if capacity<=0:
            raise ValueError

    @size.setter
    def size(self,size):
        self._size = size


