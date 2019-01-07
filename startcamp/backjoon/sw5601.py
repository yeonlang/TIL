testcase=int(input())
for i in range(1,testcase+1):
    n=int(input())
    print(f'#{i} ', end='')
    for j in range(1,n+1):
        print(f'1/{n}',end='')
        if j == n :
            print('')
        else :
            print(' ',end='')


