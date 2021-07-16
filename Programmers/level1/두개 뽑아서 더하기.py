# date: 2021/07/16
# level: 1
# link: https://programmers.co.kr/learn/courses/30/lessons/68644

import itertools

def solution(numbers):
  answer = set()
  for i in list(itertools.combinations(numbers, 2)):
    answer.add(sum(i))
  return sorted(answer)


# 다른사람 풀이
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))