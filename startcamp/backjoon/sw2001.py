def finder(lst,N,M):
    my_max=0
    my_sum=0
    for i in range(N-M+1):
        for j in range(N-M+1):
            for k in range(M):
                my_sum+=sum(lst[i+k][j:j+M])
            my_max=max(my_max,my_sum)
            my_sum=0
    return my_max

for tc in range(int(input())):
    N,M=map(int,input().split())
    lst=[[] for i in range(N)]
    for u in range(N):
        lst[u]=list(map(int,input().split()))
    print(f'#{tc+1} {finder(lst,N,M)}')