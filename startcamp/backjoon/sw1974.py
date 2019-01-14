for tc in range(int(input())):
    column=[[] for j in range(9)]
    bools=1
    for i in range(9):
        column[i]=list(map(int,input().split()))
        if len(set(column[i])) != 9 :
            bools=0
    for j in range(0,9,3):
        a=column[j][0:3]+column[j+1][0:3]+column[j+2][0:3]
        b=column[j][3:6]+column[j+1][3:6]+column[j+2][3:6]
        c=column[j][6:9]+column[j+1][6:9]+column[j+2][6:9]
        if len(set(a)) != 9 or len(set(b)) != 9 or len(set(c)) != 9:
            bools=0
    for j in range(9):
        d=column[0][j:j+1]+column[1][j:j+1]+column[2][j:j+1]+column[3][j:j+1]+column[4][j:j+1]+column[5][j:j+1]+column[6][j:j+1]+column[7][j:j+1]+column[8][j:j+1]
        if len(set(d)) != 9 :
            bools=0
    print(f'#{tc+1} {bools}')

