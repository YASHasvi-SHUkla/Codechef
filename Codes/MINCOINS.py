# cook your dish here

t = int(input())

for i in range(t):
    n = int(input())
    a = n%10 
    if a%5 == 0:
        print(n//10 + a//5)
    else:
        print(-1)
