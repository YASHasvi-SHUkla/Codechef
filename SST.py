# cook your dish here

t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    if x*10 > y*5:
        print("First")
    elif  x*10 == y*5:
        print("Any")
    else:
        print("Second")
