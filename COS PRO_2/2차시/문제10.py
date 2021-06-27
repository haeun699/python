
# 문제10 : 총 지금된 상품권의 금액 구하기 => 한줄 변경
def solution(purchase) :
    total = 0 # 총 지금된 상품권의 금액
    for p in purchase : # 상품가격을 p 에 하나씩 대입
        if p >= 10000000 : # 상품가격이 백만원이상이면
            total += 500000 # 5만원 지급
        elif p>=600000 : # 상품가격이 60만원이상이면
            total += 300000 # 3만원지급
        elif p>=400000 : # 상품가격이 40만원이상이면
            total += 200000 # 2만원 지급
        #else : # 그외 이면 [ 40만원미만이면 지급x ]
        elif p>= 2000000 :
            total += 100000
        return total

purchase = [ 15000000 , 21000000 , 399990 , 990000 , 1000000 ]

print ("solution 함수의 반환 값은 : " ,ret)