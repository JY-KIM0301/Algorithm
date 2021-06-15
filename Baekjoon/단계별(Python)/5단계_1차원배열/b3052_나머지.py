'''
수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다.
그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

1
2
3
4
5
6
7
8
9
10

10
'''
arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42)
# 중복 없애기위해 set 자료형 사용
arr = set(arr)
print(len(arr))
