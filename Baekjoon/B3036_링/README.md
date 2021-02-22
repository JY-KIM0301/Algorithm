# 백준 3036: 링

https://www.acmicpc.net/problem/3036

## 문제

상근이는 첫 번째 링을 돌리기 시작했고, 나머지 링도 같이 돌아간다는 사실을 발견했다. 나머지 링은 첫 번째 링 보다 빠르게 돌아가기도 했고, 느리게 돌아가기도 했다. 이렇게 링을 돌리다 보니 첫 번째 링을 한 바퀴 돌리면, 나머지 링은 몇 바퀴 도는지 궁금해졌다.

링의 반지름이 주어진다. 이때, 첫 번째 링을 한 바퀴 돌리면, 나머지 링은 몇 바퀴 돌아가는지 구하는 프로그램을 작성하시오.  
**예제 입력**  
첫째 줄에 링의 개수 N이 주어진다. (3 ≤ N ≤ 100)

다음 줄에는 링의 반지름이 상근이가 바닥에 놓은 순서대로 주어진다. 반지름은 1과 1000를 포함하는 사이의 자연수이다.

```
4
12 3 8 4
```

**예제 출력**
출력은 총 N-1줄을 해야 한다. 첫 번째 링을 제외한 각각의 링에 대해서, 첫 번째 링을 한 바퀴 돌리면 그 링은 몇 바퀴 도는지 기약 분수 형태 A/B로 출력한다.

```
4/1
3/2
3/1
```

## 풀이 코드

```java
import java.util.Scanner;

public class B3036 {
	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		int N = sc.nextInt(); // 링의 개수 입력

		// 첫번째 링
		int firstRing = sc.nextInt();
		for(int i=1; i<N; i++) {
			int otherRing = sc.nextInt();

			// 최대공약수 구하기
			int gcdResult = gcd(firstRing, otherRing);

			// 분모와 분자를 각각 최대공약수로 나누어 출력하기
			System.out.println((firstRing / gcdResult) + "/" + (otherRing / gcdResult));
		}

	}

	// 최대공약수 함수
	static int gcd(int a, int b) {
		int r;

		while(b != 0) {
			r = a % b;
			a = b;
			b = r;
		}
		return a;
	}
}

```

`#java`

**설명**
처음에 둘레를 구해보니 어차피 약분되어 첫번째 반지름 / 다른 원들의 반지름을 각각 구하면 되는 문제인줄 알았다. 하지만 기약분수로 출력하라는 조건이 있었고, 기약분수로 나타내려면 결과값의 분모와 분자를 각각 그들의 최대공약수로 나눠주면 된다. 최대공약수 구하는 알고리즘만 알면 풀수있는 간단한 예제.
