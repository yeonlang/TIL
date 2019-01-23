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
