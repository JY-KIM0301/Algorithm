'''
9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고
그 최댓값이 몇 번째 수인지를 구하는 프로그램

3
29
38
12
57
74
40
85
61

85
8
'''
array = []

for i in range(1, 10):
    num = int(input())
    array.append(num)
# 여기서 sort를 사용하면 인덱스가 무너져서 안됨

print(max(array))
print(array.index(max(array)) + 1)