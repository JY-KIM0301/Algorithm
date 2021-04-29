# 프로그래머스 level2: 주식가격

https://programmers.co.kr/learn/courses/30/lessons/42584

## 문제

초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요. <br><br>
입출력 예

| prices          | return          |
| --------------- | --------------- |
| [1, 2, 3, 2, 3] | [4, 3, 1, 1, 0] |

<br>입출력 예 설명

- 1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
- 2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
- 3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
- 4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
- 5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.

## 풀이 코드

```python
from collections import deque
def solution(prices):
    answer = []

    prices = deque(prices)
    while prices:
        n = prices.popleft()
        cnt = 0
        for i in prices:
            if n > i:
                cnt += 1
                break
            cnt += 1
        answer.append(cnt)
    return answer
```

## 풀이 과정

스택, 큐 구현문제라서 list로 풀기보단 최대한 스택을 사용하여 풀려고했다.
이 문제는 `deque`로 구현하면 되는 문젠데, list보다 deque가 훨씬 빠르고 복잡도도 list는 O(n)인 반면에 deque는 O(1)이다. <br><br>
먼저, prices를 deque로 만들어주고 가장 첫번째 수를 큐에서 뽑아낸다.. 이때 데크에서 가장 왼쪽 숫자 하나를 빼내려면 `popleft()`메소드를 사용하면 된다. pop과 동시에 배열에서 삭제시키는 메소드이다. 이제 이 숫자를 배열에 남아있는 숫자들과 비교하여 pop한 숫자가 더 큰경우 주식 가격이 감소한 것이다. 그 경우 카운트 +1 해주고 바로 break해서 종료시킨다. <br><br>
만약 pop한 숫자가 더 작다면 가격이 증가했거나, 변화가 없는 것이므로 계속해서 카운트 +1을 해준다. 마지막은 카운트 결과들을 answer배열에 담아 출력하도록 하기!
deque를 사용해보지 않아서 조금 헷갈렸던 문제.
