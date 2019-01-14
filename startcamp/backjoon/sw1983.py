for tc in range(int(input())):
    n,k=map(int,input().split())
    lst=[]
    for i in range(1,n+1):
        s1,s2,s3=map(int,input().split())
        score=s1*35+s2*45+s3*20
        lst.append([i,score])
    lst.sort()
