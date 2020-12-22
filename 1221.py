def factorial(num):
    if num == 0:
        return 1
    else:
        return num*factorial(num-1)
    
def fib(n):

    if n<=0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1    
    
    else:
        return fib(n-1)+fib(n-2)




if __name__=='__main__':
    num = int(input('input a number you like: '))
    print(factorial(num))
