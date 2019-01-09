T = int(input())
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    #최대이동거리, 총 거리, 충전소의수
    lst = list(map(int, input().split()))
    lst1 = [i for i in range(N+1)]
    lst2 = [0 for i in range(N+1)]

    for i in lst:
        lst2[i]+=1
    position=0
    start=1
    count=0
    while position+K<N:
        lst3=lst2[start:position+K+1]
        if not 1 in lst3:
            count=0
            break
        lst3.reverse()
        for i,j in enumerate(lst3):
            if j==1:
                position+=len(lst3)-i
                start=position+1
                lst3.reverse()
                count+=1
                break
    print(f'#{test_case} {count}')    