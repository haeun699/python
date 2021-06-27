#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(people):
    #여기에 코드를 작성해주세요.
    answer = [0 for _ in range(4)] # 0을 4개 가지고있는 리스트
    for 사이즈 in people :
        if 사이즈 < 95 :   # 사이즈가 95 미만이면
            answer[0] += 1 #리스트[0] = s의 개수에 1 추가
        elif 사이즈 >=95 and 사이즈<100 :
            answer[1] += 1 # 리스트[1] = M의 개수에 1추가
        elif 사이즈 >=100 and 사이즈 <105 :
            answer[2] +=1 # 리스트[2] = L의 개수에 1추가
        elif 사이즈 >= 105 :
            answer[3] += 1 # 리스트[3] = XL의 개수에 1추가
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
people = [97, 102, 93, 100, 107] # 주문 사이즈
       # [ m , l , s , l , xl ]
ret = solution(people)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")