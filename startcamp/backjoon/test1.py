from collections import Counter 

case=int(input())
for i in range(1,case+1):
    testnum=int(input())
    test=list(map(int, input().split()))
    
    cnt = Counter(test)
    num=cnt.most_common()
print(num)