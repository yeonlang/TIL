for tc in range(int(input())):
    lst=[list(map(int,input().split())) for i in range(int(input()))]
    lst1=list(zip(*reversed(lst)))
    lst2=list(zip(*reversed(lst1)))
    lst3=list(zip(*reversed(lst2)))
    print(f'#{tc+1}')
    for i in range(len(lst)):
        print(f'{"".join(map(str,lst1[i]))} {"".join(map(str,lst2[i]))} {"".join(map(str,lst3[i]))}')
