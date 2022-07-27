# cook your dish here

for i in range(int(input())):
    n = int(input())
    draken =  input()
    mikey = input()
    
    counter = 0
    
    for i in range(n):
        if draken[i] != mikey[i]:
             counter = counter + 1
             
    if counter % 2 !=0:
        print(0)
    else:
        print(1)
