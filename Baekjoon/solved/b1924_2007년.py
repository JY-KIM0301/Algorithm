# date: 2021/07/17
# level: Bronze 1
# link: https://www.acmicpc.net/problem/1924

x, y = map(int, input().split())

week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

before_month = 0
for i in range(x-1):
    before_month += month_length[i]
before_month = (before_month + (y-1)) % 7

print(week[before_month])

"""
처음에 이전 달들의 날짜합 만을 7로 나누고 y-1 만큼 더한 값으로 인덱스를 찾으니까
당연히 week 배열 범위 초과해서 인덱스 에러가 났다^^
1/1부터 구하고자 하는 날짜의 총 날짜 수의 합을 구하고 7로 나눈 나머지에 해당하는 인덱스를 찾아야함. 
슬라이싱으로 해결할 수 있지않을까..? 생각했는데 아래 sum함수와 슬라이싱을 이용한 풀이가 있었다.  
"""

# 다른사람 풀이
x, y = map(int,input().split())
M = [31,28,31,30,31,30,31,31,30,31,30,31]
D = ['SUN','MON','TUE','WED','THU','FRI','SAT']

print(D[(sum(M[:x-1])+y) % 7])

"""
위의 풀이를 한줄 출력으로 해결.. 
슬라이싱은 문자열 문제에서 엄청 유용하다. 내가 잘 활용할줄 모르는게 문제 
"""