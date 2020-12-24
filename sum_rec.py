#WAP to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0)

def sum1(n):
    if (n<=1):
        return n
    else:
        return n + sum1(n-2)

if __name__ == '__main__':
    a=int(input("Enter the number: "))
    print("Sum of all the positive even numbers up to ",a, " is: ",sum1(a))
