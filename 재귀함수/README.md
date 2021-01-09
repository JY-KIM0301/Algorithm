# 백준 10872: 팩토리얼 
https://www.acmicpc.net/problem/10872 

## 문제
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.

**예제 입력**
```
10
```

**예제 출력**
```
3628800
```

## 풀이 코드

``` java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	public static void main(String[] args) throws IOException {
		//Scanner sc = new Scanner(System.in);
		//n = sc.nextInt();
		//sc.close();
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		int result = f(n);
		System.out.println(result);
	}
	
	public static int f(int n) {
		if(n <= 1) return 1;
		return n * f(n-1);
	}
}

```
`#java`

**설명**    
간단한 팩토리얼 문제였고, 재귀함수로 구현했다. 첫번째 제출에서 런타임 에러(StackOverflow)가 발생했다. 
이유는 재귀함수부에서 return 조건문을 잘못 작성했다.. ```if(n == 1) return 1;``` 이라고 제출했었다! 
생각을해보자. 팩토리얼은 0 또는 양의정수로만 구현할수 있기때문에 저렇게 n이 1일때만 1을 반환시켜버리면
만약 n에 0이 들어가는경우 재귀호출부분에서 f(-1)으로 음수가 호출되기때문에 런타임에러가 발생하는 것이다. 
추가적으로, 스캐너보다 BufferedReader를 사용하는 것이 훨씬 빨랐다.
