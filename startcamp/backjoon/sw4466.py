testcase=int(input())
for i in range(1,testcase+1):
    lst1=list(map(int,input().split()))
    n, k = lst1[0], lst[1]
    lst2=list(map(int,input().split()))
    lst2.sort()
    sum=0
    for j in lst2[0:k]:
        sum+=j
    print(f'#{i} {sum}')