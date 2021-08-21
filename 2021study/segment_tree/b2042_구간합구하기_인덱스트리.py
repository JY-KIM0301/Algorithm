# date: 2021/08/16
# description: 바이너리 인덱스 트리
# problem: https://www.acmicpc.net/problem/2042

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())  # n개의 수, 변경 횟수(m), 구간합 횟수(k)

arr = [0] * (n+1)  # n개 데이터 저장
tree = [0] * (n+1)  # 트리

# 누적합
def prefix(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i & -i)
    return result

# 트리 update
def update(i, dif):  # i번째 수를 dif 만큼 더한다
    while i <= n:
        tree[i] += dif
        i += (i & -i)

# 구간합
def interval_sum(start, end):
    return prefix(end) - prefix(start - 1)

# main
for i in range(1, n+1):
    x = int(input())
    arr[i] = x
    update(i, x)

for i in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:  # update 수행
        update(b, c - arr[b])
        arr[b] = c
    else:  # 구간합 수행
        print(interval_sum(b, c))
