# date: 2021/09/02
# problem: 2021 카카오 인턴십, level2
# link: https://programmers.co.kr/learn/courses/30/lessons/81302#fn1

def solution(places):
    answer = []
    pos = [(x, y) for x in range(5) for y in range(5)]

    # 대기실 하나씩 순회
    for place in places:
        flag = False
        for x, y in pos:
            # P가 있는곳부터 check() 수행 (거리두기 지키는지 확인하는 함수)
            if place[x][y] == 'P':
                if not check(x, y, place):
                    answer.append(0)
                    flag = True
                    break
        if not flag:
            answer.append(1)
    return answer

def check(x, y, place):
    # 1칸 인접하는 좌표
    dist = [(1,0), (0,1), (-1,0), (0,-1)]
    for dx, dy in dist:
        nx, ny = x+dx, y+dy  # x, y 다음 한칸씩 이동한 좌표
        if -1 < nx < 5 and -1 < ny < 5 and place[nx][ny] == 'P':  # 다음 원소가 P인경우 실패
            return False
    # 대각선으로 인접한 좌표
    dist = [(1,1), (-1,1), (-1,-1), (1,-1)]
    for dx, dy in dist:
        nx, ny = x+dx, y+dy
        if -1 < nx < 5 and -1 < ny < 5 and place[nx][ny] == 'P' and (place[x][ny] != "X" or place[nx][y] != "X"):
            return False
    # 2칸 떨어진 좌표
    dist = [(2,0), (0,2), (-2,0), (0,-2)]
    for dx, dy in dist:
        nx, ny = x + dx, y + dy
        if -1 < nx < 5 and -1 < ny < 5 and place[nx][ny] == 'P' and place[x+dx//2][y+dy//2] != "X":
            return False
    return True

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))

