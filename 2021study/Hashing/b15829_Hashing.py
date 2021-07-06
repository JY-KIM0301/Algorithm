'''
백준15829: Hashing
https://www.acmicpc.net/problem/15829

다음과 같이 문자열을 입력하면 주어진 해시함수를 통과해 해시값으로 결과가 출력된다.
해시값을 출력하는 프로그램 작성.

5
abcde

4739715
'''

# 문자열의 길이(L) 입력
L = int(input())
# 영문 소문자로 이루어진 문자열 입력
# 맨마지막의 \n 제거위해 rstrip() 사용
word = str(input().rstrip())

# 해시함수에 들어가는 변수 선언
r = 31
M = 1234567891

# mod 하기 전의 누적합을 저장할 변수 선언
arr_sum = 0

# 문자열의 각 인덱스를 순서대로 탐색
for idx in range(L):
    # 아스키 코드 값을 반환하는 ord() 사용
    # a에는 1, b에는 2, c에는 3, ..., z에는 26으로 고유한 번호를 부여
    a_i = ord(word[idx]) - ord('a') + 1
    arr_sum += a_i * (r ** idx)

print(arr_sum % M)
