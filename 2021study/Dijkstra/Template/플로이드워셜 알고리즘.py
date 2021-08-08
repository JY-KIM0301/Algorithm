# 플로이드워셜 템플릿

import sys
input = sys.stdin.readline
inf = sys.maxsize

n = int(input())  # 노드개수
m = int(input())  # 간선개수
graph = [[inf]*(n+1) for _ in range(n+1)]  # 최단거리 테이블 (2차원리스트)

# n번에서 n번으로 가는 비용 0 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 간선정보 입력
for _ in range(m):
    # a->b 로 가는 비용이 c. 테이블에 모든 c값이 들어온다
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플로이드워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없는경우 -1 출력
        if graph[a][b] == inf:
            print("-1", end=" ")
        else:  # 거리를 순서대로 출력
            print(graph[a][b], end=" ")
    print()

'''
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
1 4 6

0 4 -1 6 
3 0 7 9 
5 -1 0 4 
-1 -1 -1 0 
'''