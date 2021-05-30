import os
import sys
import urllib.request
import json
import re
import urllib.request

def 네이버검색( 카테고리 , 검색결과수 ) :
    client_id = "yw2GbcNlmHEif8TrASs3"
    client_secret = "4PCp9m22Ju"
    url = "https://openapi.naver.com/v1/search/"+ 카테고리 + ".json"
    option = "&display="+검색결과수+"&sort=count" # display : 출력 갯수 : 검색결과 수
    query = "?query="+urllib.parse.quote( input( 카테고리+"의 검색 정보 입력 : ") )
    url_query = url + query + option

    request = urllib.request.Request(url_query)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
    else:
        print("Error Code:" + rescode)

    검색결과 = response_body.decode('utf-8') # uft-8 : 한글지원
    # 검색결과 가공하기ㅇ
    json결과 = json.loads(검색결과)
    for i in json결과['items'] :
        타이틀 = re.sub('<.+?>', '', i['title'], 0, re.I | re.S)
        print(타이틀)
        print( "감독 : "  , re.sub('<.+?>', '', i['actor'], 0, re.I | re.S)    )
        print("평점 : "  , re.sub('<.+?>', '', i['userRating'], 0, re.I | re.S))




while True :
    print("검색[naverAPI] 프로그램")
    print( "카테고리[ 1.영화 2.책 3.쇼핑] 0.종료 " )
    선택 = int( input("선택 : "))
    if 선택 == 1 :
        카테고리 = "movie"
        검색결과수 = input("검색 갯수 : ")
        네이버검색( 카테고리 , 검색결과수 )
    if 선택 == 2 :
        카테고리 = "book"
        검색결과수 = input("검색 갯수 : ")
        네이버검색( 카테고리, 검색결과수 )


