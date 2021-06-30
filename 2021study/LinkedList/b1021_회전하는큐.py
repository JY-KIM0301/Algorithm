from _collections import deque

n, m = map(int, input().split())
# 큐에 원소들을 저장
data = deque([i for i in range(1, n+1)])

# 뽑고자하는 수의 index 리스트
index = list(map(int, input().split()))

cnt = 0
for num in index:
    while 1:
        if data[0] == num:
            data.popleft()
            break
        else:
            if data.index(num) <= n//2:
                data.rotate(-1)
                cnt += 1
            else:
                data.rotate(1)
                cnt += 1

print(cnt)


