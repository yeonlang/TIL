T = int(input())
 
for tc in range(T):
    n = list(input())
    lst=['c','r','o','a','k']
    c,r,o,a,k = 0,0,0,0,0
    while n:
        for i in lst:
           if i in n:
                n.remove(i)
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
    if c == r == o == a ==k:
        print(c)
    else :
        print(-1)
        

