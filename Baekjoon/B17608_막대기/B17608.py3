import sys

N = int(sys.stdin.readline())
data = []  # 배열 생성

for _ in range(N):
  data.append(int(sys.stdin.readline()))
  # 입력받은 데이터를 배열에 저장 

target = data[-1]
answer = 1

for i in range(N-1, -1, -1):
  if data[i] > target:
    target = data[i]
    answer += 1

print(answer)

