

testcase=int(input())
for w in range(1,testcase+1):
    print(f'#{w}')
    n=int(input())
    a=[[0]*u for u in range(1,n+1)]
    a[0][0]=1
    for j,i in enumerate(a):
        for k,l in enumerate(a):
            if k==(len(i)-1):
                a[j][k]=1
                break
            if k==0:
                a[j][k]=1
            else:
                if (j>0)and(k<len(i)):
                    a[j][k]+=a[j-1][k-1]
                    a[j][k]+=a[j-1][k]
    for j in a:
        for k in j:
            
            print(f'{k} ',end='')
        print('')    