# 크기별로 리스트를 정렬한다.
# 세트를 만든다.
# 각 값을 키값으로 하고 내용이 0인 딕셔너리를 만든다.
# 첫번째 맥스값을 뒤에서 탐색하여 
# 그 값보다 이전에 있던 나날들을 모두 구매한다.
# 두번째 맥스값보다 이전에 구매되지 않은 날이 있다면 다시 구매한다.
# 이과정을 반복한다.
from collections import Counter 

case=int(input())
for i in range(1,case+1):
    testnum=int(input())
    lst1=list(map(int, input().split()))
    lst2=lst1.sort()

