
def calculation(a,b):
    sum1=a+b
    sub1=a-b
    return sum1, sub1
if __name__ == '__main__':
    x = int(input("Enter the 1st number: "))
    y = int(input("Enter the 2nd number: "))
    print(calculation(x,y))
