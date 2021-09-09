# date: 2021-09-09
# link: https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3

def solution(n, arr1, arr2):
    answer = []

    dec_arr = list(zip(arr1, arr2))

    bin_arr = []
    for first, second in dec_arr:
        result = first | second
        bin_arr.append(bin(result)[2:].zfill(n))
    for element in bin_arr:
        tmp = element.replace("1", "#").replace("0", " ")
        answer.append(tmp)
    return answer