def solution(array):
    array.sort()
    answer = len(array) // 2
    if len(array) % 2 == 1:
        return array[answer]
    return ((array[answer - 1] + array[answer]) / 2) 
