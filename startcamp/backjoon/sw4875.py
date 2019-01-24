def bfs(l,tc):
    N=l
    mat=[]
    stack=[]
    lead=[(1,0),(-1,0),(0,1),(0,-1)]
    count=0

    for i in range(N):
        a=list(map(int,input()))
        mat.append(a)
        if 2 in a :
            stack.append([i,a.index(2)])
            mat[i][a.index(2)]=1
            
    while stack:
        m,n=stack.pop()    
        
        for k in range(4):
            mm,nn=m+lead[k][0],n+lead[k][1]
            
            if mm>=0 and mm<N and nn>=0 and nn<N and mat[mm][nn]!=1:
                if mat[mm][nn]==3:
                    count=1
                stack.append([mm,nn])
                mat[mm][nn]=1

    print(f'#{tc+1} {count}')


for tc in range(int(input())):
    l=int(input())
    bfs(l,tc)    
