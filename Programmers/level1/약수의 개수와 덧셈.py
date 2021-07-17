# date: 2021/07/17
# level: 1
# link: https://programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    answer = 0

    for x in range(left, right + 1):
        divisor = []
        # 약수 구하기
        for i in range(1, x + 1):
            # x%i가 0이면 i는 x의 약수이다
            if x % i == 0:
                divisor.append(i)

        if len(divisor) % 2 == 0:  # 약수의 개수가 짝수인 경우
            answer += x
        else:  # 홀수인 경우
            answer -= x
    return answer


# 다른사람 풀이
import math

def solution(left, right):
    answer = 0
    for i in range(left, right + 1, 1):
        sqrt = math.sqrt(i)
        if int(sqrt) == sqrt:
            answer -= i
        else:
            answer += i

    return answer