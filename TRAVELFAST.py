# cook your dish her
# taking the number of test cases as input
t = int(input())

for i in range(t):
    x,y = input().split()    # taking input speed of Bike and Car repsectively 
    x = int(x)
    y= int(y)
    if x<y:
        print("BIKE")
    elif x>y:
        print("CAR")
    else:
        print("SAME")
