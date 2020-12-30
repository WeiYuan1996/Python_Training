class list_stack:
    def __init__(self):
        self._data=[]

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        if len(self._data) == 0:
            return True
        else:
            return False

    def push(self,element):
        self._data.append(element)
    
    def pop(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            return self._data.pop()

    def top(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            return self._data[-1]

    def logic(self, b):
        for i in range(0,len(b)):
            if b[i]=='(':
                self.push(b[i])
            elif b[i]=='{':
                self.push(b[i])
            elif b[i]=='[':
                self.push(b[i])
            elif b[i]==')':
                self.pop()
            elif b[i]=='}':
                self.pop()
            elif b[i]==']':
                self.pop()

        print(self.top())
        if self.is_empty():
            print("Correct")
        else:
            print("Incorrect")





if __name__=="__main__":
    obj_stack = list_stack()
    s = input("Enter the string: ")
    obj_stack.logic(s)



