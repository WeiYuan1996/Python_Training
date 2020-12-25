# 7. Assign a different name to function and call it through the new name

def displayName(name):
    print(name)

displayName("minjae")

showName = displayName
showName("minjae")

print(displayName("tony"))
