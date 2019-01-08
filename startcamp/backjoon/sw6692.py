case=int(input())
for c in range(1,case+1):
    num=int(input())
    sum=0.0
    for n in range(1,num+1):
        lst1=list(map(float, input().split()))
        print(lst1)
        sum=sum+lst1[0]*lst1[1]            
    print(f'#{c} {sum}')