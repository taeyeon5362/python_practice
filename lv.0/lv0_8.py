def solution(angle):
    if angle > 90 :
        if angle == 180 :
            return 4
        return 3
    else :
        if angle == 90 :
            return 2
        return 1
