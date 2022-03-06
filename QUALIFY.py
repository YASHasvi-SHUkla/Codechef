# cook your dish her
# taking the number of test cases as input
t = int(input())

for i in range(t):
    x,a,b = input().split()
    if int(a)+int(b) * 2 >= int(x):
        print("Qualify")
    else:
        print("NotQualify")
