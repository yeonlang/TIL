def subset(A, index=0, count=0,k=0 ):
    if index == len(A):
        if sum(A)==k:
            count+=1
        return count
    B=A[:] #index를 증가시켜 다음 탐색할 리스트
    A.pop(index)
    C=A[:] #원소 하나를 pop한 후 다음 index를 탐색    
    return subset(B, index + 1,count,k) + subset(C, index,count,k)
        


test=int(input())
for tc in range(1,test+1):
    n,k=map(int,input().split())
    myinput=list(filter(lambda x : int(x)<=k ,input().split()))
    lst=list(map(lambda x : int(x), myinput))
    count=0
    	
    print(f'#{tc} {subset(lst,0,0,k)}')


