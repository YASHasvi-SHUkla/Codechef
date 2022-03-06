# cook your dish her
# taking the number of test cases as input
t = int(input())

for i in range(t):
    x,y = input().split()    # taking input speed of Bike and Car repsectively      
    if x<y:
        print("BIKE")
    elif x>y:
    i    prnt("CAR")
    else:
        print("SAME")
