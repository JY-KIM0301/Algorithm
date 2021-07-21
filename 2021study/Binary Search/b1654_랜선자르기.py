# date: 2021/07/21
# level: Silver 3
# link: https://www.acmicpc.net/problem/1654
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = [int(input()) for i in range(k)]

start = 1
end = max(lan)
result = 0

while start <= end:
    mid = (start + end) // 2  # 중간길이의 랜선길이 저장
    lan_cnt = 0  # 자른 랜선 개수저장

    for i in lan:
        lan_cnt += i // mid

    if lan_cnt >= n:
        result = mid
        start = mid + 1

    else:
        end = mid - 1
print(result)

"""
처음에 틀렸었다. 이유는 for문을 돌때 각 랜선(i)들이 mid값보다 클때만 잘려져야 한다는 조건을 걸어줬기 때문.
생각해보면 랜선중에 한번도 안잘리는게 있을 수 있다. 우리는 n개의 잘린 랜선만 얻으면 되는것. 
주어진 테케로는 답이 바로 나와서 그냥 제출했던것 같다. 
"""