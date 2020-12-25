# 1. Given a list of numbers, return True if first and last number of a list is same

list1 = [2, 17, 38, 39, 57, 6, 2]

def same_start_end(lis):
    if lis[0] != lis[-1]:
        return False
    return True

print(same_start_end(list1))