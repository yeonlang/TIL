'''
문제 4.
표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
국어는 90점 이상,
영어는 80점 초과,
수학은 85점 초과, 
과학은 80점 이상일 때 합격이라고 정했습니다.(한 과목이라도 조건에 만족하지 않으면 불합격)
다음 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되도록 작성하시오. 
'''

a = int(input('국어: '))
b = int(input('영어: '))
c = int(input('수학: '))
d = int(input('과학: '))

print(a>=90 or b >80 or c > 85 or d>= 80)
# 아래와 같이도 구현이 가능 (딕셔너리의 사용에 집중)
# score = {'국어' : a , '영어' : b ,'수학' : c ,'과학' : d}
# test = {'국어' : 89 , '영어' : 80 , '수학' : 85 , '과학' : 79 }
# n=0
# for i in score.keys() :
#     if score[i] >= test[i] :
#         n=n+1
# if n==3 :
#     print("True")        
# else :
#     print("False")


# print(score.values())