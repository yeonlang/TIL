for tc in range(int(input())):
    n=int(input())
	if tc>2164:
        print(n)
    a=int((n**2+n)/2)
    b=n*n
    c=n*(n+1)
    print(f'#{tc+1} {a} {b} {c}')