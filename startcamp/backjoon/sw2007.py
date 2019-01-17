test_case=int(input())
for tc in range(1,test_case+1): 
    lst=input()
    count=0
    bools=False
    for j in range(1,11):
        start=0
        for k in range(len(lst)//j+1):
            if j==len(lst[start+j:start+2*j]):
                if lst[start:start+j]==lst[start+j:start+2*j]:
                    bools=True
                else:    
                    bools=False    
            else:
                break            
            start+=j
        if bools:
            count=j
            break
    print(f'#{tc} {count}')

    [[1,2,3,4,5,6,7,8]
    [1,2,3,4,5,6]
    [1,2,3,4,5,6,7]
    [1,2,3,4,5,6]
    [1,2,3,4,5,6]]
list(zip())
[(1,1,1,1,1,1,),(2,2,2,2,2,2,)]