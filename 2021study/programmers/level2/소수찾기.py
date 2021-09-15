# date: 2021-09-16
# link: https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3
# level: 2

from itertools import permutations

def is_prime_number(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    lst = []
    for i in range(len(numbers)):
        lst.append(numbers[i])
    per = []
    # 자리수마다 순열구하기
    for i in range(1, len(lst) + 1):
        per += list(permutations(lst, i))  # tuple 리스트 형태의 순열이 생성됨
    # tuple 내의 원소들을 연결해 숫자로 만드는 작업
    new_lst = [int(('').join(p)) for p in per]
    # 중복제거
    new_lst = list(set(new_lst))

    # 소수판별
    for item in new_lst:
        if is_prime_number(item) == True:
            answer += 1

    return answer