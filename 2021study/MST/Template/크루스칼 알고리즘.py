'''
신장 트리란, 그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 의미함.
최소한의 비용으로 구성된 신장 트리를 찾는게 '최소 신장 트리' 문제이며, 그리디 알고리즘으로 분류된다.
    1. 간선 데이터를 비용에 따라 오름차순 정렬
    2. 간선을 하나씩 확인하여 현재의 간선이 사이클을 발생시키는지 확인
        - 사이클이 발생하지 않는 경우, 최소 신장트리에 포함시킴
'''

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 찾기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# main
v, e = map(int, input().split())  # 노드개수, 간선개수 입력
parent = [0] * (v+1)  # 부모 테이블 초기화

edges = []  # 간선 저장할 리스트
result = 0  # 최종 비용 초기화

# 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 간선정보 입력
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선을 비용순으로 오름차순 정렬
edges.sort()

# 간선 하나씩 탐색, 사이클이 발생하지 않는 경우만 집합에 포함
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
