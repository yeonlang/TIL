z=0
while z<10:
    a=input()
    b=list(map(int,input().split()))
    c=len(b)
    i=2
    k=0
    while i<c-2:
        d=b[i-2:i+3]
        if max(d)==b[i]:
            y=d.pop(2)
            k=k+y-max(d)
        i=i+1
    print("#%d %d"%(z+1,k))
    z=z+1