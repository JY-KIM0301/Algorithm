# 백준 2231: 분해합

https://www.acmicpc.net/problem/2231

## 문제

어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.

자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오. <br>
**예제 입력**

```
216
```

**예제 출력**

```
198
```

## 풀이 코드

```java
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		// 입력받을 자연수 N, 생성자를 저장할 result 선언 및 초기화
		Scanner sc= new Scanner(System.in);
		int N = sc.nextInt();
		int result = 0;

		for(int i=0; i<N; i++) {
			int number = i;
			int sum = 0; // 각 자리수의 합을 저장할 변수, sum

			while(number != 0) {
				sum += number % 10; // number가 0이 아닌 경우만 각 자리수 더하기
				number /= 10;
			}

			// i값과 각 자리수의 합이 같다 -> 생성자 발견
			if(sum + i == N) {
				result = i;
				break; // 종료
			}

		}
		System.out.println(result);

	}
}

```

`#java`

**설명**  
브루트포스(brute-force) 알고리즘이란?

- 조합 가능한 모든 문자열을 하나씩 대입해보는 알고리즘 방식
- 이론적으로 가능한 모든 경우의수를 다 검색해보는 방식이라 정확도는 100% 보장된다

이 문제는 브루트포스 방식을 사용하여 가장 작은 생성자를 찾아내는 문제이다.  
1부터 N까지 하나씩 대입하여 탐색하다가 생성자를 발견하면 해당 생성자를 출력후 종료, 존재하지 않으면 0을 출력한다.

하나의 반복문만 있으면되고, 생성자 i를 저장할 number와 각 자리수의 합을 저장할 sum 변수를 생성.

생성자가 0인경우를 제외하고 나머지 생성자들 각각의 자리수를 더해 sum에 저장시킨다.
