row, column = map(int,input().split())
maze =  [list(input()) for _ in range(row)]
visit = [[0]*column for _ in range(row)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

# bfs의 시작 시작지점도 경로값에 1 추가
arr = []
arr.append((0,0))
visit[0][0] = 1
while arr:
    a, b = arr.pop(0)
    #row-1,column-1 인덱스는 행렬의 우측 하단 끝, 끝에 도달한다면 실행
    if a == row-1 and b == column-1:
        print(visit[a][b])

    for i in range(4):
        #ax,ay는 다음 방문 위치
        ax = a + dx[i]
        ay = b + dy[i]
        #ax,ay>0즉 행렬의 시작범위를 벗어나면 안된다. ax<=x-1,ay<=y-1 행렬의 끝범위를 벗어나면 안된다. 
        if ax>=0 and ax<row and ay>=0 and ay<column:
            #방문하지 않았던 곳이고 갈수있는 길이라면 이전루트+1 arr에 경로 추가
            if visit[ax][ay]==0 and maze[ax][ay] == 1:
                visit[ax][ay] = visit[a][b] + 1
                arr.append((ax, ay))