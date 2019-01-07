testcase=int(input())
for i in range(1,testcase+1):
    n=list(map(int, input().split()))
    print(f'#{i} ',end='')
    if n[2] < n[0]:
        print(n[0]-n[2])
    elif (n[2] >= n[0]) and (n[2] <= n[1]):
        print(0)
    else :
        print(-1)
