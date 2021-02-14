# 백준 2577: 숫자의 개수

https://www.acmicpc.net/problem/2577

## 문제

세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

**예제 입력**

```
150
266
427
```

**예제 출력**

```
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
```

## 풀이 코드

**방법1: Scanner**

```java
import java.util.Scanner;

public class B2577 {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int value = sc.nextInt() * sc.nextInt() * sc.nextInt(); // 세개 자연수 입력 합
		String str = Integer.toString(value); // 곲한 결과값을 String으로 변환
		sc.close();

		for(int i=0; i<10; i++) {
			int count = 0;
			for(int j=0; j<str.length(); j++) {
				if((str.charAt(j) - '0') == i) // charAt(j) - '0' 또는 -48
					count++;
			}
			System.out.println(count);
		}
	}
}
```

**설명**  
입력 자연수가 3개로 정해졌으므로 `sc.nextInt()`로 입력과 동시에 곱한 결과를 value에 저장, String타입으로 변환해서 str에 다시 저장한다.

0부터 9까지 각각의 수가 있는지 검사하는 반복문을 첫번째 for문으로, 해당 문자열 인덱스값이 존재하면 count++를 수행하기 위한 반복문을 내장 for문으로 지정하여 같은 수를 발견할때마다 count를 1씩 증가시키면 된다.

주의해야할 점은 charAt() 메소드로 해당 인덱스의 값을 뽑아쓰면 '숫자' 형태의 문자형이 출력되어 아스키코드에 대응하는 문자가 나오므로 반드시 '0' 또는 48을 마이너스 해준다음 같은지 비교해야한다. <br><br>

**방법2: BufferedReader**

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B2577_case2 {
	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] arr = new int[10];

		int value = Integer.parseInt(br.readLine()) * Integer.parseInt(br.readLine()) * Integer.parseInt(br.readLine());
		String str = String.valueOf(value);

		for(int i=0; i<str.length(); i++) {
			arr[(str.charAt(i) - '0')]++;
			}

		for(int count : arr)
			System.out.println(count);
	}
}
```

**설명**  
Scanner 방식은 시간복잡도가 O(N^2), BufferedReader 방식은 O(N) 이라 BufferedReader 방식의 수행속도가 훨씬 빠르다.
