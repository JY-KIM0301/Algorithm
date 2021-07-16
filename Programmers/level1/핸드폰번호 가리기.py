# date: 2021/07/16
# level: 1
# link: https://programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    answer = ''

    back_four_number = phone_number[-4:]
    return ('*') * (len(phone_number) - 4) + back_four_number


