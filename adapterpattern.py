class ListStack:
    def __init__(self):
        self._data=[]
    
    def __len__(self):
        return len(self._data)

    def isEmpty(self):
        if len(self._data)==0:
            return True
        else:
            return False
    
    def push(self,element):
        self._data.append(element)
        
    def pop(self):
        if self.isEmpty():
            raise Empty('Stack is empty')
        else:
            return self._data.pop()
    
    def top(self):
        if self.isEmpty():
            raise Empty('Stack is empty')
        else:
            return self._data[-1]

    def getSelf(self):
        return self._data

if __name__ =="__main__":
    a = ListStack()
    p = input('please input a string you like with brackets "(){}[]": ')
    for i in p:
        if i in ['(','{','[']:
            a.push(i)
    print(a.getSelf())

    for i in p:
        if i in [')','}',']']:
            if a.top() =='(':
                a.pop()
            elif a.top() =='{':
                a.pop()
            elif a.top()=='[':
                a.pop()

    print(a.getSelf())
    if a.isEmpty():
        print('Correct')
    else:
        print('Incorrect')



