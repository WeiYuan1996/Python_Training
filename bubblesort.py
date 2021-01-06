def bubble_sort(list):
# Swap the elements to arrange in order
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                breakpoint()
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp



def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
# Find the middle point and devide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))

# Merge the sorted halves

def merge(left_half,right_half):

    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
        if len(left_half) == 0:
            res = res + right_half
        else:
            res = res + left_half
        return res

def insertion_sort(InputList):
    for i in range(1, len(InputList)):
        j = i-1
        breakpoint()
        nxt_element = InputList[i]
# Com   pare the current element with next one
    while (InputList[j] > nxt_element) and (j >= 0):
        import pdb; pdb.set_trace() # breakpoint f5aa403f //
        InputList[j+1] = InputList[j]
        j=j-1
    InputList[j+1] = nxt_element

def selection_sort(input_list):
    for idx in range(len(input_list)):
        min_idx = idx
        for j in range( idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
            # Swap the minimum value with the compared value

            input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]


if __name__ == '__main__': 
    list = [19,2,31,45,6,11,121,27]
    bubble_sort(list)
    print(list)
