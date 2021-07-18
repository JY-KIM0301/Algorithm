# date: 2021/07/18
# level: Silver 1
# description : 분할정복, 재귀
# link: https://www.acmicpc.net/problem/1992

# 잘린부분이 같은 숫자인지 확인
def same_num(n, x, y):
    start = image[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if start != image[i][j]:  # 하나의 숫자라도 다르면 4분할
                print("(", end='')
                same_num(n//2, x, y)  # 왼쪽 위
                same_num(n//2, x, y+n//2)  # 오른쪽 위
                same_num(n//2, x+n//2, y)  # 왼쪽 아래
                same_num(n//2, x+n//2, y+n//2)  # 오른쪽 아래
                print(")", end='')
                return
    if start == 0:  # 숫자가 모두 0인 경우
        print('0', end='')
    else:  # 모두 1인 경우
        print('1', end='')

# main
n = int(input())
image = []
for _ in range(n):
    image.append(list(map(int, input())))

same_num(n, 0, 0)

"""
'('와 ')'를 같이 출력하는게 어려웠음.. 
"""