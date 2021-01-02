class CircularQueue:
    def __init__(self, n):
        self.max_size = n
        self.data = [None] * n
        self.size = 0
        self.tail = 0
        self.head = 0

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.max_size 

    def enqueue(self, x):
        if self.isFull():
            raise IndexError("Queue full")
        
        self.tail = (self.tail + 1) % self.max_size
        self.data[self.tail] = x
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue empty")
        
        self.head = (self.head + 1) % self.max_size
        x = self.data[self.head]
        self.size -= 1
        return x

    def peek(self):
        if self.isEmpty():
            raise IndexError("Queue empty")
        return self.data[(self.head + 1) % self.max_size]
    
    def printQueue(self):
        print(slef.data)

if __name__ == "__main__":
    lq = CircularQueue(5)
    lq.enqueue(1)
    lq.enqueue(2)
    lq.enqueue(3)
    lq.enqueue(4)
    lq.enqueue(5)
    lq.printQueue()
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
    lq.printQueue()
