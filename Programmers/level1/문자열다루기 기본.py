# date: 2021/07/16
# level: 1
# link: https://programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    answer = True
    if (len(s) == 4 or len(s) == 6) and s.isdigit() == True:
        return answer
    else:
        return False


# 다른사람 풀이
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)