#    if a<=1:
#        return (a,0)
#    else:
#        (a,b)=simple_fibo(a-1)
#        return(a+b,a)

#Binary Search:
a = []
for i in range(1,10):
    a.append(i)


b = int(input('input a number: '))
c=a


def bin(a,b):
    # upper_point = a[-1]
    # lower_pint= a[0]
    mid_point = a[(len(a)//2)]
    if mid_point == b:
        print(c.index(b))
    elif b < mid_point:
        a = a[0:len(a)//2-1]
        return bin(a,b)

    elif b > mid_point:
        a = a[len(a)//2+1:-1]
        return bin(a,b)



print(a,b)
bin(a,b)









    
