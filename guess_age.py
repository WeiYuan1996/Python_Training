def calculate_year(birth_year):
	age = 2020 - birth_year
	print(f'You are {age} years old')



if __name__ == '__main__':
	birth_year = int(input("Enter your birth year: "))
	calculate_year(birth_year)
