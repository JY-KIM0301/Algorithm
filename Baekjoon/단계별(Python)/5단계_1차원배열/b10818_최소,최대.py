'''
주어진 배열에서 최소와 최대값 출력하는 프로그램

[input]
5
20 10 35 30 7

[output]
7 35
'''
# min(), max() 사용 풀이법
n = int(input())
array = list(map(int, input().split()))  # 개수 상관없이 리스트로 받음
print(min(array), max(array))

# sort() 사용 풀이법
n = int(input())
array = list(map(int, input().split()))
array.sort()
print(array[0], array[-1])

# 정렬하는것보다 min, max함수 사용하는게 더 빨랐다. 거의 차이는 없음.