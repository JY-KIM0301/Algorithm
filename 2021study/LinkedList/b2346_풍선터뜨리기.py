from _collections import deque

n = int(input())
data = deque(enumerate(map(int, input().split())))
index_list = []

while True:
    idx, paper = data.popleft()
    index_list.append(idx + 1)

    if not data:
        break

    if paper > 0:
        data.rotate(-(paper - 1))
    elif paper < 0:
        data.rotate(-paper)

print(' '.join(map(str, index_list)))


