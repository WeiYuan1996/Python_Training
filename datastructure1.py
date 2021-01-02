class ListStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isEmpty(self):
        if len(self._data) == 0:
            return True
        else:
            return False

    def push(self, element):
        self._data.append(element)

    def pop(self):
        if self.isEmpty():
            raise Empty('Stack is empty''')
        else:
            return self._data.pop()

    def top(self):
        if self.isEmpty():
            raise Empty('Stack is empty')
        else:
            return self._data[-1]

if __name___ == '__main__':