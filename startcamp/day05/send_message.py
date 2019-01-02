import os
import requests

chat_id = os.getenv('CHAT_ID')
token = os.getenv('TELEGRAM_BOT_TOKEN')

#하고싶은것들

text = 'stop'
requests.get('https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}?text=오늘의식단')

