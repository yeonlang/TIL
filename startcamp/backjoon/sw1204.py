from collections import Counter 

case=int(input())
for i in range(1,case+1):
    testnum=int(input())
    test=list(map(int, input().split()))
    
    cnt = Counter(test)
    num=cnt.most_common()
    max_num=int(num[0][0])

    for j in range(len(num)):
        if num[j][1]==num[j+1][1] :
            max_num=max([num[j][0],num[j+1][0]])
        else :
            break
    print(f'#{testnum} {max_num}')
    