# cook your dish here
# taking input the number of test cases
t= int(input())

for i in range(t):
    a,b = input().split()
    num =    21-(int(a)+int(b))
    if num > 10:
        print(-1)
    else:
        print(num)
