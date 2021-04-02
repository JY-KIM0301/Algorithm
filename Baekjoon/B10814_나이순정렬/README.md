# 백준 10814: 나이순 정렬

https://www.acmicpc.net/problem/10814

## 문제

온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

**예제 입력**  
첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)

둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다. 나이는 1보다 크거나 같으며, 200보다 작거나 같은 정수이고, 이름은 알파벳 대소문자로 이루어져 있고, 길이가 100보다 작거나 같은 문자열이다. 입력은 가입한 순서로 주어진다.

```
3
21 Junkyu
21 Dohyun
20 Sunyoung
```

**예제 출력**  
첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.

```
20 Sunyoung
21 Junkyu
21 Dohyun
```

## 풀이 코드

```python
import sys
num = int(sys.stdin.readline())
member = []    # member 이름을 가진 배열 생성
for i in range(num):
	[x, y] = sys.stdin.readline().split()
	member.append([x, y])    # member에 [x, y] 넣어주기
result = sorted(member, key= lambda member: int(member[0]))
for i in range(num):
	print(result[i][0], result[i][1])
```

## 풀이 과정

`sorted` 함수는 파이썬에 내장된 정렬함수로, 문제에서는 sorted(정렬할 데이터, key 파라미터) 를 사용했다. key 파라미터는 어떤 것을 기준으로 정렬할 것인지 조건을 걸어주는 키워드이다. 입력받은 member배열을 정렬하기 위해서 단순히 `sorted(member)`만 걸어줬더니 이름까지 알파벳 오름차순으로 정렬이 되었다. 따라서 key를 설정해 나이값으로만 오름차순 정렬을 하도록 조건을 걸어주면 된다.
