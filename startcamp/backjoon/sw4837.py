def subset(A, *args):
    index = args[0]
    count = args[1]
    k = args[2]
    N = args[3]
    
    if index == len(A):
        if sum(A)==k and len(A)==N:
            count+=1
        return count
    B=A[:] #index를 증가시켜 다음 탐색할 리스트
    A.pop(index)
    C=A[:] #원소 하나를 pop한 후 다음 index를 탐색    
    return subset(B, index + 1, count, k ,N) + subset(C, index, count,k, N)

T = int(input())
A = [1,2,3,4,5,6,7,8,9,10,11,12]

for test_case in range(1, T + 1):
    N, k = map(int, input().split())
    print(f'#{test_case} {subset(A[:],*[0,0,k,N])}')




        