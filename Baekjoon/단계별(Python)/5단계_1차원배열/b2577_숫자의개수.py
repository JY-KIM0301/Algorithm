'''
b2577: 숫자의개수 

세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램 

150
266
427

3
1
0
2
0
0
0
2
0
0
'''
a = int(input())
b = int(input())
c = int(input())

# 곱셈결과를 리스트로 만들어주기 위해 입력값들은 int로 받고 결과를 문자열로 변환. 
arr = [int(i) for i in str(a*b*c)]

# [1,7,0,3,7,3,0,0]


array = [0]*10
for i in range(10):
    array[i] = arr.count(i)
    print(array[i])
