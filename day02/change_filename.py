import os

os.chdir(r'C:\Users\student\daehyun\day02\dummy')
#print(os.getcwd())
#for filename in os.listdir('.'):
 #   os.rename(filename, f'지원자_{filename}')
# 합격자_0_누구누구.txt
for filename in os.listdir('.'):
    rename = filename.replace('지원자_지원자_','')
    os.rename(filename, rename)