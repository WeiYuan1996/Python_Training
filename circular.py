class circular_q:
    def __init__(self,max_size):
        self._queue=list()
        self._max_size=max_size
        self._head=0
        self._tail=0
    
    def size(self):
        if self._tail>=self._head:
            return self._tail-self._head
        else:
            return self._max_size-(self._head-self._tail)

    def enqueue(self,data):
        if self._max_size-1==self.size():
            print("Queue is full")
            return False
        else:
            self._tail=(self._tail+1)%self._max_size
            self._queue.append(data)
            return self._queue

    def dequeue(self):
        if self.size()==0:
            print("Nothing to dequeue")
        else:
            head_value=self._queue[self._head]
            self._queue[self._head]=None 
            self._head=(self._head+1)%self._max_size  
            return head_value

if __name__=="__main__":
    a=int(input("Enter the maximum size of the list: "))
    obj_cir = circular_q(a)
    print(obj_cir.enqueue(1))
    print(obj_cir.enqueue(10))
    print(obj_cir.enqueue(100))
    print(obj_cir.dequeue())






