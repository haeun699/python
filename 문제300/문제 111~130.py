
     # 논리 : 맞는지 틀린지 판단
     # 연산자 :
         # 산술연산자 :  + 더하기 - 빼기 * 곱하기 / 나누기 // 나누기[몫] % 나누기[나머지]
         # 비교연산자 : > 초과 < 미만 >=이상 <=이하 ==같다 !=같지않다
         # 논리연산자 : and [이면서] or [이거나] ![부정]
         # 대입연산자 : += [ 오른쪽값을 왼쪽값에 더하기후 왼쪽값에 대입 ]
                #     -= [ 오른쪽값을 왼쪽값에 빼기 후 왼쪽값에 대입 ]
                #     *= /=  %= 등

     # IF : 논리문
     #     if 논리 :
     #         참 [ 코드 ]
     #     else :
     #         거짓 [ 코드 ]

                 # if 논리 :
                 #    if 논리  :
                 #        참 [코드]
                 #    else     :
                 #        거짓 [코드]
                 # else:
                 #     if 논리 :
                 #         참 [코드]
                 #     else :
                 #          거짓 [코드]

# 101 :
print(type(True) )  # bool : 참[True] 거짓[False] 둘 중 하나 저장하는 타입
print(type(False) )  # bool : 참[True] 거짓[False] 둘
     # 중 하나 저장하는 타입

# 102 :
print( 3==5 ) #  3 과 5은 다르다 False

# 103 :
print( 3 < 5 ) # 3은 5 보다 미만인가? True

# 104 :
x = 4
print( 1 < x < 5 ) # x은 1보다 초과 이고 5보다 미만인가? True

# 105 :
print( ( 3==3 ) and (4 != 3) ) # 3과 3은 같다 이면서 4와 3은 같지않은가? True
         # true 이면서 true = true
         # true 이면서 false = false

# 106 :
# print ( 3 => 4 ) 오류발생 이유 : 같거나 초과 기호는 없음 // 초과나 같다 >= [ 이상 ]

# 107 :
if 4 < 3 : # false
    print( "Hello world" ) # True 아니기기때문에 출력되지 않음

# 108 :

# 108 :
if 4 < 3 : # 참이면
    print("Hello world") # 출력되지 않음
else : # 거짓이면
    print("Hi , there") # 4<3 false 이기때문에 출력

# 109 :
if True : # True 이면 실행
    print("1") # 출력
    print("2") # 출력
else :
    print("3") # 출력되지 않음

print("4") # if와 관련이 없기 때문에 그냥 출력

# 110
if True :
    if False :
        print("1") # 출력x
        print("2") # 출력x
    else :  # 실행
        print("3") # 출력
else :
    print("4")

# 111
입력저장 = input( "입력 : ")
print( 입력저장*2 ) # 문자*2 : 반복출력

# 112
입력저장 = int( input("숫자입력 : ") )
print( 입력저장 * 10 )

# 113
입력저장 = int( input("홀수/짝수 판단 점수입력 : " ) )
if 입력저장 % 2 == 0 : # 값을 나누기 2 했을때 나머지가 0이면 짝수 // 나머지가 1 이면 홀수
    print("짝수")
else :
    print("홀수")

# 114
입력저장 = int( input("숫자입력 : "))
더한값 = 입력저장 + 20
if 더한값 > 255 : # 20를 더한 후 255보다 크면
    print(255)
else :
    print( 더한값 )

# 115
입력저장 = int( input("숫자입력 : "))
뺀값 = 입력저장 - 20
if 뺀값 > 255 : # 20를 뺀 후 255보다 크면
    print(255)
elif 뺀값 < 0 : # 0 보다 작으면
    print( 0 )
else:
    print(뺀값)

# 116
입력저장 = input("현재시간 : ")
if 입력시간[-2 : ] == "00" :
    print("정각 입니다")
else:
    print("정각이 아닙니다")

# 117 :
과일 = ["사과" , "포도" , "홍시"]
입력과일 = input("좋아하는 과일? : ")
if 입력과일 in 과일 : # 입력하 ㄴ과일이 리스트에 포함되어 있으면
    print("정답입니다")
else :
    print("오답입니다")

# 118 :
투자경고리스트 : ["마이크로소프트" , "구글" , "네이버" , "카카오" , "삼성" , "엘지"]
종목 : input("종목선택 : ")
if 종목 in 투자경고리스트 : # 입력한 값이 리스트에 포함되어 있으면
     print("투자 경고 종목 입니다")

# 119  :
과일 = {"봄":"딸기" , "여름":"토마토" , "가을":"사과"}
입력계절 = input("제가 좋아하는 계절은 ? ")
if 입력계정 in 과일 : # 입력한 계절이 딕셔너리에 키 가 포함되어 있으면
    print("정답입니다")
