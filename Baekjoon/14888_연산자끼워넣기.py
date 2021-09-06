# date: 2021/09/06
# link: https://www.acmicpc.net/problem/14888

from itertools import permutations

n = int(input())
numbers = list(map(int, input().split(' ')))
operator = list(map(int, input().split()))

new_operator = []
if operator[0] != 0:
    new_operator.append(['+' for _ in range(operator[0])])
if operator[1] != 0:
    new_operator.append(['-' for _ in range(operator[1])])
if operator[2] != 0:
    new_operator.append(['*' for _ in range(operator[2])])
if operator[3] != 0:
    new_operator.append(['//' for _ in range(operator[3])])

new_new_operator = sum(new_operator, [])
answer = []

print(set(list(permutations(new_new_operator, len(new_new_operator)))))

for i in set(list(permutations(new_new_operator, len(new_new_operator)))):
    first = numbers[0]
    for right, op in zip(numbers[1:], i):
        if op == '//':
            if first < 0:
                first = -(abs(first) // right)
            else:
                first = first // right
        else:
            first = eval(str(first) + op + str(right))
    answer.append(first)

print(max(answer))
print(min(answer))
