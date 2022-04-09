# cook your dish here

t = int(input())

for i in range(t):
    x,y = input().split()
    if int(y)*30 <= int(x):
        print("Yes")
    else:
        print("No")
