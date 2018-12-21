import requests
chat_id = '758344425'
token = '706338901:AAE5akaE7mRuQcHXUQmHZbmqAvSbqTrWHyY'
text = 'stop'
#하고싶은것들

requests.get('https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}?text=오늘의식단')

