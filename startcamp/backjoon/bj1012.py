def b():
    N,M,K = map(int,input().split())
    mat=[ [0]*N  for _ in range(M) ]

    for t in range(K):
        a, b =map(int, input().split())
        mat[b][a]=1

    count=0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]        

    for m in range(M):
        for n in range(N):
            if mat[m][n]:
                mat[m][n] = 0
                bfs = [[m,n]]
                
                while bfs:
                    lead = bfs.pop(0)
                    
                    for j in range(4):
                        xx = lead[1] + dx[j]
                        yy = lead[0] + dy[j]
                        if yy >= 0 and yy < M and xx >= 0 and xx < N and mat[yy][xx]:
                            bfs.append([yy,xx])
                            mat[yy][xx]=0
                
                count+=1
                

    print(count)

for tc in range(int(input())):
    b()