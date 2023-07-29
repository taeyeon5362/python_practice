def solution(money):
    a = 0
    b = 0
    if money / 5500 == 1 :
        a += 1
    else :
        a = money // 5500
        b = money % 5500
        
    answer = [a,b]
    return answer
