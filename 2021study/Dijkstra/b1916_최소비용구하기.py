"""
https://www.acmicpc.net/problem/1916
A번째 도시에서 B번째 도시까지 가는데 드는 버스 최소비용 구하는 문제.
기본 다익스트라 문제, 우선순위 큐 사용

#1753 최단경로 문제와 로직이 비슷한데, 이문제는 종료지점까지 알려주기 때문에 마지막에 종료지점만 출력
"""

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())  # 도시의 개수(n)
m = int(input())  # 버스의 개수(m)
graph = [[]for i in range(n+1)]  # 연결된 노드 정보를 저장할 리스트
distance = [INF] * (n+1)  # 최소비용을 저장할 리스트, 무한대로 초기화

# 버스정보 입력
for _ in range(m):
    u, v, w = map(int, input().split())
    # u에서 v로 이동하는데 비용이 w라는 의미
    graph[u].append((v, w))

# 출발정보 입력
start, arrival = map(int, input().split())

def dijkstra(start):
    q = []
    # 시작노드로 가기위한 최소비용은 0으로 설정해서 큐에 넣는다
    heapq.heappush(q, (0, start))
    distance[start] = 0  # 시작지점 0으로 초기화

    while q:
        # 최소비용을 가지는 구간의 비용과 노드의 정보를 꺼낸다
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재노드와 연결된 다른 인접노드 체크
        for node in graph[now]:
            cost = dist + node[1]
            if distance[node[0]] > cost:
                distance[node[0]] = cost
                # 우선순위 큐에 해당 정보 저장
                heapq.heappush(q, (cost, node[0]))

# 다익스트라 실행
dijkstra(start)

# 종료지점 출력
print(distance[arrival])
