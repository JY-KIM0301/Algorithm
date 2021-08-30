# date: 2021/08/30
# level: 2
# link: https://programmers.co.kr/learn/courses/30/lessons/17677

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