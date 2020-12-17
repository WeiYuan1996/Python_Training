
def check_even(a):
	b = a%2
	if (b==0):
		print(a)

def check_forloop(q):
	for i in range(0,q):
		check_even(i)



if __name__ == '__main__':
	#try:
	#	a = int(input("Enter a number of your choice: "))
	#	check_even(a)
	#except:
	#	print("This is an invalid input")
	q = int(input("Enter a number: "))
	check_forloop(q)


