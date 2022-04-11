# cook your dish here

t = int(input())
for i in range(t):
    a,b = input().split()
    
    if int(a) > 0 and int(b) > 0:
        print("Solution")
    elif int(b) == 0:
        print("Solid")
    else:
        print("Liquid")
