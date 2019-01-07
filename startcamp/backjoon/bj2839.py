t=int(input())
n=5000

a = set([(3*i)+(5*j) for i in range((n//3)+1) for j in range((n//5)+1)])

if (t in a):
    five=t//5
    three=0
    if t % 5 == 1:
        three+=2 
        five=five-1
    if t % 5 == 2:
        three+=4
        five=five-2    
    if t % 5 == 3:
        three+=1 
    if t % 5 == 4:
        three+=3 
        five=five-1
    print(f'{three+five}')
else :
    print(-1)
    