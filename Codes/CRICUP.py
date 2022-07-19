# cook your dish here

t = int(input())
for i in range(t):
    x,y,d = input().split()
    if abs(int(x) - int(y)) <= int(d):
        print("Yes")
    else:
        print("No")
