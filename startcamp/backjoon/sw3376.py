for tc in range(int(input())):
    n=int(input())
    a=[1,1,1,2,2]
    if n>5:
        for i in range(n-5):
            a.append(a[i]+a[-1])
    print(f'#{tc+1} {a[n-1]}')
    a=[1,1,1,2,2]