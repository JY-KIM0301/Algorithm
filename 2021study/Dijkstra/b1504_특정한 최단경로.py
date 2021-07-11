# date: 2021/07/11
# problem: 백준 1504_특정한 최단경로
# description: 다익스트라, 우선순위 큐
# link: https://www.acmicpc.net/problem/1504

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, E = map(int, input().split())
graph = [[]for i in range(N+1)]  # 연결된 노드 정보를 저장할 리스트

# 간선정보 입력
for _ in range(E):
    a, b, c = map(int, input().split())
    # a부터 b까지 거리가 c
    graph[a].append([b, c])
    # b부터 a까지 거리가 c
    graph[b].append([a, c])

# 반드시 거치는 노드정보 입력
e1, e2 = map(int, input().split())

# 기본 다익스트라 로직 구현, 실행부분에서 1 -> e1와 1 -> e2 로 이동하는 경로를 각각 구해, 최솟값을 구해준다
def dijkstra(start):
    distance = [INF] * (N + 1)  # 최단거리를 저장할 리스트, 무한대로 초기화 (함수 실행할때마다 초기화해준다)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))

    return distance

# 실행
path1 = dijkstra(1)[e1] + dijkstra(e1)[e2] + dijkstra(e2)[N]
path2 = dijkstra(1)[e2] + dijkstra(e2)[e1] + dijkstra(e1)[N]
answer = min(path1, path2)
# print(path1)
# print(path2)

# 출력
if answer < INF:
    print(answer)
else:
    print(-1)