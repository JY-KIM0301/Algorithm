# 백준 1978: 소수찾기

https://www.acmicpc.net/problem/1978

## 문제

주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

**예제 입력**

```
4
1 3 5 7
```

**예제 출력**

```
3
```

## 풀이 코드

```java
import java.util.Scanner;

public class B1978 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int count = 0;

		// 수가 수를 나누기 위해서는 그 몫이 항상 필요하며 나누는 수와 몫 중 어느 하나는 반드시 sqrt(n) 이하의 수이다.
		for(int i=0; i<N; i++) {

			// 소수이면 true, 아니면 false
			boolean isPrime = true;

			int num = sc.nextInt();

			if(num == 1) {
				continue;
			}
			for(int j=2; j<=Math.sqrt(num); j++) {
				if(num % j == 0) {
					isPrime = false;
					break;
				}
			}
			if(isPrime) {
				count++;
			}
		}
		System.out.println(count);
	}

}
```

`#java`

**설명**
소수인지 판별하는 함수를 boolean타입으로 정의해서 소수이면 true, 아니라면 false를 반환하도록. 주의할점은 숫자 1은 소수가 아니다 내부에서 반복분을 2부터 돌리는데 Math클래스의 sqrt() 메소드를 사용하여 해당수의 제곱근 이하까지로 잡고, 0으로 나누어 떨어진다면 소수가 아님! 소수인경우만 count하여 출력해주면 된다.
