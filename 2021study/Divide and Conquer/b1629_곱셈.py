# date: 2021/07/17
# level: Silver 1
# link: https://www.acmicpc.net/problem/1629

# 분할정복 재귀함수 구현
def divide_conquer(base, power, divider):
    if power == 1:
        return base % divider
    elif power % 2 == 0:
        tmp = divide_conquer(base, power/2, divider)
        return (tmp * tmp) % divider
    else:
        tmp = divide_conquer(base, (power-1)/2, divider)
        return (tmp * tmp * base) % divider

# main
a, b, c = map(int, input().split())
print(divide_conquer(a, b, c))

# pow() 함수사용
# a, b, c = map(int, input().split())
# print(pow(a, b, c))  # a ^ b % c 의미.. pow()에 나머지 기능까지 있는줄 몰랐다


# 시간초과 발생 코드
# a, b, c = map(int, input().split())
# print((a**b) % c)