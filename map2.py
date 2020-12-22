from functools import reduce
import math
import statistics


if __name__=="__main__":

    list1=[2,3,4,56,6,7,7,8,8,9]
   
    a= list(map(lambda x: x**2,list1))
    b=  reduce(lambda x,y:x+y,list1)
    c = b/len(list1)
    #print(b)
    #print(c)
    #d = list(map(lambda x:list1[a.index(x)] if (x < c),a))
    #inside map cant take external variables
    print(a)
    print(c)
    e= list(filter(lambda x:  x<c,a))
    print(e)

