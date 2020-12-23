#Given a list of numbers, return true if first and last number of list is same

def first_last():
	list1 = [1,2,3,4,5,6,1,15,45,65,1]
	print("Given list is: ",list1)
	if list1[0] == list1[-1]:
		print("True, first and last number of list is same")
	else:
		print("First and last number of list is not same")



if __name__ == '__main__':
	first_last() 
