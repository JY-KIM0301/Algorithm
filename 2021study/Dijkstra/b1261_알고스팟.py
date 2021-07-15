# date: 2021/07/15
# problem: 백준 1261_알고스팟
# description: 다익스트라, BFS
# link: https://www.acmicpc.net/problem/1261

import sys, heapq

input = sys.stdin.readline
INF = sys.maxsize
m, n = map(int, input().split())
distance = [[INF] * m for _ in range(n)]
a = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = []
heapq.heappush(q, [0,0,0])  # 시작점
distance[0][0] = 0

while q:
    dist, x, y = heapq.heappop(q)  # 벽을 부수는 최소 횟수를 꺼냄
    # 이미 방문처리 된경우
    if distance[x][y] < dist:
        continue
    # 상하좌우 탐색
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:  # 그래프 범위를 초과하는 경우 무시
            continue
        cost = dist + a[nx][ny]
        if cost < distance[nx][ny]:
            distance[nx][ny] = cost
            heapq.heappush(q, (cost, nx, ny))

print(distance[n-1][m-1])

