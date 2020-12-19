import math
import statistics
from functools import reduce


def calculate_area():
    numbers = [2,2312,3124,124,1432,4,23423,4234]
    areas = []
    for r in numbers:
        area=math.pi*r**2
        areas.append(area)
    print(areas)

    list1=[('Delhi',12),('Moscow','5'),('London',7),('Paris','6'),('Rome',9)]
    


if __name__=="__main__":
    #calculate_area()
    #tup=(1,2,3,4)
    #numbers = [2,23    12,3124,124,1432,4,2]
    #print(list(map(lambda r:math.pi*r**2,numbers)))
    #print(list(map(lambda r:math.pi*r**2,tup)))
    #list1=[('Delhi',12),('Moscow',5),('London',7),('Paris',6),('Rome',9)]
    #print(list(map(lambda x:(x[0],int(x[1]**3)),list1)))
    #sorted_list = [123,213123,34,234.2343,234234,2342342523.234234,54353.345345,36436345,234234.52352356,-209999]
    list2=[2,2,3,5]
    
    #a=statistics.mean(sort_list) 
    #a= reduce(lambda x,y:x+y,sorted_list)
    a = reduce(lambda x,y: x+y**2, list2)+list2[0]**2-list2[0]
   

    b = map(lambda x: x**2,list2)
    c = reduce(lambda x,y:x+y,list(b))
    print(a)
    
    print(c)
    #a=lambda x: sum(x)/len(x) 
    #print(a(sorted_list))






