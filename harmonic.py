#WAP to calculate the harmonic sum of n-1

def har_sum(a):
    if (a==1):
        return a
    else:
        return 1/a + (har_sum(a-1))


if __name__ == '__main__':
    n=int(input("Enter the number: "))
    print(har_sum(n-1))


