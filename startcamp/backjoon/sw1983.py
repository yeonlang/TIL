for tc in range(int(input())):
    n,k=map(int,input().split())
    lst=[]
    index_lst=0
    for i in range(1,n+1):
        s1,s2,s3=map(int,input().split())
        score=s1*0.35+s2*0.45+s3*0.20
        lst.append(score)
        if i == k:
            index_lst=score
    lst.sort()
    if lst.index(index_lst)>9*n/10-1:
        print(f'#{tc+1} A+')
    elif lst.index(index_lst)>8*n/10-1:
        print(f'#{tc+1} A0')
    elif lst.index(index_lst)>7*n/10-1:
        print(f'#{tc+1} A-')
    elif lst.index(index_lst)>6*n/10-1:
        print(f'#{tc+1} B+')
    elif lst.index(index_lst)>5*n/10-1:
        print(f'#{tc+1} B0')
    elif lst.index(index_lst)>4*n/10-1:
        print(f'#{tc+1} B-')
    elif lst.index(index_lst)>3*n/10-1:
        print(f'#{tc+1} C+')
    elif lst.index(index_lst)>2*n/10-1:
        print(f'#{tc+1} C0')
    elif lst.index(index_lst)>n/10-1:
        print(f'#{tc+1} C-')
    else:
        print(f'#{tc+1} D0')