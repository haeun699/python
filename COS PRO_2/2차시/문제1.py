
# 문제1 : 제품의 제품번호를 count[제품번호]
max_product_number = 10

def func_a(gloves) :
    counter = [0 for _ in range(max_product_number) ]
    for x in gloves : # 해당 장갑의 제품번호 = 인덱스 번호
        counter[x] += 1 # +1 저장
    return counter
        # 순서도 : [2 , 1 , 2 , 2 , 4 ]
            # 왼손 count [ 1, 3, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0]
        # 순서도 : [1,2,2,4,4,7]
            # 오른손 count [ 1,2,0,2,0,0,1,0,0,0]

def solution(left_glovers, right_glovers) :
    left_counter = func_a(left_glovers) # 왼손 장갑 제품별 개수 세기
    right_counter = func_a(right_glovers) # 오른손 장갑 제품별 개수 세기

    total = 0 # 각 제품 번호별 최대한 많은 장갑 쌍 개수 세기
    for i in range(1, max_product_number + 1) :
        total += min (left_counter[i], right_counter[i])
    return total

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
left_gloves = [2, 1, 2, 2, 4] # 왼손 장갑의 제품번호
right_gloves = [1, 2, 2, 4, 4, 7] # 오른손 장갑의 제품번호
ret = solution(left_gloves, right_gloves)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다")

