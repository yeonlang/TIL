for tc in range(int(input())):
    lst=list(map(int,input().split()))
    time=lst[0]+lst[2]+(lst[1]+lst[3])//60
    if (time%12==0) and (time//12):
        time=12
    else:
        time=time%12
    minute=(lst[1]+lst[3])%60
    print(f'#{tc+1} {time} {minute}')