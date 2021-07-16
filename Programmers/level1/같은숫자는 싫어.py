# date: 2021/07/16
# level: 1
# link: https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    result = []

    for i in arr:
        if (len(result) == 0) or (result[-1] != i):
            result.append(i)

    return result
