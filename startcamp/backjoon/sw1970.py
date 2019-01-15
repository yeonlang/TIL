def my_func(lst,n):
    money=(50000,10000,5000,1000,500,100,50,10)
    for i,j in enumerate(money):
        if n//j:
            lst[i]=str(n//j)
            n=n%j
for tc in range(int(input())):
    lst1=['0','0','0','0','0','0','0','0']
    n=int(input())
    my_func(lst1,n)
    print(f'#{tc+1}\n{" ".join(lst1)}') 

