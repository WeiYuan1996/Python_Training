#Write a recursive function to calculate the sum of numbers from 0 to 10

def recur_sum(sum_all):
	if sum_all <= 1:
		return 1
	else:
		return sum_all + recur_sum(sum_all - 1)


if __name__ == '__main__':
	sum_all = 10
	print("Sum of numbers from 0 to 10: ",recur_sum(sum_all))

