# 3. Given a string, display only those characters which are present at an even index number.

name = "minjaelee"
new_name = " "
for i, v in enumerate(name):
    if i % 2 == 0:
        new_name += name[i]
    else:
        pass
print(new_name)