'''
점수중에 최대값을 M. 모든 점수를 점수/M*100으로 고쳤다.
최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.
세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.

3
40 80 60

75.0
'''
from sys import stdin

n = int(input())
score_list = list(map(int, stdin.readline().split()))
max_score = max(score_list)

new_score_list = []
for score in score_list:
    new_score_list.append(score / max_score * 100)

print(sum(new_score_list) / n)