# 8. Accept number from user and calculate the sum of all number between 1 and given number

user_input = int(input("input number: "))
all_sum = 0
for i in range(user_input + 1):
    all_sum += i
print(all_sum)
