
# API : 미리 만들어진 코드[ 프로그램 ]
    # 네이버 API

# Documents 파이썬 코드를 복사 해오기
import os
import sys
import urllib.request
import json
import re
client_id = "yw2GbcNlmHEif8TrASs3"
client_secret = "4PCp9m22Ju"

# 직접 입력해서 검색하기
검색어 = input("블로그 검색 : ")
encText = urllib.parse.quote(검색어)
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과

# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

# 책 검색
검색어 = input( " 책 검색 : " )
encText = urllib.parse.quote(검색어)
url = "https://openapi.naver.com/v1/search/book?query=" + encText # json 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    검색결과 = response_body.decode('utf-8') # utf-8 : 한글 지원

    # 검색결과 가공 하기
    json결과 = json.loads(검색결과)

    결과리스트 = [ ]

    for i in json결과['items'] :
        타이틀 = re.sub('<.+?>', '', i['title'], 0, re.I | re.S )
        print( 타이틀 )

else:
    print("Error Code:" + rescode)

# 뉴스 검색
검색어 = input( " 뉴스 검색 : " )
encText = urllib.parse.quote(검색어)
url = "https://openapi.naver.com/v1/search/news?query=" + encText # json 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

