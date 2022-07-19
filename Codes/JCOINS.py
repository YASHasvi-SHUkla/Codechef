# cook your dish her
# taking the number of test cases as input
t = int(input())

for i in range(t):
    x,y = input().split()     #  taking 10 and 5 rupees coins as input
    print(int(x)*10+int(y)*5)   #  printing the total money
