lunch = {
    '횡성한우':'054-474-1235',
    '영덕대게':'054-485-1841',
    '영광굴비':'054-475-5689'
}
import csv

with open('lunch.csv', 'w' , encoding = 'utf8', newline = '') as f:
    csv_writer =csv.writer(f) #f는 파일 내용
    for item in lunch.items():
        csv_writer.writerow(item)
    # for item in lunch.items(): # 리스트 [(key, value),...]
    #     f.write(f'{item[0]},{item[1]}\n')