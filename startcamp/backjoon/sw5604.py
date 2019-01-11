T = int(input())
for test_case in range(1, T + 1):
    start,end=map(int ,input().split())
    my_sum=0

    for i in range(start,end+1):
        my_sum+=sum(map(int,filter(lambda x : x != '0',str(i))))
             
    print(f'#{test_case} {my_sum}')

