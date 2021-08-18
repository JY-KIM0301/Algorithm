# link: https://programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations

def solution(orders, course):
    answer = []
    for cou in course:
        dict = {}
        for order in orders:
            order = sorted(order)
            combi = combinations(order, cou)
            for c in combi:
                if c in dict:
                    dict[c] += 1
                else:
                    dict[c] = 1
            print(dict)
        dict = sorted(dict.items(), reverse=True, key=lambda item: item[1])
        print(dict)
        for i in range(len(dict)):
            if dict[i][1] == dict[0][1] and dict[i][1] >= 2:   # <------------- 여기부터 이해 필요........
                answer.append(''.join(dict[i][0]))
    return sorted(answer)

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

print(solution(orders, course))