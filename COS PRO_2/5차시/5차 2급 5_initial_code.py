def solution(a, b):
    answer = 0
    for i in range(1, b + 1): # 1~6까지 i에 넣기
        if (a * i) % b == 0:  # a *b가 b의 배수를 찾기
            # answer = b * i 오답
            answer = a * i # i가 3일때 정답
            break
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
a = 4 # 4일장
b = 6 # 6일장
    # 4일장 6일장 만나는 날 구하기 [ 공배수 ]
     # 4개수와 6배수의 동일한 수 = 공배수
     # 4 8 12 16
     # 6 12 18 24          = 12
ret = solution(a, b)




#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")