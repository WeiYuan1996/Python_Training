#WAP to calculate the harmonic sum of n-1 where n is the user input
#Note: The harmonic sum is the sum of reciprocals of the positive integers.
#Example :
#1+1/2+1/3+1/4+....


def harmoic_sum(n):
    if n ==2:
        return 1
    else: 
        return 1/(n-1)+harmoic_sum(n-1)



#WAP of recursion list sum.
#Test Data: [1, 2, [3,4], [5,6]]
#Expected Result: 21
def list_sum(a)
[[1, 2], [3,4], [5,6]]
       a.pop()
       return a[-1][0]+a[-1][1]+list_sum(a)     
        



#WAP to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0)
#Test Data:
#sum_series(6) -> 12
#sum_series(10) -> 30
n + n-2 +n-4 +n-6

n + n-2 + n-4 + n-6+n-8+n-10

n -2*(n-1)
 

def cal_positive(n,a):
    if round(n-2*a)<=0:
        return 0
    else:
        return n-2*a+cal_positive(n,a-1)




if __name__=='__main__':
    n = int(input("enter a number: "))
  
