def binary(l,h,x,a):
        m=(l+h)//2
        if a[m]==x:
            return m
        elif x<a[m]:
            return binary(l,m,x,a)
        else:
            return binary(m,h,x,a)

if __name__ == '__main__':
    a=[1,2,3,4,5,6,7,8,9,10,11]
    r=binary(0,len(a)-1,8,a)
    print(r)
