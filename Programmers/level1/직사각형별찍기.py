# date: 2021/07/10
# level: 1
# link: https://programmers.co.kr/learn/courses/30/lessons/12969

a, b = map(int, input().strip().split(' '))
for _ in range(b):  # 행의 수
    for _ in range(a):  # 열의 수
        print("*", end="")
    print()


# 다른사람 풀이
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)