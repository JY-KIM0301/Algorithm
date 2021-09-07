# date: 2021/09/06
# link: https://programmers.co.kr/learn/courses/30/lessons/64065

import re
from collections import Counter


def solution(s):
    answer = []
    s = re.findall('\d+', s)
    count = Counter(s)
    d = list(zip(count.keys(), count.values()))
    d = sorted(d, key=lambda x: -x[1])
    for e in d:
        answer.append(e[0])
    answer = map(int, answer)
    answer = list(map(int, answer))

    return answer