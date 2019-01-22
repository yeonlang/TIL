N = int(input())
myMap = [list(map(int,input().split())) for i in range(N)]

#플루이드 워샬 알고리즘
for j in range(0, N) :
    for i in range(0, N) :
        for k in range(0, N):
            if myMap[i][j] and myMap[j][k]:
                myMap[i][k]=1

for w in range(N):
    print(" ".join(map(str,myMap[w])))