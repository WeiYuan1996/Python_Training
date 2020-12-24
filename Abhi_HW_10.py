#Display all the prime numbers within a range
a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
for i in range(a,b):
    prime = True
    for j in range(2,i):
        if (i%j==0):
            prime = False
            break
    if prime==True:
            print(i)

