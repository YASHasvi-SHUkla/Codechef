# cook your dish here
# taking input the number of test cases
t= int(input())

for i in range(t):
    x1,y1,x2,y2 = input().split()
    print(max(abs(int(x1)-int(x2)),abs(int(y1)-int(y2))))                 # abs() function converts positive to negative and -abs() does vice versa
