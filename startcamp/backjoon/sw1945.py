for tc in range(int(input())):
    n=int(input())
    lst=[2,3,5,7,11]
    lst2=[0,0,0,0,0]
    while n!=1:
        if n%2==0 :
            lst2[0]+=1
            n=n//2
            continue
        if n%3==0 :
            lst2[1]+=1
            n=n//3
            continue
        if n%5==0 :
            lst2[2]+=1
            n=n//5
            continue
        if n%7==0 :
            lst2[3]+=1
            n=n//7
            continue
        if n%11==0 :
            lst2[4]+=1
            n=n//11
            continue
    print(f'#{tc+1} {" ".join(map(str,lst2))}')
        