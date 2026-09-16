class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [None] * capacity
        self.cap = capacity
        self.back = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            self.resize()
        
        self.array[self.back] = n
        self.back += 1

    def popback(self) -> int:
        self.back -= 1
        pop = self.array[self.back]
        self.array[self.back] = None
        return pop

    def resize(self) -> None:
        copy = self.array.copy()
        self.cap = self.cap * 2
        self.array = [None] * self.cap
        for i in range(len(copy)):
            self.array[i] = copy[i]

    def getSize(self) -> int:
        size = 0
        for element in self.array:
            if element is not None:
                size +=1
        return size
    
    def getCapacity(self) -> int:
        return self.cap