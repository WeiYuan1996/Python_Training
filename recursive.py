def factorial(a):
	if a == 0:
		return 1
	else:
		return a*factorial(a-1)

	
if __name__ == '__main__':
	a = int(input("Enter a number to get a factorial: "))
	print(factorial(a))

	s=1
	a=1
	b=0
	for i in range(10):
		print(s)
		s=a+b
		b=a
		a=s
	





