import requests
import bs4

response = requests.get('https://www.naver.com/').text
soup = bs4.BeautifulSoup(response, 'html.parser')
#result = soup.select_one('#KOSPI_now').text
result = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base span.ah_k')
# result = soup.select_one('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-of-type(1)').text
for i in result:
    print(i.text)


#content > div > div.keyword_carousel > div > div > div:nth-child(1) > div > div > ul > li:nth-child(1) > a
##PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child(2) > a.ah_a > span.ah_k
#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child(1)