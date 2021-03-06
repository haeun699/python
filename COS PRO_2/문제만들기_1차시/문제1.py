# 문제1 : 리스트내 동일한 개수 세기
    # 조건1 : 리스트에 사이즈별로 개수를 담아서 리턴해주는 함수

def 함수(선호티셔츠): # 함수 만들기
    티셔츠개수 = [ 0 , 0 , 0 , 0 , 0 , 0  ] # 처음에는 0으로 설정
               # XS # S # M # L #XL #XXL
    for 티셔츠 in 선호티셔츠 : # 선호티셔츠 하나씩 티셔츠에 넣기
        if 티셔츠 == "XS" : # 만약에 "XS" 이면
            티셔츠개수[0] += 1 # XS 자리에 1추가
        if 티셔츠 == "S" : #만약에 "S" 이면
            티셔츠개수[1] += 1 # S자리에 1추가
        if 티셔츠 == "M" :
            티셔츠개수[2] += 1
        if 티셔츠 == "L" :
            티셔츠개수[3] += 1
        if 티셔츠 == "XL" :
            티셔츠개수[4] += 1
        if 티셔츠 == "XXL" :
            티셔츠개수[5] += 1

    return 티셔츠개수 # 함수 끝내기
# 학생들이 선호하는 티셔츠 목록
선호티셔츠 = [ "S" , "S" , "XS" , "L" , "XXL" , "S" , "XL" , "L" ]
    # XS = 1       S = 3    M = 0   L = 2    XL = 1      XXL = 1

print("함수 실행 결과 : " , 함수(선호티셔츠))

####################################################################################################

def 초등학생세기(학생나이목록) :
    초등학생인원수 = [ 0 , 0 , 0 , 0 , 0 , 0 ]

    for 초등학생 in 학생나이목록 :
        if 초등학생 == 8 :
            초등학생인원수[0] += 1
        if 초등학생 == 9 :
            초등학생인원수[1] += 1
        if 초등학생 == 10 :
            초등학생인원수[2] += 1
        if 초등학생 == 11 :
            초등학생인원수[3] += 1
        if 초등학생 == 12 :
            초등학생인원수[4] += 1
        if 초등학생 == 13 :
         초등학생인원수[5] += 1

    return 초등학생인원수
학생나이목록 = [ 8 , 8 , 9 , 10 , 10 , 10 , 11 , 9 , 8 , 12 , 13 , 8 , 11 ]

print("초등학생의 인원수 : " , 초등학생세기(학생나이목록))

##############################################################################################

# 영화관 한곳에서 하루동안 상영할수있는 총 영화의 개수 => 15시간동안 6편  12시간동안 4편   전체상영 22
# 관람객의 인원 총 수익=> 154,000    광고 => 22000000    청소부 => 959200   전기세 => 220000
# 총 세금을 구하시오(모든 상영관은 관람객이 모두 차있다 ) = > 2057480
# 입장시간 -> 광고시간 -> 영화상영시간 -> 청소시간
# 모든 상영관은 아침 8시 ~ 저녁 11시 까지만 운영한다 3*15  1*12
# 영화 한편 당 볼수있는 관람객 수 : 50명
# 영화표 : 7000원
# 영화 한편당 전기료 : 10000원
# 한관당 10명의 청소부가 청소를 한다
# 청고부의 임금 : 8,720원
# 영화 시작전 광고시간 광고비 : 1000000원
# 상영관 : 4개
# 청소시간 : 30분
# 광고시간 : 10분
# 입장시간 : 20분
# 영화상영시간 : 90분
# 조건1 : 1시부터 상영관 중 하나가 고장이나 사용 할 수 없고 3시간뒤 다시 상영 할 수 있다고한다
# 조건2 : 총 광고비와 영화표 수익은 10% 세금을 때간다


상영관 = 4
광고시간 = 10
청소시간 = 0.5
입장시간 = 20
상영시간 = 90
청소부임금 = 8720
영화표 = 7000
전기료 = 10000
광고비 = 1000000
관람객수 = 50
청소부수 = 10
전체시간 = 57
전체분 = 57*60
상영개수 = 전체분 / (청소시간+광고시간+입장시간+상영시간)
수익 = 상영개수 + 영화표 + 관람객수 + 상영개수 + 광고비
나가는돈 = 청소부수+(청소부임금 + 청소시간)+전기료 + 상영개수
세금 = (수익-나가는돈) * 0.1
print( 세금 )









