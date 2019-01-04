def my_func(a):
    num=int(a)
    if num%2 == 0 :
        return 0
    if num%2 == 1 :
        return num
case = int(input())
for case_num in range(case) :
    lst1=list(map(my_func, input().split()))
    int_sum=0
    for i in lst1 :
        int_sum+=int(i)
    print(f'#{case_num+1} {int_sum}')