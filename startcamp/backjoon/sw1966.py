for tc in range(int(input())):
    n=int(input())
    m=list(map(int,input().split()))
    m.sort()
    print(f'#{tc+1} {" ".join(map(str,m))}')