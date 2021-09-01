# date: 2021/08/31
# problem: 수식 최대화 (2020 카카오 인턴십), level2
# link: https://programmers.co.kr/learn/courses/30/lessons/67257

import itertools
import re

def solution(expression):
    answer = 0
    operators = []

    # 연산자 순열 구하기
    for i in range(len(expression)):
        if expression[i] == '-' or expression[i] == '+' or expression[i] == '*':
            operators.append(expression[i])  # 연산자만 입력
    ops = []
    for operator in operators:
        if operator not in ops:
            ops.append(operator)  # 연산자 중복없이 ops에 저장
    ops = list(itertools.permutations(ops, len(ops)))  # 순열
    # [('-', '*', '+'), ('-', '+', '*'), ('*', '-', '+'), ('*', '+', '-'), ('+', '-', '*'), ('+', '*', '-')]

    # expression 리스트 변환 ['숫자', '연산자', '숫자', ... ]
    expression = re.split('(\D)', expression)
    # ['100', '-', '200', '*', '300', '-', '500', '+', '20']

    for op in ops:
        copy_expression = expression.copy()
        for i in op:
            idx = 0
            while idx < len(copy_expression):
                if copy_expression[idx] == i:  # 찾는 연산자 발견시, 연산자 기준으로 좌 우 연산 수행
                    left, right = int(copy_expression[idx-1]), int(copy_expression[idx+1])
                    if i == '+':
                        sub_ans = left + right
                    elif i == '-':
                        sub_ans = left - right
                    else:
                        sub_ans = left * right
                    copy_expression = copy_expression[:idx-1] + list(str(sub_ans).split()) + copy_expression[idx+2:]  # 계산 결과를 배열에 대체해서 대입
                    print(copy_expression)
                else:
                    idx += 1
        else:
            answer = max(answer, abs(int(copy_expression[0])))

    return answer

expression = "100-200*300-500+20"
print(solution(expression))
print(solution("50*6-3*2"))

# expected result: 60420, 300