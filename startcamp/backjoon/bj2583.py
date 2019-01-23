M,N,K = map(int,input().split())
mat=[ [1]*N  for _ in range(M) ]

for t in range(K):
    x1, y1, x2, y2 = map(int,input().split())
    
    for i in range(y1,y2):
        mat[i][x1:x2] = [0]*(x2-x1)
                
size = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]        

for m in range(M):
    for n in range(N):
        if mat[m][n]:
            count = 0
            mat[m][n] = 0
            bfs = [[m,n]]
            
            while bfs:
                lead = bfs.pop(0)
                count+=1
                
                for j in range(4):
                    xx = lead[1] + dx[j]
                    yy = lead[0] + dy[j]
                    if yy >= 0 and yy < M and xx >= 0 and xx < N and mat[yy][xx]:
                        bfs.append([yy,xx])
                        mat[yy][xx]=0
            
            size.append(count)
            

print(len(size))
print(*sorted(size))
