# date: 2021/07/25
# level: Gold 3
# link: https://www.acmicpc.net/problem/16434

import sys
input = sys.stdin.readline

array = []
n, h_atk = map(int, input().split())
for _ in range(n):
    t, a, h = map(int, input().split())
    array.append((t, a, h))

start, end = 1, sys.maxsize  # mid값을 1부터 무한대 사이에서 찾으려고함
answer = 0

# 이분탐색
while start <= end:
    mid = (start + end) // 2
    h_cur_hp, h_cur_atk = mid, h_atk  # 용사의 현재 생명력, 현재 공격력 초기화
    for i, j, k in array:
        if i == 1:  # 몬스터 만난경우
            if k % h_cur_atk != 0:  # 한번에 나누어 떨어지지 않는경우
                cnt = k // h_cur_atk + 1
            else:  # 딱맞게 처리한 경우
                cnt = k // h_cur_atk
            h_cur_hp -= j * (cnt - 1)

            if h_cur_hp <= 0:
                break  # 용사의 생명력이 0 이하인 경우 게임종료
        elif i == 2:  # 포션 획득한 경우
            h_cur_atk += j
            h_cur_hp = min(mid, h_cur_hp + k)
    if h_cur_hp > 0:
        end = mid - 1
        answer = mid
    else:
        start = mid + 1

print(answer)

"""
용사의 최소 생명력만 구하면 되므로, mid값과 현재 hp에 k를 더한 값중에서 최솟값을 할당해준다
용사의 생명이 0보다 크고 몬스터도 쓰러뜨렸다면 해당 mid값이 정답일 것이고, 최소의 생명력을 구해야하므로 end값을 낮추고 재탐색 해준다.
용사의 생명이 0보다 작아지면 게임이 종료되고, 다시 게임을 시작해야한다. 이때는 용사의 생명력을 이전보다 늘려줘야 하므로 start를 키우고 재탐색하면 된다.   
"""