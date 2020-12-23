#Given a number count the total number of digits in a number

a = int(input("Enter a number: "))
n=a
c=0
while (n>0):
    c=c+1
    n=n//10
print("The number of digits of",a,"=",c)
