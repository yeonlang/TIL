def max_in(lst):
    return str(lst.pop(lst.index(max(lst))))
def min_in(lst):
    return str(lst.pop(lst.index(min(lst))))

T = int(input())
for test_case in range(1, T + 1):
    tc=int(input())
    lst=list(map(int, input().split()))
    result=[]
    while True:
        if (lst)and(len(result)<10):
            result.append(max_in(lst))  
        else :
            break
        if (lst)and(len(result)<10):
            result.append(min_in(lst))
        else :
            break
    print(f'#{test_case} {" ".join(result)}')   