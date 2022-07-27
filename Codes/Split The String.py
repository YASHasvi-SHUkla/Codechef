# cook your dish here
import math
for i in range(int(input())):
    
    x,y = map(int,input().split())
    s = input()
    
    s1 = s.count("1")
    s2 = s.count("0")
    diff = abs(s1 - s2)
    print(math.ceil(diff/y))
