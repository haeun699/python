
#1. print() 함수
#   정의 : 코드 출력
#   사용방법 : print("안녕하세요")

#2. type() int() str() float() 함수
#   정의 :
      #type()  :데이터 타입을 확인할 수 있는 함수
      #int()   :숫자나 문자열을 정수형으로 변환
      #str()   :숫자를 문자열로 변환하는 함수
      #float() :숫자나 문자열을 실수형 (Float)으로 변환
#   사용방법 :
      #type()  : a = 128 print( type(a) )
      #int()   : year = "2020" print( int ("2020")) print( int ("2020") +1 ) print( int ("2020") +2 )
      #str()   : num = 100 num_str = str( num ) print(num_str)
      #float() : 문자열 = " 15.79" 실수형 = float( 문자열 ) print(실수형)

#3. 인덱싱 이란
#   정의 : 문자열이나 리스트에 번호를 부여하는것

#4. 슬라이싱
#   정의 :범위를 지정해 선택해서 객체들을 가져오는 방법 및 표기법
#   사용방법: print( int ("2020"))
# print( int ("2020") +1 )
# print( int ("2020") +2 )

#5. replace( ) 함수
#   정의 : 문자열 변경
#   사용방법 : phone_number = "010-1111-2222"
# phone_number1 = phone_number.replace( "-" , " " ) # -(하이폰)을 공백으로
# print(phone_number1)

#6.split() 함수
#   정의 : 문자열을 나누어 주는 함수
#   사용방법 : url =  "http://sharebook.kr"
# url_split = url.split(".") # .[점] 기준으로 자르기
# print(url_split)

#7. %formatting 이란
#문자열에 숫자, 문자열을 대입할 수 있고, %d %f %s 등이 사용된다.

#8.format() 함수
#    정의 :문자열에 숫자, 문자열을 대입할수 있다.
#    사용방법 : 중괄호{}를 사용하는 방법으로, .format() 괄호안에 중괄호에 대입할 문자나 숫자를 입력한다.

#9.f-string
#    정의 : 문자열에서 특정 부분만 바꾸기
#    사용방법: print(f"f*이름 : 나이 : {name1} 나이 : {age1}")
# print(f"f*이름 : 나이 : {name2} 나이 : {age2}")

#10. string() rstrip() lstrip() 함수
#    정의 :
# string() : 앞뒤 공백 제거
# rstring() : 오른쪽 공백제거 함수
# lstring() : 왼쪽 공백제거 함수
#    사용방법 :
#date = "       삼성전자             "
#공백제거 = date.strip( )
#print(공백제거)

#11. upper() lower() capitalize()
#    정의 :
# upper : 대문자로 변환
# lower :  소문자로 변환
# capitalize() : 첫글자를 대문자로 변환
# 사용방법 : a.upper() , a.lower() , a.capitalize()

#12. endswith() startswith() 함수
#    정의:
#endswith() 끝나는 문자가 맞는지 확인 함수
# startswith() 시작하는 문자가 맞는지 확인하는 함수
#    사용방법: a.endswith("문자")
#a.startswith("문자") => 맞으면 Ture, 아니면 False

# 13.  리스트와 변수 차이
# 변수: 저장 공간
#   변수명 = 10
# 리스트: 여러개의 변수를 저장하는 공간
#    리스트 = [변수1, 변수2, 변수3 ...]
#       *리스트는 [] 사용

#14.append() insert() 함수
#    정의: append() 리스트에 변수 추가
#inert() 인덱스 번호에 변수 추가
#    사용방법: 리스트명.append(추가할변수)
#   리스트명.insert(인덱스 번호, 추가할 변수)

#15.del
#    정의: 원하는 인덱스를 삭제
#    사용방법: 리스트명[인덱스번호] => 해당 인덱스 번호가 삭제

#16. max() min() sum() len() 함수
#    정의:
# max() 최대값[리스트내 최댓값을 구한다]
# min() 최솟값[리스트내 최솟값을 구한다]
# sum() 합계[리스트내 모든 숫자를 더한다]
# len() 계수[리스트내 인덱스의 개수를 구한다]
#사용방법:
# max(리스트명)
#min(리스트명)
#sum(리스트명)
#len(리스트명)

#17 . join 함수
     # 정의 : 리스트 내 항목을 합칠때 사용
     # 사용방법 : interest = ['삼성전자','LG전자','Naver','SK하이닉스','미래에셋대우']
                # print(" ".join(interest))

#18 . \n  \t 제어문자
     # 정의 : \n : 줄바꿈 제어문자  # \t : 들여쓰기 제어문자

#19 . 리스트를 오름차순 / 내림차순 방법
# 오름차순 sort()   내림차순 data.sort(reverse=True)

#20 . 데이터를 저장하는 방법 4가지의 차이 와 사용방법
     # 변수 = def 함수이름(매개변수):
     # 리스트 = ['삼성전자', 'LG전자', 'SK Hinix']
     # 튜플 =  ('삼성전자', 'LG전자', 'SK Hinix')
     #딕셔너리 = { 키 : 값 , 키2 : 값2 , 키3 : 값3 }

#21 . 튜플을 리스트로 변환 하는 방법
# print( list (interest))
#22 . 리스트를 튜플로 변환 하는 방법
#print( tuple (interest))

#23 . 튜플 언팩킹 이란
     # 정의 : # 언팩킹[ 묶음x ]
     # 사용방법 : team = ('apple','banana','cake')
                 # a,b,c = team
                 # print(a,b,c)

#24 . 딕셔너리 활용
     # 1. 딕셔너리 리스트 추가하는 방법
      # 딕셔너리명["키"] = 값
     # 2. 딕셔너리의 키 만 출력 하는 방법
      # print(딕셔너리명.keys())
     # 3. 딕셔너리의 값 만 출력 하는 방법
      # 딕셔너리명[ 키 ] => 해당하는 키의 값이 출력 된다
     # 4. 두 개의 딕셔너리를 합치는 방법
      # 딕셔너리명.update(딕셔너리명2) : 딕셔너리명 에 딕셔너리명2 추가
     # 5. [키] 튜플 과 [값] 튜플을 딕셔너리 변환하는 방법
      # dict(zip(튜플명1, 튜플명2))
     # 6. [키]리스트 과 [값] 리스트 을 딕셔너리 변환하는 방법
      # dict(zip(리스트명1, 리스트명2))

