
    #1. for 변수 in 리스트명 :
    #2. for 변수 range ( 시작값 , 끝값 , 충격단위 ) :
    #3. for 변수 in enmerate( 리스트명 ) :    인덱스와 값 동시 변환

# 문제 171
가격목록 = [ 32100 , 32150 , 32000 , 32500 ]
for 변수 in 가격목록 :
    print( 변수 )

# 문제 172
가격목록 = [ 32100 , 32150 , 32000 , 32500 ]
for i , 가격목록 in enumerate( 가격목록 ) :
    print( i,가격목록 )

# 문제 173
가격목록 = [ 32100 , 32150 , 32000 , 32500 ]
for i in range( len(가격목록) ) :
    print( 3-i , 가격목록[i])

# 문제 174
for i in range(1,4) :
    print(90 + 10 * i , 가격목록[i] )

# 문제 175
my_list = ["가" , "나" , "다" , "라" ]
for i in range( 1 , 4 ) :
    print( my_list[i-1] , my_list[i] )

# 문제 176
my_list = ["가" , "나" , "다" , "라" , "마" ]
for i in range( 2 , 5 ) :
    print( my_list[i-2] , my_list[i-1] , my_list[i] )

# 문제 177
my_list = ["가" , "나" , "다" , "라" ]
for i in range[  3 , 2 , 1 ] :
    print( my_list[i] , my_list[i-1] )

# 문제 178
내목록 = [ 100 , 200 , 400 , 800 ]
print( 내목록[1] - 내목록[0] )
print( 내목록[2] - 내목록[1] )
print( 내목록[3] - 내목록[2] )
for i in range( 3 ) :
    print( 내목록[i+1] - 내목록[i] )

# 문제 179
내목록 = [100 , 200 , 300 , 400 , 800 , 1000 , 1300 ]
print( (내목록[0] + 내목록[1] + 내목록[2] ) /3 )
print( (내목록[1] + 내목록[2] + 내목록[3] ) /3 )
print( (내목록[2] + 내목록[3] + 내목록[4] ) /3 )
print( (내목록[3] + 내목록[4] + 내목록[5] ) /3 )

for i in range( 4 ) :
    print( (내목록[1] + 내목록[i+1] , 내목록[i+2]  /3 ))

# 문제 180
저가 = [ 100 , 200 , 400 , 800 , 1000 ]
고가 = [ 150 , 300 , 430 , 880 , 1000 ]

저장리스트 = ()
for i in range( 5 ) :
    저장리스트.append( 고가(1) - 저가(i))

# 2차원 리스트 : [ [1차원] , [1차원] , [1차원] ]
 # 행 : 가로
 # 열 : 세로
# 딕셔너리 : 키 와 값 으로 이루어진 한쌍 => 여러개 저장 하는 공간

# 문제 181
아파트 = [ ["101호","102호"] , ["201호","202호"] , ["301호","302호"] ]

# 문제 182
스톡 =  { ["시가" , 100,200,300] , ["종가" , 80,210,330]}

# 문제 183
스톡 =  {"시가" : [100,200,300] , "종가" : [80,210,330]}

# 문제 184
스톡 = {"10/10" : [100 ,200 , 300] , "10/11" : [210,230,190,200]}

#문제 185
아파트 = [ [101 , 102] , [201,202] , [301,302] ]
         # 행 : 3개      # 열 : 행마다 2개
for 행 in 아파트 :
    for 열 in 행 :
        print( 열 , "호" )

# 문제 186
for 행 in 아파트[ : : -1] : # 역순[반대로] [ : : -1 ]
    for 열  in 행 :
        print(열,"호")

# 문제 187
for 행 in 아파트 [ : : -1 ] :
    for 열 in 행[ : : -1 ] :
        print( 열 , "호")

# 188
for 행 in 아파트 :
    for 열 in 행 :
        print( 열 , "호" )
        print("--------")

# 문제 189
for 행 in 아파트 :
    for 열 in 행 :
        print( 열 , "호" )
        print("--------") # 행마다 출력

# 문제 190
for 행 in 아파트 :
    for 열 in 행 :
        print(열,"호")
print("--------") # 반복문 종료후 한번만 출력

# 문제 191
data = [
    [2000 , 3050 , 2050 , 1980],
    [7500 , 2050 , 2050 , 1980],
    [15450 , 15050 , 15550 , 14900]
]
for 행 in data :
    for 열 in 행 :
        print( 열*1.00014 )
# 1 : 100% 0.5 : 50%  0.05 : 5%  0.00014 : 0.014%

# 문제 192
for 행 in data :
    for 열 in 행 :
        print(  열 * 1.00014 )
        print("-"*5)  # 행마다 출력

# 문제 193
결과 = []
for 행 in data  :
    for 열 in 행 :
     결과.append( 열 * 1.00014 ) # 하나씩 리스트에 저장
     print(결과) # 리스트 화면

# 문제 194 :
결과 = [] # 2차원 리스트 사용될 예정
for 행 in data :
    sub = [ ] #  행 리스트
    for 열 in 행 :
        sub.append( sub )
    print(결과)

# 문제 195
ohlc = [["open" , "high" , "low" , "close"] ,
        [100 , 110, 70 , 100] ,
        [200 , 210 , 100 , 190 ] ,
         [300 , 310 , 300 , 310] ]

for 행 in ohlc[ 1 : ] : # 0번 행 제외
    print( 행[3] ) # 각 행 마다 3번 인덱스 출력

# 문제 196
for 행 in ohlc[ 1 : ] : # 0번 행 제외
    if 행[3] > 150 : # 각 행 마다 3번 인덱스 값이 150보다 크면
        print( 행[3] ) # 각 행마다 3번 인덱스 출력

# 문제 197
for 행 in ohlc[ 1 : ] : #0번 행 제외
    if 행[3] >= 행[0] : # 3번 인덱스가 0번 인덱스보다 이상이면
        print( 행[3] ) # 각 행마다 3번 인덱스 출력

# 문제 198
변동폭 = []
for 행 in ohlc[ 1 : ] : # 0번 행 제외
    변동폭.append( 행[1]  - 행[2] )
                 # 고가 - 저가
print(변동폭)

# 문제 199
for 행 in ohlc :
    if 행[3] > 행[0] : # 종가가 시작보다 크면
        print( 행[1] - 행[2] ) # 변동폭 계산

# 문제 200
총수익금 = 0
for 행 in ohlc[ 1 : ] : # 0번 행 제외
    총수익금 += ( 행[3] - 행[0]) # 총가-시가 => 수익 => 총수익금
print(총수익금)