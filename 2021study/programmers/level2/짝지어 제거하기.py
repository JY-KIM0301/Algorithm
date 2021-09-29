# date: 2021-09-29
# link: https://programmers.co.kr/learn/courses/30/lessons/12973
# description: 스택/큐

def solution(s):

    stack = list()

    for x in s:
        if len(stack) == 0:
            stack.append(x)
        else:
            if stack[-1] == x:
                stack.pop()
            else:
                stack.append(x)

    if len(stack) == 0:
        return 1
    else:
        return 0

print(solution("baabaa"))