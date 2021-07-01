# k를 주기로 사람들을 제거하는 문제

n, k = map(int, input().split())

# 큐에 1부터 n까지 원소들을 저장
arr = [i for i in range(1, n+1)]

answer = []  # 제거된 사람들을 저장
num = 0

for i in range(n):
    num += k-1
    if num >= len(arr):
        num = num%len(arr)

    answer.append(str(arr.pop(num)))
print("<", ", ".join(answer)[:], ">", sep='')

