

# 정보수집_크롤링 패키지
    # 1. Ex1.py

# 크롤링 : 인터넷에서 데이터 추출하기
    # 인터넷문서 => 웹문서 => html ( 하이퍼텍스트 마크업 언어 )

# 1. BeautifulSoup  , bs 설치

from bs4 import BeautifulSoup as bs # html 파일 읽는 메소드 제공 => read()
import urllib.request as ur # 파이썬에 html 가져오기 => urlopen

url = 'http://quotes.toscrape.com/' # 1. 인터넷 주소 넣기
html = ur.urlopen( url ) # 2. 해당(url) 인터넷을 파이썬에서 열기해서 html 변수에 저장

soup = bs( html.read() , 'html.parser') # 3. read() : 인터넷을 읽어오기

print( soup.find_all('span')[0].text ) # 4. 읽어온파일중 찾기 ('span') 찾아서 텍스트 가져오기
#   마크업언어[html] 에서 <span> 태그를 찾어서 태그 사이에 있는 텍스트 가져오기

# find_all() : 찾는값 모두 가져오기
print( soup.find_all('span')[2].text)

# find_all() : 찾는값 모두 가져오기
print( soup.find_all('span')[4].text)

# 모든 span 출력
for i in soup.find_all( 'span' ) :
    print( i.text )

# div 태그에 포함된 해당 클래스만 찾기
for i in soup.find_all( 'div' , {"class" : "quote"} ) :
    print( i.text )
    # 아니면 출력x
