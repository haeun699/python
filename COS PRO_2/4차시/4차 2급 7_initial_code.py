def func_a(scores1, scores2): # 기말고사 점수에서 중간고사 점수를 뺀 값의 최댓값 함수
    answer = 0
    for score1, score2 in zip(scores1, scores2):
        answer = max(answer, score2 - score1)
    return answer

def func_b(scores1, scores2): # 기말고사 점수에서 중간고사 점수를 뺀 값의 최솟값 함수
    answer = 0
    for score1, score2 in zip(scores1, scores2):
        #answer = min(answer, score1 - score2) # 중간고사 - 기말고사 : 오답
        answer = min(answer, score2 -  score1) # 기말고사 - 중간고사
    return answer
            
def solution(mid_scores, final_scores):
    up = func_a(mid_scores, final_scores)
    down = func_b(mid_scores, final_scores)
    answer = [up, down] # 1번과2과 과정에서 구현 점수를 리스트에 담아 return
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
mid_scores = [20, 50, 40] # 중간시험
final_scores = [10, 50, 70] # 기말시험
#기말고사-중간고사 -10  0  30
ret = solution(mid_scores, final_scores)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")



