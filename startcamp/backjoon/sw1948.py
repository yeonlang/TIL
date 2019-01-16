for tc in range(int(input())):
    month=[0,31,59,90,120,151,181,212,243,273,304,334]
    m1,d1,m2,d2=map(int,input().split())
    start=month[m1-1]+d1
    end=month[m2-1]+d2
    print(f'#{tc+1} {end-start+1}') 