def plus(N):
    mysum=0
    for i in range(1,N+1):
        if i%2:
            mysum+=i
        else :
            mysum-=i
    return mysum
 
for tc in range(int(input())):
    N=int(input())
    print(f'#{tc+1} {plus(N)}')