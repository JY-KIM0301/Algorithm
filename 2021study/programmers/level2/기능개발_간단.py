# date: 2021/08/18
# description: Queue
# problem: https://programmers.co.kr/learn/courses/30/lessons/42586

from collections import Counter

def solution(progresses, speeds):
    day = 1
    day_list = []
    answer = []

    while len(progresses) > 0:
        if progresses[0] + speeds[0] * day >= 100:
            progresses.pop(0)
            speeds.pop(0)
            day_list.append(day)
        else:
            day += 1

    count_list = Counter(day_list).items()

    # day_list 원소 중에서 개수만 출력
    for count in count_list:
        answer.append(count[1])

    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))