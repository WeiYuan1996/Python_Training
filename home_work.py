#Write the following programs and push to GIT:


#1. Given a list of numbers, return True if first and last number of a list is same


a=[]
for i in range(5):
    n =int(input(f'give number {i}: ')
    a.append(n)

if a[1]==a[-1]:
	return True
# give number 0: 1
# give number 1: 2
# give number 2: 3
# give number 3: 45
# give number 4: 6
# [1, 2, 3, 45, 6]


#2. Given a list of numbers, Iterate it and print only those numbers which are divisible of 5
a = [ 12,23,124124,12312,3123,45,323]
for i in a:
	if a %5=0:
		print(i)
		
   

#3. Given a string, display only those characters which are present at an even index number.
a = 'aksdjflajsdlfj;saldjflsakjdfkl'
for i in range(0,len(a)):
	if i %2 == 0:
	    print(a[i])
	

   

#4. Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list
a= [12,123,24124,15125,12412]
b=[123,244,2412,3123,12,312,312,3,45,1,2512,35]
c= []
for i in a:
	if  i %2==0:
		c.append(i)
for j in b:
	if j%2 !=0:
		c.append(j)
print(c)
   

#5. Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it. And also it must return both addition and subtraction in a single return call

def calculation(a,b):
	return a+b, a-b
   print(caluculation())

#6. Write a recursive function to calculate the sum of numbers from 0 to 10

def rec_plus(a):
    if a ==0:
        return 0
    elif a>0:
        return rec_plus(a-1)+a

if __name__=='__main__':
    print(rec_plus(10))

#7. Assign a different name to function and call it through the new name
a = lambda x: x**2
b = a


print(b(2))
   

#8. Accept number from user and calculate the sum of all number between 1 and given number

#_________anonymouse function  method____________
a= int(input('please givem e your favorite number : '))
b = []
for i in range(1,a+1):
    b.append(i)

c =reduce(lambda x,y: x+y,b)
   

#_________recursive method____________

a= int(input('please givem e your favorite number : '))
def add(a):
    if a ==1:
        return 1
    elif a>1
        return a +add(a-1)



#9. Given a number count the total number of digits in a number
a= int(input('please givem e your favorite number : '))
   

#10.  Display all the prime numbers within a range:

a= int(input('please give me a lower  number : '))
b = int(input('please give me an upper number : '))
for m in range(a,b+1):
    for n in range(2,m):
        if m%n == 0:
            break
    else: 
        print(m)


if __name__=="__main__":

