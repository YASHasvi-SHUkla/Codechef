# cook your dish here

for i in range(int(input())):
    a,b = map(int,input().split())
    ls = list(range(1,50))
    
    x = [2**i for i in ls]
    x.append(1)
    
    if max(a,b)//min(a,b) in x and max(a,b)%min(a,b) ==0:
        print("YES")
    else:
        print("NO")
