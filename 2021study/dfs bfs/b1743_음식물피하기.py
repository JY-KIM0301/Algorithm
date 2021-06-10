'''
떨어진 음식물중, 가장 큰 음식물의 크기를 구하라.

# . . .
  . # # .
  # # . .

위와 같이 음식물이 떨어져있고 제일큰 음식물의 크기는 4가 된다.
(인접한 것은 붙어서 크게 된다고 나와 있음.
대각선으로는 음식물 끼리 붙을수 없고 상하좌우로만 붙을수 있다.)
'''
# 그래프를 0으로 전부 초기화하고, 음식물이 떨어진 위치는 1로 바꿔준다.
# bfs로 상하좌우 탐색, 방문한 기록이 없고 1이 연속으로 있다면, cnt + 1 증가.

from collections import deque

n, m, k = map(int, input().split())
graph = [[0]*m for _ in range(n)]  # 그래프 0으로 전부 초기화
visited = [[False for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1


def bfs(a, b):
    deq = deque()
    deq.append((a, b))
    visited[a][b] = True
    cnt = 1

    while deq:
        x, y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 조건을 만족하고 방문기록이 없다면
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    deq.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
    return cnt


for x in range(n):
    for y in range(m):
        if not visited[x][y] and graph[x][y] == 1:
            result = max(result, bfs(x, y))    # 가장 많이 cnt된 경우 출력 (가장 큰 쓰레기)

print(result)
