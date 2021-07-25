# date: 2021/07/25
# level: Silver 1
# link: https://www.acmicpc.net/problem/2110

n, c = map(int, input().split())
x = sorted([int(input()) for _ in range(n)])

start, end = 1, x[-1]-x[0]  # 두 공유기 사이의 간격이 가장 인접할때 (start), 가장 멀리있는 경우(end)
answer = 0

while start <= end:
    mid = (start + end) // 2  # 간격을 중간값으로 저장해둔다
    # 첫번째 집에는 공유기 무조건 설치
    router_install = x[0]
    # 설치한 공유기 개수 카운팅
    cnt = 1
    # 그다음 집부터 탐색하면서 공유기를 설치해준다
    # 첫번째 집에서 부터 mid간격 이상 떨어진 곳에만 설치 가능
    for i in range(1, n):
        if x[i] >= router_install + mid:
            cnt += 1
            router_install = x[i]

    # 탐색이 끝났는데 설치된 공유기 개수가 c 미만이면 간격을 줄이고, 재탐색
    if cnt < c:
        end = mid - 1
    # 공유기 개수가 c 이상이면 간격을 넓히고 재탐색
    else:
        start = mid + 1
        answer = mid

print(answer)

"""
처음엔 어려웠던 문제. 
문제의 핵심은 두개의 거리들 중에서 최대거리를 구하는 것으로, 
최대거리를 구하려면 첫번째 (가장왼쪽) 집에는 공유기가 무조건 설치될 것이다. 
마지막에 mid를 answer에 저장해두는 것도 .. 우리는 공유기 개수가 c개라는걸 확인해도 최대 거리를 구하기 위해 재탐색에 들어간다. 
만약 재탐색 결과가 조건을 만족하지 않는다면? 이전에 구해놓은건 무시되고 while문이 종료될 것이다. 
따라서 조건을 충족할때마다 mid값을 저장해둘 공간이 필요하다.   
"""