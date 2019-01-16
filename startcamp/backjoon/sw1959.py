for tc in range(int(input())):
    n,m =map(int,input().split())
    lst1=list(map(int, input().split()))
    lst2=list(map(int, input().split()))
    result=[]
    if len(lst1)>len(lst2):
        lst1,lst2=lst2,lst1
    while True:
        result.append(sum(map(lambda x: x[0]*x[1],zip(lst1,lst2))))
        if len(lst1)==len(lst2):
            break
        else:
            lst2.pop(0)
    print(f'#{tc+1} {max(result)}')
    