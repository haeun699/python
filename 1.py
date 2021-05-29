def solution( shirt_size ) :
    size_count = [0,0,0,0,0,0]
    for ss in shirt_size :
        if ss in "XS" :
            size_count[0] +=1
        if ss in "S" :
            size_count[1] +=1
        if ss in "M" :
            size_count[2] +=1
        if ss in "L" :
            size_count[3] +=1
        if ss in "XL" :
            size_count[4] +=1
        if ss in "XXL" :
            size_count[5] +=1
    return size_count
함수 = ["XS" , "S" , "L" , "L" , "XL" , "S"]
print(solution(함수))

