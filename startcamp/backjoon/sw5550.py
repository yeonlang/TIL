T = int(input())
 
for tc in range(T):
    n1 = list(input())
    n=n1[:]
    lst=['c','r','o','a','k']
    c,r,o,a,k = 0,0,0,0,0
    index, count= -1,0
    while n1:
        while n:         
            for j,i in enumerate(lst):
                
                if i in n:
                    # if n.index(i)<=index :
                    #     count+=1
                    index=n.index(i)
                    if i == 'c':
                        c+=1
                    if i == 'r':
                        r+=1
                    if i == 'o':
                        o+=1
                    if i == 'a':
                        a+=1
                    if i == 'k':
                        k+=1
                        index=n.index(i)
                    n1.pop(n1.index(i))
            if index<=n.index('c'):
                count+=1        
            n=n1[n.index('c'):]
            
    if c == r == o == a ==k:
        print(count)
    else :
        print(-1)