# date: 2021/08/30
# problem: [1차]뉴스 클러스터링, level2
# link: https://programmers.co.kr/learn/courses/30/lessons/17677

"""
단순해보였지만, 조건들이 까다로운 문제였다. 다중집합의 교집합, 합집합 구하는 부분에서 한참 고민했다..
다중집합  a={1,1,2,2,3}, b={1,2,2,4,5} 라고 한다면 교집합은 {1,2,2}, 합집합은 {1,1,2,2,3,4,5}가 된다.
따라서 교집합을 구할때는 a에 있는 원소가 b에도 들어있다면, 각각에서 겹치는 원소를 동시에 빼내야한다. (40~44 lines)
"""

import math
import string

def solution(str1, str2):
    alphabet = [i for i in string.ascii_uppercase]  # 대문자 알파벳 리스트만들기

    # 입력된 문자열 대문자로 변환
    str1 = str1.upper()
    str2 = str2.upper()

    arr1, arr2, a, b = [], [], [], []

    for i in range(len(str1)-1):
        arr1.append(str1[i:i+2])
    for j in range(len(arr1)):
        if arr1[j][0] in alphabet and arr1[j][1] in alphabet:
            a.append(arr1[j])

    for i in range(len(str2) - 1):
        arr2.append(str2[i:i + 2])
    for j in range(len(arr2)):
        if arr2[j][0] in alphabet and arr2[j][1] in alphabet:
            b.append(arr2[j])

    a_copy = a.copy()
    b_copy = b.copy()

    # 다중집합의 교집합
    intersection = []
    for i in a:
        if i in b_copy:
            intersection.append(i)
            a_copy.remove(i)
            b_copy.remove(i)

    # 다중집합의 합집합
    union = intersection + a_copy + b_copy

    print(intersection)
    print(union)

    # 자카드 유사도
    if len(union) == 0:
        jaccard = 1
    else:
        jaccard = len(intersection)/len(union)
    answer = math.floor(jaccard * 65536)

    return answer

str1 = "abccc"
str2 = "ccdefgg"

print(solution(str1, str2))

# expected result = 16384