def solution(korean, english):
    answer = 0
    math = 210 - ( korean + english )
    # 210 - ( 영어점수 + 수학점수 ) : 영어+수학을 먼저 더한다음 빼기
    if math > 100: # 수학점수 100점 초과
        answer = -1 # -1 : 비정상
    else: # 아니면
        answer = math # 찾은 수학점수를 결과에 저장
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
korean = 70
english = 60
ret = solution(korean, english)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")





def solution(korean , eglish) :
    answer = 0
    math = 210 - (korean + eglish)
    if math > 100 :
        answer = -1
    else:
        answer = math
    return answer
korean = 75
eglish = 60
ret = solution(korean,eglish)

print(ret)




















def solution(korean , eglish) :
    answer = 0
    math = 210 - (korean+eglish)
    if math > 100 :
        answer = -1
    else :
        answer = math
    return answer

korean = 75
eglish = 60
ret = solution(korean , eglish)

print( ret )