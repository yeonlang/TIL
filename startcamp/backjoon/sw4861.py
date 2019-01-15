for tc in range(int(input())):
    n,m=map(int, input().split())
    row=[tuple(input()) for i in range(n)]
    column=list(zip(*row))
    bools=True
    for i in range(n):
        if bools:
            for j in range(n-m+1):
                test=row[i][j:m+j]
                if test == test[::-1] :
                    print(f'#{tc+1} {"".join(test)}')
                    bools=False
                    break
        else:
            break
        if bools:
            for k in range(n-m+1):
                test=column[i][k:m+k]
                if test==test[::-1] :
                    print(f'#{tc+1} {"".join(test)}')
                    bools=False
                    break
        else:
            break