# cook your dish here
t = int(input())
for i in range(t):
    x = int(input())
    if x*0.1 > 100:
        print(int(x*0.1))
    else:
        print(100)
