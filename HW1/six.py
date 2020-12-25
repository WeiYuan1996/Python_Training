# 6. Write a recursive function to calculate the sum of numbers from 0 to 10

def rec_sum(x):
    if x == 0:
        return 0
    return rec_sum(x-1) + x

print(rec_sum(10))