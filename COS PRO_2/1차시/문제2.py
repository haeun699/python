
# 문제2

def solution(price , grade) : # 함수
    # 지문 보고 코드 작성하는 곳
    answer = 0

    if grade == "S" :
        answer = price * 0.95  # 1 :  100%  o.5 : 50%  o.25 : 25%
    if grade == "G" :
        answer = price * 0.9
    if grade == "V" :
        answer = price * 0.85

    return int (answer) # 계산된 가격을 리턴

price1 = 2500
grade1 = "V"
ret1 = solution( price1 , grade1 ) # 함수호출 ( 가격 , 등급 ) 인수를 보내기

print("Solution: return value of the function is" , ret1, ".")

price2 = 96900
grade2 = "S"
ret2 = solution(price2 , grade2)

print("Solution : return value of the function is " , ret2 , ".")