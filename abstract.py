#Abstract Base Classes
from abc import ABCMeta,abstractmethod

#whatever you get child class for your base class(which has many abstractmethods)in your child class you have to have 
class Sequence(metaclass=ABCMeta):
    @abstractmethod
    def length(self):
        '''This is the length method'''
    @abstractmethod
    def getItem(self,i):
        '''This is the getItem method'''
    @abstractmethod
    def index(self,value):
        '''This is the index method'''
class ChildSeq(Sequence):
    def __init__(self,list1):
        self._list1 = list1
    def length(self):
        pass
    def getItem(self):
        pass
    def index(self,value):
        if value in self._list1:
            print("Value is presenting in list")
        else:
            print("Value is not presented")

if __name__=='__main__':
    b = [1,2,3,45,6,6,78,7,99]
    objA = ChildSeq(b)
    objA.index(999)
