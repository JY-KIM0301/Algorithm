# date: 2021/08/19
# description: Heap
# problem: https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    h = []
    answer = 0

    for i in range(len(scoville)):
        heapq.heappush(h, scoville[i])

    while h[0] < K:
        first = heapq.heappop(h)
        second = heapq.heappop(h)
        mix = first + 2 * second
        heapq.heappush(h, mix)
        answer += 1
        if len(h) == 1 and h[0] < K:
            return -1

    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7

print(solution(scoville, K))

# 다른사람 풀이
# heapq 모듈의 heapify(list) 함수를 사용하면 리스트를 자동으로 heap으로 변환시켜준다

'''
import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer
'''