"""
https://www.acmicpc.net/problem/1753
정점과 간선, 가중치가 주어지고 지정된 시작 노드부터 도착 노드까지 최단경로를 구하는 문제.
먼저, 순차탐색으로 구현해본다.
백준 제출결과: 시간초과
해결방법: 우선순위 큐로 풀어야함 
"""
import sys
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())  # 노드수(V), 정점수(E)
k = int(input())  # 시작노드(k)
graph = [[]for i in range(V+1)]  # 연결된 노드 정보를 저장할 리스트
visited = [False] * (V+1)  # 방문여부 체크를 위한 리스트, 방문한 경우 True
distance = [INF] * (V+1)  # 최단경로를 저장할 리스트, 무한대로 초기화

# 간선정보 입력
for _ in range(E):
    u, v, w = map(int, input().split())
    # u에서 v로 이동하는 가중치가 w라는 의미
    graph[u].append((v, w))

# 방문하지 않은 노드중, 가장 최단거리가 짧은 노드를 반환
def get_smallest_node():
    min_value = INF
    index = 0  # 최단거리가 가장 짧은 노드 (0부터 초기화)
    for i in range(1, V+1):
        # i번째 노드의 최단거리가 무한대보다 작으면서, 방문한 적이 없는 경우
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]  # 해당 최단거리로 업데이트 된다
            index = i  # 해당 인덱스를 가진 노드로 업데이트 된다
            # distance[1] 부터 순차적으로 탐색하면서 가장 짧은 거리를 찾으며, 만약 거리가 같다면 먼저 나온 인덱스를 반환
    return index

# 다익스트라 구현
def dijkstra(k):
    # 시작노드 초기화
    distance[k] = 0
    visited[k] = True  # 시작노드부터 방문함을 의미
    for j in graph[k]:
        distance[j[0]] = j[1]

    # 시작노드를 제외하고 전체 (V-1)개 노드에 대해 반복
    for i in range(V-1):
        # 현재 최단거리가 가장 짧은 노드를 꺼내, 방문처리한다.
        now = get_smallest_node()
        visited[now] = True

        # 현재노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재노드를 거쳐 다른노드로 이동하는 거리가 더 짧은 경우 -> 최단경로 갱신
            if cost < distance[j[0]]:
                distance[j[0]] = cost  # 해당 cost를 최단경로로 갱신

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