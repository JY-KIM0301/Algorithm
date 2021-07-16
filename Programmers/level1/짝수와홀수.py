# date: 2021/07/10
# level: 1
# link: https://programmers.co.kr/learn/courses/30/lessons/12937

def solution(num):
    if num % 2 == 0:
        return("Even")
    else:
        return("Odd")


# 다른사람 풀이
def evenOrOdd(num):
    if (num%2):
        return "Odd"
    else:
        return "Even"