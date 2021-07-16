# date: 2021/07/16
# level: 1
# link: https://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    if len(arr) > 1:
        arr.pop(arr.index(min(arr)))  # 최소값을 가지는 숫자의 인덱스 제거
        return arr
    else:
        return [-1]
