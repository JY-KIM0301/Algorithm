# date: 2021/07/12
# level: 1
# link: https://programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    answer = []
    y = 0
    for _ in range(n):
        y += x
        answer.append(y)

    return answer


# 다른사람 풀이
def number_generator(x, n):
    # 함수를 완성하세요
    return [i * x + x for i in range(n)]
print(number_generator(2, 5))
