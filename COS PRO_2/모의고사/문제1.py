# 1-m까지 누적합계
# 1 - n-1까지 누적합계
# 1단계 - 2단계 의 결과값
def func_a(k):    # m -> k   # n -1 -> k
    sum = 0 # 누적합계 변수
    for i in range(k+1):
    # for 변수 in range( ~~ 전까지 ) : 변수는 1부터 ~~ 전까지 1씩 증가하면서 반복
         # i는 1 부터 k 전까지 반복
         # i 는 1부터 k+1 전까지 반복
        sum +=i

    return sum

def solution(n, m):
    sum_to_m = func_a(m)          # 1단계
    sum_to_n = func_a(n-1)        # 2단계
    answer = sum_to_m - sum_to_n  # 3단계
    return answer

print( solution(5,10))