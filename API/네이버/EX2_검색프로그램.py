# Documents 파이썬 코드를 복사 해오기
import os
import sys
import urllib.request
import json
import re
import urllib.request

 # 네이버 검색 API 이용한 JSON 가공 프로그램
     # JSON : 키-값 => 한쌍   <--- 딕셔너리와 유사

# 네이버검색 함수
def 네이버검색( 카테고리 , 검색결과수 ) :
    client_id = "yw2GbcNlmHEif8TrASs3"
    client_secret = "4PCp9m22Ju"
    url = "https://openapi.naver.com/v1/search/" + 카테고리 + ".json"
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

    검색결과 = response_body.decode('uft-8') # uft-8 : 한글지원
    # 검색결과 가공하기ㅇ
    json결과 = json.loads(검색결과)
    for i in json결과['items'] :
            타이틀 = re.sub('<.+?>', '', i['title'], 0, re.I | re.S)
            print(타이틀)


# 프로그램 코드
while True : # 무한반복하기 : 0번을 입력하면 종료 된다
    print("검색[naverAPI] 프로그램")
    print("카테고리[ 1.뉴스 2.쇼핑 3.도서 4.영화 5.사전 ] 0.종료")
    선택 = int( input("선택 : ") ) # 입력받아 선택변수에 저장
    # 선택 제어
    if 선택 == 1 :
        카테고리 = "news"
        검색결과수 = input(" 뉴스 선택 했습니다. 몇개 출력할까요? ")
        네이버검색(카테고리, 검색결과수) # 함수불러내기
    if 선택 == 2 :
        카테고리 = "shop"
        검색결과수 = input("--> 쇼핑 선택 했습니다. 몇개 출력할까요?")
        네이버검색(카테고리, 검색결과수)  # 함수불러내기
    if 선택 == 3 :
        카테고리 = "book"
        검색결과수 = input("--> 책 선택 했습니다. 몇개 출력할까요?")
        네이버검색(카테고리, 검색결과수)  # 함수불러내기
    if 선택 == 4 :
        카테고리 = "movie"
        검색결과수 = input("--> 영화 선택 했습니다. 몇개 출력할까요?")
        네이버검색(카테고리, 검색결과수)  # 함수불러내기
    if 선택 == 5 :
        카테고리 = "encyc"
        검색결과수 = input("--> 사전 선택 했습니다. 몇개 출력할까요?")
        네이버검색(카테고리, 검색결과수)  # 함수불러내기
    if 선택 == 0 :
        print("--> 이용해주셔서 감사합니다.")
        break # 반복문 종료 : while문 탈출