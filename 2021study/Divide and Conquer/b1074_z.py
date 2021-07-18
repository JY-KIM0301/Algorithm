# date: 2021/07/18
# level: Silver 1
# description: 분할정복, 재귀
# link: https://www.acmicpc.net/problem/1074

import sys

def z(n, x, y):
    global cnt

    if not (x <= r < x + n and y <= c < y + n):
        cnt += n * n
        return
    if n <= 2:  # 가장 작을때 분할 필요없고 값 그대로 반환
        if x == r and y == c:
            print(cnt)
            sys.exit()
        cnt += 1
        if x == r and y + 1 == c:
            print(cnt)
            sys.exit()
        cnt += 1
        if x + 1 == r and y == c:
            print(cnt)
            sys.exit()
        cnt += 1
        if x + 1 == r and y + 1 == c:
            print(cnt)
            sys.exit()
        cnt += 1
        return
    else:  # 4x4 배열부터 4분할 진행, 재귀호출
        z((n // 2), x, y)
        z((n // 2), x, y + (n // 2))
        z((n // 2), x + (n // 2), y)
        z((n // 2), x + (n // 2), y + (n // 2))

# main
input = sys.stdin.readline
n, r, c = map(int, input().split())
cnt = 0
z(2 ** n, 0, 0)

"""
시간초과가 엄청 났던 문제. 
알고보니 분할영역 내에 찾고자하는 행렬번호 칸이 존재하지 않는경우, 
분할영역의 칸 개수만큼 카운트로 더해놓고, 다음 영역으로 넘어가면 된다. 
그부분을 빠뜨려서 시간초과가 났음!! 
"""