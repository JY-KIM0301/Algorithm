# date: 2021/08/21
# problem: 최솟값, 최댓값
# description: 세그먼트 트리
# link: https://www.acmicpc.net/problem/2357

import sys

input = sys.stdin.readline


# 최솟값 세그먼트 트리
def init_min(start, end, node):
    if start == end:
        tree_min[node] = tree[start]
        return tree_min[node]
    mid = (start + end) // 2
    tree_min[node] = min(init_min(start, mid, node * 2), init_min(mid + 1, end, node * 2 + 1))
    return tree_min[node]


# 최댓값 세그먼트 트리
def init_max(start, end, node):
    if start == end:
        tree_max[node] = tree[start]
        return tree_max[node]
    mid = (start + end) // 2
    tree_max[node] = max(init_max(start, mid, node * 2), init_max(mid + 1, end, node * 2 + 1))
    return tree_max[node]


# 최솟값 구하기
def find_min(start, end, left, right, node):
    # 이분탐색으로 찾는 구간이 전체 구간에 포함되어 있다면 해당 노드 return
    if right < start or end < left:
        return sys.maxsize
    if left <= start and end <= right:
        return tree_min[node]
    mid = (start + end) // 2
    return min(find_min(start, mid, left, right, node * 2), find_min(mid + 1, end, left, right, node * 2 + 1))


# 최댓값 구하기
def find_max(start, end, left, right, node):
    # 이분탐색으로 찾는 구간이 전체 구간에 포함되어 있다면 해당 노드 return
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree_max[node]
    mid = (start + end) // 2
    return max(find_max(start, mid, left, right, node * 2), find_max(mid + 1, end, left, right, node * 2 + 1))


# main
n, m = map(int, input().split())

# 트리 사이즈 초기화
size = 1
while size < n:
    size *= 2

# 최소, 최대 트리 초기화
tree_min = [0] * (2 * size)
tree_max = [0] * (2 * size)

# 입력 배열 리프노드에 채우기
tree = []
for i in range(n):
    tree.append(int(input()))

# 초기화함수 실행
init_min(0, n - 1, 1)
init_max(0, n - 1, 1)

for _ in range(m):
    a, b = map(int, input().split())
    print(find_min(0, n - 1, a - 1, b - 1, 1), find_max(0, n - 1, a - 1, b - 1, 1))
