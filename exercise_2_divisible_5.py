#Given a list of numbers, iterate it and print only those numbers which are divisible of 5


def divisible_by_5():
	list1 = [1,5,7,10,14,20,60,76,85]
	print("Numbers are: ",list1)
	for i in list1:
		if i%5 == 0:
			print(i,"is divisible by 5")


if __name__ == '__main__':
	divisible_by_5()	 
