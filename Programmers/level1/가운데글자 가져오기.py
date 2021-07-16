# date: 2021/07/16
# level: 1
# link: https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    if len(s) % 2: #홀수길이
        return s[len(s)//2]
    else: #짝수길이
        return s[(len(s)//2)-1 : len(s)//2+1]


# 다른사람 풀이
def string_middle(str):

    return str[(len(str)-1)//2:len(str)//2+1]