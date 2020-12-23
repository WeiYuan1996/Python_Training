#Write a recursive function to calculate the sum of numbers from 0 to 10

def rec_sum(a):
    if a==0:
        return 0
    else:
        sum1= a + rec_sum(a-1)
        return sum1
if __name__ == '__main__':
    print(rec_sum(10))
