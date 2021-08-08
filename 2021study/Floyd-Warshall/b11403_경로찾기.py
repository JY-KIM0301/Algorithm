# date: 2021/08/08
# problem: https://www.acmicpc.net/problem/11403
# description: 최단경로 (플로이드워셜)

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
for k in range(n):
    for a in range(n):
        for b in range(n):
            # a에서 b로 다이렉트로 가는게 1이거나, k를 거쳐 a에서 b로 가는 경로가 모두 1이면 테이블 1로 업데이트
            if graph[a][b] == 1 or (graph[a][k] == 1 and graph[k][b] == 1):
                graph[a][b] = 1

for a in range(n):
    for b in range(n):
        print(graph[a][b], end=" ")
    print()