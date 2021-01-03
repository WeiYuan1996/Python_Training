class CircularQ:
    def __init__(self,maxSize):
        self._queue = list()
        self._maxSize = maxSize
        self._head = 0
        self._tail = 0

    def size(self):
        if self._tail >= self._head:
            return self._tail - self._head
        else:
            return self._maxSize-(self._head- self.tail)
    
    def enqueue(self,data):
        if self._maxSize-1 == self.size():
            print("this queue is full we are not allow any queue jumpers.")
            return False
        else:
            self._tail =(self._tail+1)%self._maxSize
            self._queue.append(data)
            return self._queue
    def dequeue(self):#no need extra data, we will dequeue from the current list
        if self.size() ==0:
            print("there is nothing to dequeue byebyebye byebyeybyeyey")
        else:
            headValue =self._queue[self._head]
            self._queue[self._head]=None
            self._head=(self._head+1)%self._maxSize
            return headValue

def Reverse(Q,S):
    while(not Q.Empty()):
        S.push(Q.dequeuue


if __name__=="__main__":
    a = int(input("Enter the maximum size of the queue: "))
    objCir = CircularQ(a)
    print(objCir.enqueue(1))
    print(objCir.enqueue(2))
    print(objCir.enqueue(3))
    print(objCir.dequeue())
