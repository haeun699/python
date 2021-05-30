from bs4 import BeautifulSoup as bs
import urllib.request as ur

# 현재 금 가격 크롤링

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EA%B8%88+%EA%B0%80%EA%B2%A9'
html = ur.urlopen(url)
soup = bs(html.read() , 'html.parser')
가격 = soup.find_all('em' , {"class":"down _now_value"})
print(가격[0].text)