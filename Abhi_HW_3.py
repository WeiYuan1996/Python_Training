#Given a string, display only those characters which are present at an even index number

a=input("Enter the string: ")
for i in range(len(a)):
    if i%2==0:
        print(a[i])
