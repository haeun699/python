
# 문제7 : or => and 변경 // count +=1

def solution( scores ) : # 토익시험 특정 조건을 충족하면 초급영어강의 수강대상 구하기
    count = 0
    for s in scores :
        if 650 <= s and s < 800 :      # 토익시험 650 이상 800 미만
            count +=1
    return count

scores = [650,722,914,558,714,803,650,679,669,800] # 수강신청한 사람들의 토익점수
ret = solution( scores )

print( "solution 함수결과 : " , ret , "." )



















