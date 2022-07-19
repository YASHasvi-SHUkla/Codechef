# cook your dish here
t = int(input())

for i in range(t):
    c = 0                             #      temporary variable
    length = int(input())
    n = input()

    for j in n:
        if j == '5' or j == '0':     #   just check if 0 or 5 is there if yes it will become a multiple of 5 otherwise will not.
            c = c+1
    if c >0:
        print("Yes")
    else:
        print("No")
