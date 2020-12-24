#Write a function calculation() such that it can accept 2 variables and calculate the addition and subtraction of it. And also it must return both addition and subtractionin sigle return call


def calculation(num1,num2):
	add_num = num1 + num2
	sub_num = num1 - num2
	print("Addition of ",num1," and ",num2,"is: ",add_num,"\nSubtraction of ",num1,"and ",num2,"is :",sub_num)


if __name__ == '__main__':
	num1 = int(input("Enter a number: "))
	num2 = int(input("Enter a number: "))
	calculation(num1,num2)
	
