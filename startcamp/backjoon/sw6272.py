n=int(input())
lst1=[0,2,4,6,8]
bools=True
for i in range(1,n+1):
    bools=True
    for j in str(i):
        if not int(j) in lst1:
            bools=False
            break
    if bools:
        print(i)                
