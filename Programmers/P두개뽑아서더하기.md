# 프로그래머스(level 1): 두개뽑아서 더하기

https://programmers.co.kr/learn/courses/30/lessons/68644

## 문제

정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

**예제 입력**

```
[2,1,3,4,1]
```

**예제 출력**

```
[2,3,4,5,6,7]
```

## 풀이 코드

```python
import itertools

def solution(numbers):
  answer = set()
  for i in list(itertools.combinations(numbers, 2)):
    answer.add(sum(i))
  return sorted(answer)
```

## 풀이 과정

조합 함수를 이용한 간단한 문제였다.

- `set()` : 답이 들어올 배열에 중복이 없게하기 위해 set()함수 사용
- `combinations` : 조합 함수 사용해서 2개씩 묶어 조합을 만들고 리스트에 넣어줌 순서쌍 하나당 i번째고 for문을 돌려 각각을 더해준다 `sum(i)`
- 오름차순 정렬 위해 `sorted()` 사용
