# lunch = {
#     '중국집' : '02-316-5554' ,
#     '양식집' : '054-563-1331' ,
#     '한식집' : '053-525-4379' ,
# }
# print(lunch)

# # 1. 딕셔너리 내용 생성
# dinner = dict(중국집='02-123-123')

# # 2. 딕셔너리에 내용 추가하기
# lunch['분식집'] = '053-123-123'

# # 3. 딕셔너리 내용 가져오기
# print(lunch['중국집']) #=> '02-316-5554'

# # 4. 딕셔너리 반복문 활용하기
# for key in lunch:
#     print(key,end=' ')
#     print(lunch[key])

# idol = {
#     'bts' : 
#      {
#         '지민' : 24,
#         'RM' : 25,
#     }
# }
# idol['bts'] #=> { '지민' : 24, 'RM', 25}
# idol['bts']['RM'] #=> 25

# # key 만 가져오기
# for key in lunch.keys():
#     print(key)

# # value만 가져오기 : .values()
# for value in lunch.values() :
#     print (value)

# # item(key, value) 가져오기 : .items()
# # lunch.items) #=> [('중식','02'), ... ]
# for item in lunch.items()
#     print(item[0], item[1])

# # item을 분리해서 가져오기
# for key, value in lunch.items()
#     print(key, value)

# # 2개 = 자료형(list, tuple, ...) 길이 2
# a , b , c = (1,2,3)
# print(a)
# print(b)    

scores = {
    'a' : {  
        '수학' : 80,
        '국어' : 90,
        '음악' : 70,
        },
    'b' : {  
        '수학' : 80,
        '국어' : 90,
        '음악' : 100,
        }
}

total_score = 0
count = 0

for person_score in scores.values() : #=> [{ '수학' : 80, '국어' : 90, '음악' : 70} ,{'수학' : 80,'국어' : 90,'음악' : 100}]
    # person_score #=> { '수학' : 80, '국어' : 90, '음악' : 70}
    # person_score.values() #=>  [80, 90, 70]
    for subject_score in person_score.values():
        # 1번째 시행 일때
        # subject_score #=> 80
        total_score += subject_score
        count += 1   
print(total_score/count)
    
# 문제 1 평균 구하기
score = {
    '수학' : 80,
    '국어' : 90,
    '음악' : 100,
}

# #풀이 1
# add=0
# num=0

# for value in score.values():
#     add = add + value
#     num = num + 1
# print(add/num)

#풀이 2
total_score = sum(score.values()) #=> sum([80,90,100]) = 270
avg_score = total_score / len(score) #=>270 / 3
print(avg_score)

# 문제 2 반 평균을 구하시오
scores = {
    'a' : {  
        '수학' : 80,
        '국어' : 90,
        '음악' : 100,
        },
    'b' : {  
        '수학' : 80,
        '국어' : 90,
        '음악' : 100,
        }
}

num = 0
total = 0

for key in scores :
    for mem in scores[key] :
        total = total + scores[key][mem]
        num = num + 1
print(total/num)    
    
# a_total = sum(scores['a'].values())
# b_total = sum(scores['b'].values())

# print((a_total+b_total)/(len(scores['a'])+len(scores['b'])))

# 문제 3

city = {
    '서울' : [-6,-10,6],
    '대전' : [-3,-6, 2],
    '광주' : [0, -2, 10],
    '구미' : [2, -2, 9],
}
#3-1 도시별 최근 3일의 온도 평균은?
print('각 도시별 최근 3일의 온도 평균은 다음과 같습니다.')
for key in city :
    a = sum(city[key])/len(city[key]) 
    print(f'{key} : {round(a,1)}')       
    city[key] = a
    print(city.values())
# 3-2 가장 더웠던 곳은?


