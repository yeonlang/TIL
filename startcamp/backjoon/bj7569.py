M,N,H=map(int,input().split())

mat=[ [] for _ in range(H)]
q=[]
count=0
bools=0

direct=[(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]

for h in range(H):
    for n in range(N):
        lst=list(map(int,input().split()))
        mat[h].append(lst)
        for m,val in enumerate(lst):                    
            if val == 1:
                q.append([h,n,m])
            if val == 0 :
                bools+=1

while q:
    m,n,h = q.pop(0)
     
    for d in direct:
        dm = m + d[0]
        dn = n + d[1]
        dh = h + d[2]
        if dm < 0 or dn <0 or dh<0 or dm >= H or dn >= N or dh >= M:
            continue
        if mat[dm][dn][dh] == 0:
            mat[dm][dn][dh] = mat[m][n][h] + 1
            count=max(count,mat[dm][dn][dh])
            q.append((dm, dn, dh))
            bools-=1

if not bools:
    print(count-1)
else:
    print(-1)