else:
    print("오답입니다")

# 120 :
과일 = {"봄":"딸기" , "여름":"토마토" , "가을":"사과"}
입력과일 = input("제가 좋아하는 과일은 ? ")
if 입력계절 in 과일 : # 입력한 과일이 딕셔너리에 값 에 포함되어 있으면
    print("정답입니다")
else:
    print("오답입니다")

# 121  :
입력저장 = input("영문 입력 : " )
if 입력저장.islower() : # 소문자이면 True 아니면 false
    print( 입력저장.upper() ) # 대문자로 변환
else:
    print( 입력저장.lower()) # 소문자로 변환

# 122 :
점수 = int( input("점수입력 : "))
if 점수 >= 81 :
    print("A등급")
elif 점수 >= 61 :
    print("B등급")
elif 점수 >= 41 :
    print("C등급")
elif 점수 >= 21 :
    print("D등급")
else :
    print("E등급")

#  123 :
환률 = {"달러":1167 , "엔":1.096 , "유로":1268 , "위안":171}
입력저장 = input("금액과 통화명 입력 : ")
금액 , 통화명 = 입력저장.split(" ") # 공백 기준으로 분리
print(int(금액) * 환률[통화명] , "원") # 환률 딕셔너리에서 입력한 통화명 찾아서 값 가져오기

# 124 :
숫자1 = int( input("숫자1 입력 :  "))
숫자2 = int( input("숫자2 입력 : " ))
숫자3 = int( input("숫자3 입력 : " ))

#정답1
print(max(숫자1 , 숫자2 , 숫자3 ))
#정답2
if 숫자1 > 숫자2 and 숫자2 and 숫자3 : # 숫자1 이 숫자2보다 크면서 숫자3보다 크면
    print( 숫자1 )
elif 숫자2 > 숫자1 and 숫자2 > 숫자3 : # 숫자2 가 숫자1 보다 크면서 숫자3보다 크면
    print(숫자2)
else :
    print(숫자3)

# 125 :
핸드폰번호 = input("핸드폰번호 입력 : ") # 010-1111-1111
통신사번호 = 핸드폰번호.split("-")[0] # - 기준으로 분리후 첫번재 값 가져오기 = 010
if 통신사번호 == "011" :
    print("당신은 SKT 입니다")
elif 통신사번호 == "016" :
    print("당신은 KT 입니다")
elif 통신사번호 == "LGU" :
    print("당신은 LGU 입니다")
else:
    print(" 알수 없습니다 ")

# 126 :
우편번호 = input("우편번호 : ")
우편번호 = 우편번호 [ 0 : 3 ] # 0 ~2 까지 가져오기 [ 앞3자리 ]
if 우편번호 in ["010" , "011" , "012" ] : # 010 011 012 : 강북구
    print("노원구")
if 우편번호 in ["014" , "015" , "016" ] : # 014 015 016 : 노봉구
    print("노원구")

# 127 :
주민번호 = input("주민등록번호 : ")
주민번호 = 주민번호.split("-")[1] # -기준으로 분리 했을때 뒷자리
if 주민번호[0] == "1" or 주민번호[0] == "3" :
    print("남자")
else:
    print("여자")

# 128 :
주민번호 = input("주민등록번호 : ")
뒷자리 = 주민번호.split("-")[1] # -기준으로 분리 했을때 뒷자리 가져오기
# 00 - 08 : 서울 // 00 - 12 부산
if 0 <= int (뒷자리 [1:3] ) <= 0 :
     print("서울입니다")
else:
    print("서울입니다")

# 129 :
주민번호 = input("주민등록번호 : ")
계산1 = int( 주민번호[0]) *2 + int( 주민번호[1] )*3 + int( 주민번호[2]) *4 +  int( 주민번호[3]) *5 + \
       int( 주민번호[4]) *6 +  int( 주민번호[5]) *7 +  int( 주민번호[7]) *8 + int( 주민번호[8]) *9 + \
       int( 주민번호[9]) *2 +  int( 주민번호[10]) *3 + int( 주민번호[11]) *4 +  int( 주민번호[12]) *5
# 주민번호[ 0 ] : - 제외


# 130 :
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
                    # 해당 주소의 딕셔너리 가져오기[ data ] 키 의 값 을 가져오기
변동폭 = int(btc["max_price"]) - int(btc["min_price"]) # 최고가 - 최저가 => 차이
시가 = int(btc["opening_price"]) #
최고가 = int(btc["max_price"])

if(시가 + 변동폭) > 최고가 :
    print("상승장")
else:
    print("하락장")


