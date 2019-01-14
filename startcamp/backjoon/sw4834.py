n=input()
m=input()
mydic=dict(zip(m,[0 for i in m]))
for i in m:
    mydic[i]+=1
sorted(mydic.items(), key=lambda x: x[1], reverse=True)

print(mydic[0])