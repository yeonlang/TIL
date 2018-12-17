import webbrowser
kewards = ('날씨', '아이유', '구미맛집')
for k in kewards:
    webbrowser.open('https://search.daum.net/search?w=tot&q='+k)