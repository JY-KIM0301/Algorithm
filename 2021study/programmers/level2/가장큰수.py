# date: 2021-09-29
# link: https://programmers.co.kr/learn/courses/30/lessons/42746
# description: 문자열 정렬

"""
순열을 사용하면 답은 맞는데 시간초과가 났다. 도저히 모르겠어서 풀이과정 보고 푼 문제.
- 문자열의 대소비교는 ASCII 코드로 비교되기 때문에 '6'과 '10'을 비교한다면 ord('6')이 ord('1')보다 더 크기때문에 '6' > '10' 이라는 결과가 나온다.
"""

def solution(numbers):

    # numbers 원소 문자열로 형변환
    numbers = [str(x) for x in numbers]

    # 원소를 3번 반복한 형태의 숫자로 고친결과로 비교하여 내림차순 정렬
    numbers = sorted(numbers, key=lambda x: x*3, reverse=True)

    return str(int(''.join(numbers)))

print(solution([6, 10, 2]))