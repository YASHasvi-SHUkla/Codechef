# cook your dish here
# taking number of test cases as input

t = int(input())

for i in range(t):
    a,b,x,y = input().split()
    if int(a)*int(b) <= int(x) * int(y):
        print("Yes")
    else:
        print("No")
