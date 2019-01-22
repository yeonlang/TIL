from itertools import combinations
while True:
    n, *s = map(int, input().split())
    if not n:
        break
    for i in combinations(s,6):
        u=set(i)
        i=list(u)
        i.sort()
        print(i)