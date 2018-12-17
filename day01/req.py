import requests
import bs4

response = requests.get('http://finance.naver.com/marketindex/').text
soup = bs4.BeautifulSoup(response, 'html.parser')
result = soup.select_one('#exchageList > li.on > a.head.usd > div > span.value').text
print(result)