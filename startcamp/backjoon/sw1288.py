# N값 입력받는다
# N을 인트형으로 하나 저장하고 각 자리수를 분리해서 리스트에 한번 더 저장한다.
# N의 배수를 취해서 똑같은 과정을 거친다 그리고 전의 리스트에 새로운 리스트 항목을 추가한다.
# 
case=int(input())
for i in range(1,case+1):
    n=input()
    num=int(n)
    lst=[]
    num2=0
    count=1
    while True:
        num2=num*count
        lst.extend(list(str(num2)))
        lst=set(lst)
        lst=list(lst)
        lst.sort()
        if len(lst)>9:
            print(f'#{i} {num2}')
            break
        count+=1
