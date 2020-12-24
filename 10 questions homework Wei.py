#Question1
def identical_first_name():
	list1=[1,2,3,4,5,6,1]
	if list1[0]==list1[-1]:
		return True

def divisibleby5():
	list1=[1,2,5,10,15,23]
	for i in list1:
		if i%5==0:
			print(i)

def printevenstring():
	x='abcdef'
	y=0
	for i in x:
		if y%2==0:	
			print(i)
		y+=1
#	for i in len(x)/2:
#		print(x[2*i])

def createlist():
	l1=[1,2,3,4,5,6,7]
	l2=[1,2,3,4,5,6,7]
	l3=[]
	for i in l1:
		if i%2==0:
			l3.append(i)
	for i in l2:
		if i%2!=0:
			l3.append(i)
	return l3

def calculation(x,y):
	return x+y, x-y


def recursive(x):
	if x==0:
		return 0
	return recursive(x-1)+x

def userinput():
	i=input()
	x=0
	for j in range(2,int(i)):
		x+=j
	print(x)

def length(x):
	return len(str(x))

def primenumber():
	for i in range(1,3):
		flag=0
		if i>1:
			if i==2:
				print(2)
				continue
			for j in range(2,int(i)):
				if i%j==0:
					flag=1
			if flag==0:
				print(i)
	
'''
#another way
	def prinumber(a,b)
	a=int(input('Please enter a lower range: '))
	b=int(input('Please enter a upper range: '))
	for i in range(a,b+1):
		for j in range(2,i)
			if(i%j==0):
				break
		else:
		  if i>1:
		  	print(i)
'''
	 

if __name__ == "__main__":
#	print(identical_first_name())
#	divisibleby5()
#	printevenstring()
#	print(createlist())
#	print(calculation(2,1))
#	print(recursive(10))
#	userinput()
#  	print(length(1000))
	primenumber()	
	

