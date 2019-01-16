for tc in range(int(input())):
    str1=set(input())
    str2=tuple(input())
    result=[]
    for i in str1:
        result.append(str2.count(i))
    print(f'#{tc+1} {max(result)}')