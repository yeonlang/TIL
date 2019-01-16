def slicing(s):
    while True:
        if len(s)<=10:
            print(s)
            break
        else:
            print(s[0:10])
            s=s[10:]

for tc in range(int(input())):
    s=''
    for i in range(int(input())):
        a, b = input().split()
        s=s+a*int(b)
    print(f'#{tc+1}')
    slicing(s)