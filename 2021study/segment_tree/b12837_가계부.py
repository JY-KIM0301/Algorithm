# date: 2021/08/21
# problem: 가계부
# description: 세그먼트 트리
# link: https://www.acmicpc.net/problem/12837


# 구간합 구하기
def interval_sum(start, end, left, right, node):  # 전체구간(start, end), 찾고자 하는 부분(left, right)
    # 이분탐색하여 찾는 구간이 포함되어 있다면 노드를 return, 아니라면 0으로 채우기
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return interval_sum(start, mid, left, right, node * 2) + interval_sum(mid + 1, end, left, right, node * 2 + 1)


# 세그먼트 트리 원소값 갱신
def update(start, end, index, node, dif):
    if start > index or end < index:
        return
    tree[node] += dif
    if start != end:
        mid = (start + end) // 2
        update(start, mid, index, node * 2, dif)
        update(mid + 1, end, index, node * 2 + 1, dif)


# main
n, q = map(int, input().split())
h = 1
while h < n:
    h *= 2
tree = [0] * (h*2)
for i in range(q):
    a, b, c = map(int, input().split())
    if a == 1:  # b 번째에 c를 추가
        update(0, n-1, b-1, 1, c)
    else:  # a가 2인 경우 구간합 함수 실행
        print(interval_sum(0, n-1, b-1, c-1, 1))