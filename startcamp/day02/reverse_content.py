with open('SSAFY.txt','r', encoding='utf8') as f :
    lines = f.readlines()
    for line in lines :
        print(line)

#1.한번에 처리
with open('SSAFY.txt','r', encoding='utf8') as f :
    lines = f.readlines()
    with open('This is SSAFY!','w',encoding='utf8') as ff :
    ff.writelines(reversed(lines))      
    
#2.read/write 분리처리
with open('SSAFY.txt','r', encoding='utf8') as p :
    lines = p.readlines()
    lines.reverse()

with open('This is SSAFY!','w',encoding='utf8') as pp :
    pp.writelines(reversed(lines))        