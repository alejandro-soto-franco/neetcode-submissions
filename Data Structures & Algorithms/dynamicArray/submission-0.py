class DynamicArray:
    
    # assume capacity > 0.
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        # See note 1
        self.arr = [0] * self.capacity

# Get value at the i-th index
    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        
        # insert at next empty position
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
        return self.arr[self.length]
 

    def resize(self) -> None:
        # Create a new array of double capacity
        self.capacity *= 2
        new_arr = [0] * self.capacity

        # Copy elements to new_arr
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr


    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity

# Note 1: Python allocates exactly one integer object for 0 on the heap
# It allocates a contiguous block of memory to hold `capacity` number of pointers
# So Python fills that array by compying the memory address of that 0 object into every slot