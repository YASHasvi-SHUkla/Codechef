for i in range(int(input())):

    n = int(input())
    s = input()
    e = ""
    o = ""

    for j in range(n):
        if j%2 == 0:
            e = e+ s[j]
        else:
            o = o + s[j]

    if list(sorted(e)) == list(sorted(o)):
        print("YES")
    else:
        print("NO")
