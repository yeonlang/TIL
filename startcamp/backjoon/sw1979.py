def find(m_lst,k):
    m_count=0
    my_lst=[-1]
    for i,a in enumerate(m_lst):
        if a == 0:
            my_lst.append(i)
    my_lst.append(len(m_lst))
    for j in range(len(my_lst)):
        if k != my_lst[0]:
            if my_lst[j]-my_lst[j-1]-1 == k:
                m_count+=1 
    return m_count

def array(mat1):
    for i in range(len(mat1)):
        for j in range(len(mat1)):
            if i < j:
                mat1[i][j],mat1[j][i] = mat1[j][i] , mat1[i][j]

test = int(input())
for l in range(1,test+1):   
    N,K = map(int, input().split())
    count=0
    lst1=[]

    for b in range(N):
        lst1.append(list(map(int,input().split())))

    for c in range(N):
        count+=find(lst1[c],K)

    array(lst1)

    for d in range(N):
        count+=find(lst1[d],K)
        
    print(f'#{l} {count}')