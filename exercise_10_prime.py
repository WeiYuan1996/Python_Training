#Display all the prime numbers within a range


num1 = int(input("Enter a low number: "))
num2 = int(input("Enter a high number: "))


for num in range(num1,num2+1):
	if num > 1:
		for i in range(2,num):
			if (num%i) == 0:
				break
		else:
			print(num)

