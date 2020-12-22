if __name__ == '__main__':
    terms = int(input("How many terms? "))

# first two terms
    n1 = 0
    n2= 1
    count = 0

    if (terms == 1):
        print(n1)
    else:
        while (terms > count):
            print(n1)
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            count = count + 1
