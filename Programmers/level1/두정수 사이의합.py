# date: 2021/07/16
# level: 1
# link: https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    answer = 0
    if b > a:
        for i in range(a, b+1):
            answer += i
    elif a > b:
        for i in range(b, a+1):
            answer += i
    else:
        return a or b
    return answer



# 다른사람 풀이
def adder(a, b):
    # 함수를 완성하세요
    if a > b: a, b = b, a

    return sum(range(a,b+1))