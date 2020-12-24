#Given two lists of numbers, create a new list such that new list should contain only odd numbers from the first list and even numbers from second list

list1 = [3,28,2,11,10,29,22,80,78,83,85,87]
list2 = [1,6,5,11,13,19,4,10,22,4]

#odd numbers from list1
print("Numbers in first list: ",list1)
odd_list = []
for i in list1:
	if i%2 != 0:
		odd_list.append(i)
	
print("Odd numbers from list 1: ",odd_list)


#even number from list2
print("\nNumbers in second list: ",list2)
even_list = []
for i in list2:
	if i%2 == 0:
		even_list.append(i)

print("Even numbers from list2: ",even_list)
