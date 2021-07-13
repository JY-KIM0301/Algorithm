# date: 2021/07/13
# problem: 백준 4485_녹색옷 입은애가 젤다지?
# description: 다익스트라, BFS, 우선순위 큐
# link: https://www.acmicpc.net/problem/4485

import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
tc = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(n, a, distance):  # 그래프 크기 (n*n 행렬), 그래프 입력(a), 최단거리 저장할 리스트 (distance)
    q = []
    heapq.heappush(q, (0, 0, 0))
    distance[0][0] = 0

    while q:
        # 가장 최단거리의 노드 정보 꺼내기
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:  # 현재 노드가 이미 방문된적 있으면 무시
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:  # 그래프의 범위를 벗어나는 경우 무시
                continue
            cost = dist + a[nx][ny]  # !!!
            # 현재 노드를 거쳐 다른노드로 가는 거리가 더 짧은 경우 -> 갱신
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                # 우선순위 큐에 해당 정보 기록
                heapq.heappush(q, (cost, nx, ny))
    # 정답은 [n-1][n-1] 배열의 값에 시작점의 위치값을 더해준 결과
    return distance[n-1][n-1] + a[0][0]

# 실행 및 출력
while True:
    tc += 1
    n = int(input())
    if n == 0:
        break
    a = [list(map(int, input().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]
    print("Problem %d: %d\n" % (tc, dijkstra(n, a, distance)))