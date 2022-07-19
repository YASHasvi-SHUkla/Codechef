# cook your dish here

t = int(input())
for i in range(t):
    a,b = input().split()
    if int(a)< int(b):
        print("First")
    elif int(a) == int(b):
        print("Any")
    else:
        print("Second")
