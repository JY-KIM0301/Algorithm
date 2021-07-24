# date: 2021/07/24
# level: Silver 3
# link: https://www.acmicpc.net/problem/2512

n = int(input())
budget_list = list(map(int, input().split()))
m = int(input())

start = 1 
end = max(budget_list)  # 예산 최댓값 저장

while start <= end:
    mid = (start + end) // 2  # 중간값 저장
    total_budget = 0  # 합계를 저장할 변수 초기화

    for budget in budget_list:  # budget과 mid값을 하나씩 비교탐색 시작
        if budget > mid:
            total_budget += mid  # 상한선보다 예산 값이 크기때문에 상한값들로 교체후, 누적합해줌
        else:
            total_budget += budget  # 작거나 같은경우, 해당 budget을 그대로 누적합
    # 전체 국가예산(m)과 비교
    if total_budget > m:  # 전체 예산보다 크다면, 상한선 크기를 줄이고 재탐색
        end = mid - 1
    else:  # 작거나 같은경우, 충족은 되지만, 최대 예산을 받기위해 최적값 찾으러 재탐색
        start = mid + 1
print(end)  # 최대 예산 출력
