# n^2 으로 시간초과 발생. 트리로 풀어야함.

n, m, k = map(int, input().split())
data = []
arr = []
answer = []
for _ in range(n):
    d = input()
    data.append(int(d))

for _ in range(m+k):
    a, b, c = map(int, input().split())
    arr.append((a, b, c))


for i in arr:
    sum_value = 0
    prefix_sum = [0]

    if i[0] == 1:  # a가 1인경우
        # b번째 수를 c로 바꾼다
        data[i[1]-1] = i[2]

    if i[0] == 2:  # a가 2인경우
        for j in data:
            sum_value += j
            prefix_sum.append(sum_value)

        # b번째부터 c까지 구간합 저장
        answer.append(prefix_sum[i[2]] - prefix_sum[i[1]-1])
        # print(prefix_sum)

[print(answer[i]) for i in range(len(answer))]