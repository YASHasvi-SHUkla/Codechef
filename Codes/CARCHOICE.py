# cook your dish here

t = int(input())
for i in range(t):

    x1,x2,y1,y2 = input().split()

    p = int(y1)/int(x1)
    q = int(y2)/int(x2)

    if p < q:
        print(-1)
    elif  p == q:
        print(0)
    else:
        print(1)
        
