# cook your dish here

r,o,c = input().split()
left = (20 - int(o))*6*6
if int(c)+left > int(r):
    print("Yes")
else:
    print("No")
