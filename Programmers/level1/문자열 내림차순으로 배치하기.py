# date: 2021/07/10
# level: 1
# link: https://programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    answer = ''.join(sorted(s, reverse = True))
    # 알파벳을 내림차순 정렬하는 문제
    return answer