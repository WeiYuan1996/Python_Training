if __name__ == '__main__':
	num = int(input("Enter a number: "))
	squ_num = lambda x: x ** 2	
	print("Square of ",num, ": %s"%squ_num(num))
	cube_num = lambda y: y * y * y
	print("Cube of ",num, ": %s"%cube_num(num))
        print("Python Program")
