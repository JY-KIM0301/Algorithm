# problem: 가장 긴 증가하는 부분수열2
# link: https://www.acmicpc.net/problem/12015

n = int(input())
a = list(map(int, input().split()))

d = [0]

for i in range(n):
    start = 0
    end = len(d) - 1

    # 이진탐색
    while start <= end:
        mid = (start + end) // 2  # 중간길이의 부분수열 길이 저장
        if d[mid] >= a[i]:
            end = mid - 1
        else:
            start = mid + 1
    # d[i] 중에서 가장 작은 a[i]를 저장
    if start >= len(d):
        d.append(a[i])
    else:
        d[start] = a[i]
    # print(d)
    '''
    a = [10, 20, 10, 30, 20, 50]
    [0, 10]
    [0, 10, 20]
    [0, 10, 20]
    [0, 10, 20, 30]
    [0, 10, 20, 30]
    [0, 10, 20, 30, 50]
    4
    '''
print(len(d[1:]))