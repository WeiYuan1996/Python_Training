#Given a string, display only those characters which are present at an even index number


def even_index(string1):
	for i in range(len(string1)):
		if i%2 == 0:
			print(string1[i]," is at an even index of the string")



if __name__ == '__main__':
	user_input = input("Enter a string: ")
	even_index(user_input)
