# date: 2021/08/21
# problem: 구간 합 구하기
# description: 세그먼트 트리
# link: https://www.acmicpc.net/problem/2042

from math import ceil, log2

# 세그먼트 트리 초기화
def init():
    # 리프노드(인덱스 size-1) 부터 루트노드(인덱스 0)까지 구현
    for i in range(size-1, 0, -1):
        tree[i] = tree[i*2] + tree[i*2+1]

# 구간합 구하는 함수
def sum(start,end,left,right,node):  # 전체구간(start, end), 찾고자 하는 부분(left, right)
    # 이분탐색하여 찾는 구간이 포함되어 있다면 노드를 return, 아니라면 0으로 채우기
    if right<start or end<left:
        return 0
    if left<=start and end<=right:
        return tree[node]
    mid=(start+end)//2
    return sum(start,mid,left,right,node*2)+sum(mid+1,end,left,right,node*2+1)

# 세그먼트 트리값 갱신 (원소가 변경되는 경우)
def update(index, diff):
    temp = index + size - 1  # 변경되는 노드의 인덱스
    # temp 번째 노드부터 연결된 모든 부모노드, 루트노드까지 모두 변경
    while temp >= 1:
        # 갱신하는 값과 원래의 값의 차이를 diff, 관련된 노드에 모두 더해준다
        tree[temp] += diff
        temp //= 2

# main
n, m, k = map(int, input().split())
size = 2**ceil(log2(n))  # 리프노드 크기
tree = [0]*(size*2)

# 입력 값을 리프노드에 채우기
for i in range(n):
    tree[size+i] = int(input())

init()  # 초기화함수 실행

for i in range(m+k):
    a, b, c = map(int,input().split())
    if a == 1:
        diff = c-tree[size+b-1]  # 바뀌는 곳(b), 바뀌는 값(c)
        update(b, diff)
    else:
        print(sum(1, size, b, c, 1))