def mycount(start,over,c=0,count=0,b=0,newcount=0):
    for j in 'croak':
        if j in start:
            newcount+=1    
    for i in 'croak':
        if not newcount==5:
            return
        c=over.index(i,c) 
        over[over.index(i,c)]='-'
        # start[start.index(i,)]='-'

    over.reverse()
    a=over.index('-')
    over.reverse()
    b=len(over)-a
    
    if newcount==5:
        mycount(over[b:],over,c,count,b)
        
num=int(input())
for w in range(1,num+1):
    st=list(input())
    count2=True
    for r in st:
        if not r in 'croak':
            count2=False           
    if (st[0]=='c')and(st[-1]=='k')and(len(st)%5==0)and(count2):
        count=0
        over=st[:]
        while len(set(over))>1:
            mycount(st,over)
            while '-' in over:
                del over[over.index('-')]
            count+=1
    if count==0:
        print(f'#{w} {count-1}')
    else:
        print(f'#{w} {count}')