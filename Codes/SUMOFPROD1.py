def yash(arr, n):
	
	ans = 0
	res = 0

	i = n - 1
	while(i >= 0):
		incr = arr[i] * (1 + res)

		ans += incr

		res = incr
		i -= 1

	print(ans)


for i in range(int(input())):
    n = int(input())
    ls = list(map(int,input().split()))
    
    yash(ls,n)
