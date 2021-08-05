import sys

input = sys.stdin.readline

n, m = map(int, input().split())  # 도시 개수(n), 노선 개수(m)
graph = []  # 연결된 노드 정보를 저장할 리스트
# 그래프 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))  # a에서 b로 이동하는데 비용은 c
inf = sys.maxsize
distance = [inf] * (n + 1)  # 최단시간 저장할 리스트

# 벨만포드 구현
def bellman_ford(start):
    distance[start] = 0
    minus = False  # minus이면 무한
    for i in range(1, n+1):
        for j in range(m):
            start_node = graph[j][0]
            next_node = graph[j][1]
            cost = graph[j][2]
            if distance[start_node] != inf and distance[next_node] > distance[start_node] + cost:
                distance[next_node] = distance[start_node] + cost
                if i == n:
                    minus = True
    return minus

answer = bellman_ford(1)

if answer:
    print(-1)
else:
    for i in range(2, n + 1):
        if distance[i] == inf:
            print(-1)
        else:
            print(distance[i])

"""
다익스트라와 다르게 접근
1. 그래프를 우선순위 큐가 아닌, 일반 배열로 받음
2. 계속 줄어드는지 보기위해 n번 반복해서 최솟값으로 갱신 
3. n번째 값까지 갱신된다면? minus = True 한다 
4. minus가 True이면 -1, 경로가 없어도 -1, 아닌경우에 정점의 값을 출력함 
"""
