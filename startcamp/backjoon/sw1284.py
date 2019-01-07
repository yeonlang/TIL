testcase=int(input())
for i in range(1,testcase+1):
    lst1=list(map(int,input().split()))
    p,q,r,s,w = lst1[0], lst1[1], lst1[2], lst1[3], lst1[4] 
    #1리터당 요금 , 기본요금, 기준사용량, 초과요금, 월간사용량
    lst2=[]
    if w>r :
        lst2.append((w-r)*s+q) 
    else :
        lst2.append(q)
    lst2.append(p*w)
    print(f'#{i} {min(lst2)}')