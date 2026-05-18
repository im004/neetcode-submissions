class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        # Create a physical list filled with dummy zeros matching the capacity
        self.arr = [0] * capacity


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
            
        # Place the new item at the end of our current filled data
        self.arr[self.length] = n
        self.length += 1


    def popback(self) -> int:
        # Track the item we are about to soft-delete so we can return it
        val = self.arr[self.length - 1]
        self.length -= 1
        return val
 

    def resize(self) -> None:
        # 1. Double the capacity variable
        self.capacity = self.capacity * 2
        
        # 2. Create the new, bigger list
        new_arr = [0] * self.capacity
        
        # 3. Copy old items over
        for i in range(self.length):
            new_arr[i] = self.arr[i]
            
        # 4. Make our main array point to this new bigger array
        self.arr = new_arr


    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
