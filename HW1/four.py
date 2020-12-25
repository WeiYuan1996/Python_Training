# 4. Given a two list of numbers create a new list such that
# new list should contain only odd numbers from the first list
# and even numbers from the second list

list1 = [1, 17, 38, 39, 57, 6]
list2 = [27, 31, 35, 40, 50, 5]
new_list = []

for i in list1:
    if i % 2 != 0:
        new_list.append(i)
for j in list2:
    if j % 2 == 0:
        new_list.append(j)
print(new_list)