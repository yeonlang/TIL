'''
문제 3.
숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.
'''

number = int(input('숫자를 입력하세요 : '))
if(number % 2) :
    print(f'{number}는 홀수 입니다.')
else :
    print(f'{number}는 짝수 입니다.')