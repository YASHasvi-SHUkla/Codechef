# cook your dish here
for i in range(int(input())):
    
    x,y,z = map(int,input().split())
    
    if x<=3:
        print(x*y)
    else:
        a = x%3
        if a ==0:
            print((((x//3)-1)*z) + (x*y))
        else:
            print(((x//3) * z ) + (x*y))
