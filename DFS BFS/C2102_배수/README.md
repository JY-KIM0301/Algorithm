# 코드업 2102: 배수

https://codeup.kr/problem.php?id=2102

## 문제

자연수 N이 입력될 때, 0과 1로 이루어진 N의 배수 중 가장 작은 자연수를 출력하시오.

**예제 입력**

```
3
```

**예제 출력**
0과 1로 이루어진 N의 배수 중 가장 작은 자연수를 출력한다. 이때 출력되는 자연수의 맨 앞자리는 1이어야 한다. 조건을 만족하는 자연수가 unsigned long long형의 범위에 없을 경우 0을 출력한다.

```
111
```

## 풀이 코드

```python
import sys
n = int(sys.stdin.readline())

def multiple_min(n):
  b_num = 0b1
  d_num = int(format(b_num, "b"), 10)

  while True:
    if d_num % n == 0:
      return d_num
    b_num += 1
    d_num = int(format(b_num, "b"), 10)

    if d_num >= 100000000000000000000:
      return 0

print(multiple_min(n))

```

## 풀이 과정

이진수 1, 10, 11, 100, ... 를 만들기 위해 b_num 변수에 이진수 1값을 넣어두고 무한루프에서 1씩 더해주었다. 그리고 조건문에서 n으로 나누어 떨어지면 반환되도록 구현했다.
