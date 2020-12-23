#Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list

list1=[1,2,3,4,5,6]
list2=[7,8,9,10,11,12]
result=[]
for i in list1:
    if i%2!=0:
        result.append(i)

for j in list2:
    if j%2==0:
        result.append(j)
print(result)
        
