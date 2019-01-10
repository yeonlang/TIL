tc=int(input())
mat2=[[0]*10 for i in range(0,10)]
count=0
for i in range(1,tc+1):
    x1,y1,x2,y2,color=map(int,input().split())
    
    for i in range(0,10):
        for j in range(0,10):
            if (i>=x1) and (i<=x2) and (j>=y1) and (j<=y2):
                if mat2[i][j] == 0:
                    mat2[i][j] = color
                    continue
                if mat2[i][j] == 1:
                    if color ==2 :
                        mat2[i][j] = 3
                    continue
                if mat2[i][j] == 2:
                    if color ==1 :
                        mat2[i][j] = 3
                    continue
                if mat2[i][j] == 3:
                    continue

for i in range(0,10):
    for j in range(0,10):
        if mat2[i][j] == 3:
            count+=1

print(f'# {count}')