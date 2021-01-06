class Node:
    def __init__(self,data=None):
        self._dataval=data
        self._nextadd=None
        
class SingleLList:
    def __init__(self):
        self._head =None

    def insertBeginning(self,data):
        objNode=Node(data)
        objNode._nextadd =self._head
        self._head= objNode
    
    def printList(self):
        init = self._head
        while init is not None:
            print(init._dataval)
            init = init._nextadd
    
    def appendData(self,value):
        objNode=Node(value)
        if self._head is None:
            self._head= objNode
        else:
            init = self._head
            while init._nextadd:
                init = init._nextadd
            init._nextadd =objNode#newly created object
           # objNode._nextadd = self._head
        
    def insertMiddle(self,prenode,value):
        objNode = Node(value)
        if self._head is None:
            self._head = objNode
        else:
            self._head._nextadd = prenode._nextadd
            prenode._nextadd = objNode
                    
    def deletion(self,value):
        a = self._head
        if a is not None:
            if a._dataval ==value:
                self._head = a._nextadd
                a = None
                return
            while (a is not None):
                if a._dataval ==value:
                    break
                prev =self._head
                a = a._nextadd
            prev._nextadd = a._nextadd
            a = None
        


if __name__ == "__main__":
    objSLL = SingleLList()
    objSLL.insertBeginning(12)
    objSLL.insertBeginning(20)
    objSLL.insertBeginning(15)
    objSLL.insertBeginning(22)
    objSLL.insertBeginning(42)
    objSLL.insertBeginning(32)
    objSLL.deletion(12)
    objSLL.printList()
