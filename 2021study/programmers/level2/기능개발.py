# date: 2021/08/18
# description: Queue
# problem: https://programmers.co.kr/learn/courses/30/lessons/42586

from collections import Counter

def solution(progresses, speeds):
    day = 1
    temp_list = []
    answer = []

    while len(progresses) > 0:
        if progresses[0] + speeds[0] * day >= 100:
            progresses.pop(0)
            speeds.pop(0)
            temp_list.append(day)
        else:
            day += 1
    # print(temp_list)

    # temp_list를 돌면서 다음 원소가 현재 원소보다 작다면 현재 원소로 바꾸기
    i = 0
    for j in range(1, len(temp_list)):
        if temp_list[j] < temp_list[i]:
            temp_list[j] = temp_list[i]
        i += 1
    # print(temp_list)
    # print(Counter(temp_list))

    count_list = Counter(temp_list).items()
    # print(count_list)

    # temp_list 원소 중에서 개수만 출력
    for count in count_list:
        answer.append(count[1])

    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))