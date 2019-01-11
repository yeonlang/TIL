def a_find(start,end,page):
    count=1
    while True:
        mid = int((start+end)/2)
        if mid == page:
            return count
        elif mid >page :
            count+=1
            end=mid
        else :
            count+=1
            start=mid


def b_find(start,end,page):
    count=1
    while True:
        mid = int((start+end)/2)
        if mid == page:
            return count
        elif mid >page :
            count+=1
            end=mid
        else :
            count+=1
            start=mid

T = int(input())
for test_case in range(1, T + 1):
    start=1
    end, a_page, b_page=map(int,input().split())


    a=a_find(start,end,a_page)
    b=b_find(start,end,b_page)

    if a>b:
        result='B'
    elif a<b:
        result='A'
    else:
        result='0'
    print(f'#{test_case} {result}')
