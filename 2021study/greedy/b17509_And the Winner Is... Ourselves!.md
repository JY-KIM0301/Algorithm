# 백준 17509: And the Winner Is... Ourselves!

https://www.acmicpc.net/problem/17509

## 문제

Let us remind you about how the total penalties are calculated for this contest:

- When you solve a problem at minutes, is added to your penalty, where is the number of incorrect verdicts (except compile errors) received on that problem.
- If you do not solve a problem before the contest ends, the incorrect verdicts on that problem are not counted as penalties.  
  Here is a bad news for all of you: we, the problem setters, are planning to join the competition and solve our own problems!

We know our problems really well, so we can solve all the problems before the contest ends. Furthermore, we can precisely predict how long it takes to solve each problem, and how many incorrect verdicts (except compile errors) we get in each problem. Depending on the order of the problems we solve, our total penalty might differ. What is the minimum penalty if we solve all problems? <br><br>
**예제 입력**

```
20 1
20 0
20 3
10 0
10 0
10 0
30 0
30 0
30 0
20 0
20 10
```

**예제 출력**

```
1360
```

## 풀이 코드

```python
list = [[int(x) for x in input().split()] for y in range(11)]

list.sort(key=lambda x:x[0])
sum_error = 0

list_m = []
for i in list:
    list_m.append(i[0])

arr = [0] * 11
arr[0] = list_m[0]
for i in range(1, 11):
    arr[i] = arr[i-1] + list_m[i]
sum_time = sum(arr[0:])

for x, y in list:
    sum_error += y*20
print(sum_time + sum_error)

```

## 풀이 과정

2x11 배열을 입력받고 첫번째열은 걸린 시간, 두번재열은 에러횟수를 나타내고 T+20V 이라는 패널티를 구하는 공식이 주어졌다.

모든 문제를 풀어서 최소의 패널티 점수를 출력하는 문제. 틀린횟수가 0이더라도 문제를 푼 횟수에 따라 패널티도 증가하게 된다. 틀린횟수는 언제 틀리든 상관없이 20을 곱해서 모두 더해주면 되는데, 시간의 경우에는 푸는데 가장 적은시간이 걸리는 문제부터 풀어야 최소의 패널티점수를 받게된다.

따라서 시간을 기준으로 오름차순 정렬후에, 각각 따로 연산해서 마지막에 합해주었다.  
그리고 걸린 시간에 따른 패널티는 10 + (10+10) + (10+10+10) + ... 이러한 규칙이 보여서 dp로 풀었다!!
