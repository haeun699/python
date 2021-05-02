
#문제21 : 인덱싱 [ 문자순서] : 0번시작
letters = 'python'
print( letters[0] , letters[2] )

#문제22 : 슬라이싱[ 시작번호 , 끝번호 , 단위 ]
  # 시작번호부터 끝번호 전까지의 문자 출력
license_plate = "24rk 2210"
print( license_plate[4:8] )
print( license_plate[-4: ] )

#문제23 :
string = "홀짝홀짝홀짝"
print( string[ 0 : 6 : 2 ]) # 0부터 6전까지 2단위로 이동 [ 0 2 4 ]

#문제24 :
string = "PYTHON"
print( string[ : : -1] ) # 뒤에서부터 시작

#문제25 : replace( "기존문자" , "새로운문자" ) 교체 함수
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace( "-" , " " ) # -(하이폰)을 공백으로
print(phone_number1)

#문제26
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace( "-" , "" ) # -(하이폰)을 공백으로
print(phone_number1)

#문제27 : split : 분리[분열] 함수
url =  "http://sharebook.kr"
url_split = url.split(".") # .[점] 기준으로 자르기
print(url_split)

#문제28 : 예상 : 오류발생 !! : 이유
lang = 'python'
#lang[0] = 'p' # 이유 : 문자열 일부분 수정불가
print(lang)

#문제29 : replace 교체함수
string = "abcdfe354a32a"
string = string.replace( "a" , "A" )
                        #기존 #새로운
print(string)

#문제30 : 예상 abcd => aBcd 교체된다.


#문제31 : 예상 34
a = "3" #문자 [ " " 안에 있으면 문자 ]
b = "4" #문자
print(a+b) # 문자+문자 [연결된다]

#문제32 : 예상 HiHiHi
print("Hi"*3)

#문제33 :
print('-'*80)

#문제34 :
t1 = 'python'
t2 = 'java'
t3 = t1 +" "+ t2 + " " # 문자끼리 + 로 변경
print( t3 * 4 )        # 문자 반복 + 사용

#문제35 : format : 형식[꾸미기] formatting : %
           # %s : 문자 형식 ,  %d  : 정수형식
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
    # 이름 : 김민수 나이 : 10
print("이름 : %s 나이 : %d" % (name1 , age1 ) )
print("이름 : %s 나이 : %d" % (name2 , age2 ) )

#문제36 : format() 함수 사용
     # {} 안에 들어갈 데이터를 format 함수 안에 넣기
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름 : {} 나이 : {}".format(name1 , age1))
print("이름 : {} 나이 : {}".format(name2 , age2))

#문제37 : f-string : f*문자(변수명)
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print(f"f*이름 : 나이 : {name1} 나이 : {age1}")
print(f"f*이름 : 나이 : {name2} 나이 : {age2}")

#문제38 : 컴마 제거
상장주식수 = "5,969,782,550" # 문자열
컴마제거 = 상장주식수.replace("," , "" ) # 교체 , -> 공백
타입변환 = int(컴마제거) #문자열 -> 숫자열
print(타입변환)

#문제 39 :
분기 = "2020/03(E) (IFRS연결)"
print( 분기[ 0:7] ) # 0 ~ 6 위치 문자 출력

#문제40 : 공백제거 string() 함수 사용시 앞뒤에 공백 저거 함수
date = "       삼성전자             "
공백제거 = date.strip( )
print(공백제거)

#문제41 : upper( ) 함수 : 대문자로 변환 해주는 함수
ticker = "btc_krw"
print( ticker.upper() )

#문제42 : lower() 함수 : 소문자로 변환 해주는 함수
ticker = "btc_krw"
print(ticker.lower() )

#문제43 : capitalize() 함수 : 첫글자만 대문자로 변환 해주는 함수
ticker = "btn_krw"
print(ticker.capitalize() )

#문제44 : endswith() 함수 : 끝나는 문자가 맞는지 확인 함수
file_name = "보고서.xlsx" # 엑셀 파일
print(file_name.endswith("xlsx") ) # 파일에서 "xlsx" 으로 끝나는지 확인
          # 맞으면 true 아니면 false

#문제45 : 문자열에 xlsx 또는 xls 로 끝나는지 확인 함수
file_name = "보고서.xlsx"
print( file_name.endswith( ("xlsx" , "xls" ) ) )

                        # xlsx 혹은 xls 로 끝나는지 확인
#문제46 : startswith() 함수 : 시작하는 문자가 맞는지 확이 ㄴ함수
file_name = "2020_보고서.xlsx"
print( file_name.startswith("2020") )

#문제47 :
a = "heool world"
print(a.split()) # 공백 기준으로 2개로 분리되어 리스트에 저장

#문제48 : _[언더바] -[하이푼]
ticker = "btc_krw"
print( ticker.split("_")) # _기준으로 분리되어 리스트에 저장

#문제49 :
date = "2020-05-01"
print(date.split("-")) # - 기준으로 분리되어 리스트에 저장

#문제50 : strip( ) : 양쪽 공백 제거 # rstrip() : 오른쪽 공백 제거
date = "  039490 "
print( date.rsplit( ) )

