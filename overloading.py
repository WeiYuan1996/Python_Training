class OverLoad:
    def __init__(self,a):
        self._a=a
    def __add__(self,second):
        return self._a*second._a
    def __len__(self):
        return(len(self._a)**2)

if __name__=='__main__':
    x= int(input("enter numberx: "))

    y= int(input("enter numbery: "))
    z= int(input("enter numbery: "))
    w=input('enter a string:')
    objOver= OverLoad(x)
    objLoad=OverLoad(y)
    objOver2=OverLoad(z)
    objOver3= OverLoad(w)
    result = objOver+objLoad2
    ojOverSum = Overload(result)
    print(ojOverSum+objOver2
    print(objOver+objLoad3)
    print(objOver+objLoad+objOver2)
    print(len(


