for tc in range(int(input())):
    v,l,a,b=0,0,0,0
    for i in range(int(input())):
        mstr=input()
        if len(mstr)>1:
            a,b=map(int,mstr.split())
        else :
            a=0
        if a==1:
            v+=b
            l+=v
        elif a==2:
            if v>=b:
                v-=b
            l+=v
        else :
            l+=v
    print(f'#{tc+1} {l}')