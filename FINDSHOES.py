#  cook your dish here

t = int(input())

for i in range(t):
    n,m = input().split();
    right = int(n) 
    left = int(m)
    if left  < int(n):     #   if number of left shoes is less than the total friends
        print(right + (right-left))
    else:
        print(right)
