"""
https://www.acmicpc.net/problem/1753
정점과 간선, 가중치가 주어지고 지정된 시작 노드부터 도착 노드까지 최단경로를 구하는 문제.
다익스트라 알고리즘, 우선순위 큐로 구현

우선순위 큐(Priority  Queue)
- 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
힙(Heap)
- 우선순위 큐를 구현하기 위해 사용하는 자료구조 중 하나
- 최소힙, 최대힙이 존재한다
"""
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())  # 노드수(V), 정점수(E)
k = int(input())  # 시작노드(k)
graph = [[]for i in range(V+1)]  # 연결된 노드 정보를 저장할 리스트
distance = [INF] * (V+1)  # 최단경로를 저장할 리스트, 무한대로 초기화

# 간선정보 입력
for _ in range(E):
    u, v, w = map(int, input().split())
    # u에서 v로 이동하는 가중치가 w라는 의미
    graph[u].append((v, w))

# 다익스트라 구현
def dijkstra(k):
    q = []
    # 시작노드로 가기위한 최단경로는 0으로 설정해서 큐에 넣는다
    heapq.heappush(q, (0, k))
    distance[k] = 0

    while q:
        # 가장 최단거리가 짧은 노드의 정보를 꺼낸다
        dist, now = heapq.heappop(q)  # 거리값(dist), 현재노드(now)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐, 다른노드로 가는 거리가 더 짧은경우, 해당 거리로 갱신
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                # 우선순위 큐에 해당정보 기록
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 실행
dijkstra(k)

# 주어진 시작점에서 다른 모든 정점으로의 최단경로를 출력
for i in range(1, V+1):
    # 경로가 존재하지 않는 경우, INF 출력
    if distance[i] == INF:
        print("INF")
    # 경로가 존재하면 해당 경로값 출력
    else:
        print(distance[i])