
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