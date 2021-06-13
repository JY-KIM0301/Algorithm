from sys import stdin

n, m, v = map(int, stdin.readline().split())
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)

# 간선 입력받기
for _ in range(m):
    x, y = map(int, stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(v):
    visited[v] = True
    print(v, end=" ")
    for i in range(1, n+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    visited[v] = False
    queue = [v]
    while queue:
        v = queue.pop(0)
        print(v, end=" ")
        for i in range(1, n+1):
            if visited[i] and graph[v][i] == 1:
                queue.append(i)
                visited[i] = False
dfs()
print()
bfs()

# 런타임 에러발생???