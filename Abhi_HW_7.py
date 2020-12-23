def show_salary(emp,sal):
    return emp, sal


if __name__ == '__main__':
    e = input("Enter the employee's name: ")
    s = int(input("Enter his/her salary: "))
    show_salary(e,s)
    display_salary = show_salary
    print(display_salary(e,s))

