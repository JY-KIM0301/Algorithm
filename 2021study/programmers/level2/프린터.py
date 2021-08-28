# date: 2021/08/28
# description: 스택/큐
# link: https://programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    # priorities 길이 만큼의 1부터 증가하는 int 배열
    int_list = []
    for i in range(1, len(priorities) + 1):
        int_list.append(i)
    # dictionary
    dictionary = dict(zip(int_list, priorities))
    # tuple
    items = deque(list(dictionary.items()))

    # location 위치 원소 저장
    pos = items[location]  # (1, 1)

    # 프린터할 목록 저장
    print_list = []

    while items:
        func(items)
        print_list.append(items.popleft())

    answer = print_list.index(pos) + 1

    return answer

def func(items):
    # 첫번째 원소 저장
    max_priority = items[0]

    # 중요도가 최대인 원소 찾기
    for i in range(1, len(items)):
        if items[i][1] > max_priority[1]:
            max_priority = items[i]

    for _ in range(items.index(max_priority)):
        items.append(items.popleft())
    return items


priorities = [2, 1, 3, 2]
location = 2

print(solution(priorities, location))
# expected return 1

# 다른사람 풀이

def solution(priorities, location):
    answer = 0
    from collections import deque

    d = deque([(v,i) for i,v in enumerate(priorities)])

    while len(d):
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer
