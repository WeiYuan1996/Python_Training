#Accept a number from user and count the total number of digits in a number

def count_digit(user_input):
	print(len(str(user_input)))


if __name__ == '__main__':
	user_input = int(input("Enter a number: "))
	count_digit(user_input)
