import re
def solution(my_string):
    return sum(int(i) for i in str(re.sub(r"[^0-9]", "", my_string)))
