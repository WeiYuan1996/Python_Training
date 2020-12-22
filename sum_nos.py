def check_even (c): 
    try:
       
        b = c % 2
        if (b == 0):
            print("This is an even number")
        else:
            print("It is an odd number")
    except:
        print("This is an invalid input")

def give_loop(a):
    i=0
    while i<10:
        print(a)
        i=i+1

def check_loop(a):
    for i in range(0,a):
        if i%2==0:
            print(i)

def check_string(a):
    for letter in a:
        print(letter)

def sum(a):
    s=0
    for i in range(1,a+1):
        s = s+i
    print(s)
#Python file

if __name__ == '__main__':
    m = int(input("Enter a number of your choice: "))
    #check_even (a)
    #give_loop(a)
    #check_loop(a)
    #check_string(m)
    sum(m)


