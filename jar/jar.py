class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity

    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        return self._house

    @property
    def size(self):
        ...

    @capacity.setter
    def capacity(self,capacity):
        if self._capacity < 0:
            raise ValueError
        self._capacity = capacity