def mycount(start,over,count=0,b=0,newcount=0):
    for i in 'croak':
        if i in start:
            c=start.index(i) 
            over[over.index(i,b+c)]='-'
            start[start.index(i,c)]='-'

            newcount+=1
    if not newcount==5:
        count+=1
        return count
    over.reverse()
    a=over.index('-')
    over.reverse()
    b=len(over)-a
    
    if newcount==5:
        mycount(start[b:],over,count,b)

st=list('crocrakcoarkoackcrrooaakkcroak')
over=st[:]
mycount(st,over)




num=int(input())
for nu in range(1,num+1):
    lsti=list(input())
    lstc=['c','r','o','a','k']
    lstu=[j for i in range(int(len(lsti)/5)) for j in lstc]
    c,r,o,a,k = 0,0,0,0,0
    count=0    
    if (lsti[0]!='c')or(lsti[-1]!='k')or(len(lstu)!=len(lsti)):
        count=-1
        

                
        else :
            count=-1
    if c==r==o==a==k :
        print(count)
    else:
        print(-1)















# T = int(input())
 
# for tc in range(T):
#     n1 = list(input())
#     n=n1[:]
#     lst=['c','r','o','a','k']
#     c,r,o,a,k = 0,0,0,0,0
#     index, count= -1,0
#     while n1:
#         while n:         
#             for j,i in enumerate(lst):
                
#                 if i in n:
#                     # if n.index(i)<=index :
#                     #     count+=1
#                     index=n.index(i)
#                     if i == 'c':
#                         c+=1
#                     if i == 'r':
#                         r+=1
#                     if i == 'o':
#                         o+=1
#                     if i == 'a':
#                         a+=1
#                     if i == 'k':
#                         k+=1
#                         index=n.index(i)
#                     n1.pop(n1.index(i))
#             if index<=n.index('c'):
#                 count+=1        
#             n=n1[n.index('c'):]
            
#     if c == r == o == a ==k:
#         print(count)
#     else :
#         print(-1)
