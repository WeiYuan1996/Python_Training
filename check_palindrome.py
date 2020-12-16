def check_palindrome(str):
	str2 = ""
	for letter in str:
		str2 = letter + str2
	if (str == str2):
		print("It's Palindrome",str)
	else:
		print("It's not Palindrome",str)

if __name__ == '__main__':
	str = input("Enter a word: ")
	check_palindrome(str)
