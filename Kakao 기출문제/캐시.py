# date: 2021/09/06
# link: https://programmers.co.kr/learn/courses/30/lessons/17680

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    status = deque()

    if cacheSize == 0:
        answer = len(cities) * 5
    else:
        for city in cities:
            city = city.upper()
            if city in status:
                answer += 1
                status.remove(city)
            else:
                answer += 5
                if len(status) >= cacheSize:
                    status.popleft()
            status.append(city)

    return answer