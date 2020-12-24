#Accept a number from user and calcualte the sum of all number between 1 and given number

def sum_of_all(sum):
	sum_all = 0
	for i in range(sum):
		i = i+ 1
		sum_all = i + sum_all
	print("Sum of all number between 1 and ", sum, "is: ",sum_all)
	


if __name__ == '__main__':
	user_input = int(input("Enter a number: "))
	sum_of_all(user_input)
