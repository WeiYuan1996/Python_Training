def sum_of_all(a):
	print("Number you entered: ",a)
	sum = 0
	for i in range(a):	
		i = i+1
		#print("second i: ",i)
		#print("second a: ",a)
		sum = sum + i
	print("Sum from 1 to ",a , ": ",sum)

if __name__ == '__main__':
	a = int(input("Enter a number: "))
	sum_of_all(a)
	
