# date: 2021/07/21
# level: Silver 3
# link: https://www.acmicpc.net/problem/2805

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)
height = 0

# 이진탐색 (반복문)
while start <= end:
    mid = (start + end) // 2  # 중간길이 저장
    cut_tree = 0  # 벌목된 나무길이의 합 초기화

    # tree가 mid길이보다 길다면, 벌목가능 -> 잘린 값들을 누적합 시킴
    for tree in trees:
        if tree > mid:
            cut_tree += (tree - mid)

    # 벌목된 나무길이가 m보다 크거나 같다면, mid길이를 늘리고 다시 조사해본다 (나무를 아끼기위한 최적값 찾기)
    if cut_tree >= m:
        # 그때의 mid값 저장
        height = mid
        start = mid + 1
    # 벌목된 나무길이가 m보다 작다면, 충족시키지 못한것. 최대길이를 낮춘다.
    elif cut_tree < m:
        end = mid - 1

print(height)

"""
1. 처음에 start 초기값을 min(trees)로 설정해서 틀림. 
-> 나무를 하나라도 무조건 잘라야하기 때문에 절단기의 길이 최솟값을 1로 시작해야한다.
2. cut_tree가 m과 동일한 경우, 같다고해서 그대로 반환하는게 아니라, 최적의 height값이 존재하는지 다시 조사해야함 
-> 단순 인덱스찾기 문제와는 조금 다르다 
"""