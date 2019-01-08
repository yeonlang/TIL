

def output(matr,n):
    count, a, b, c, d=1, 0, 0, 0, 0
    while True:
        for right in range(a,len(matr)-b):
            matr[c][right]=count 
            count+=1
        c+=1
        if count > (n*n):
            return matr
        for down in range(c,len(matr)-d):
            matr[down][len(matr)-b-1]=count            
            count+=1
        b+=1
        if count > (n*n):
            return matr
        for left in range(len(matr)-b-1,a-1,-1):
            matr[len(matr)-d-1][left]=count 
            count+=1
        d+=1   
        if count > (n*n):
            return matr
        for up in range(len(matr)-d-1,c-1,-1):
            matr[up][a]=count 
            count+=1
        a+=1
        if count > (n*n):
            return matr
    
        
        
def column(mymatrix, a1, b1):
    return mymatrix[a1][b1]       


num=int(input())


for t in range(1,num+1):
    print(f'#{t}')
    m=int(input())
    my_Matrix=[[0]*m for c in range(m)]
    matr1=output(my_Matrix,m)

    for z in range(len(my_Matrix)):
        for v in range(len(my_Matrix)):
            print(column(my_Matrix, z, v), end='')
            if v == len(my_Matrix)-1:
                print('')
            else : 
                print(' ',end='')     
