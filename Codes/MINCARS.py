# cook your dish here

t = int(input())

for i in range(t):
    n = int(input())
    if n%4 == 0:
        print(n//4)
    elif n< 4:
            print("1")
    else:
        print((n//4)+1)
