import requests
import bs4

response = requests.get('https://www.naver.com/').text
soup = bs4.BeautifulSoup(response, 'html.parser')
result1 = soup.select('div.PM_CL_realtimeKeyword_list_base span.ah_r')
result2 = soup.select('div.PM_CL_realtimeKeyword_list_base span.ah_k')
i=0
for item in result2 :
    print(f'{result1[i].text} {item.text}')
    i=i+1
     

