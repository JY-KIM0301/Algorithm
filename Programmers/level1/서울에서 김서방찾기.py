# date: 2021/07/12
# level: 1
# link: https://programmers.co.kr/learn/courses/30/lessons/12919

def solution(seoul):
    # Kim의 인덱스 1을 불러와야함
    x = seoul.index('Kim')
    answer = "김서방은 " + str(x) + "에 있다"
    return answer


# 다른사람 풀이
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))