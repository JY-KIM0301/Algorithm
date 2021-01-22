# 백준 2750: 오름차순 정렬 프로그램
https://www.acmicpc.net/problem/2750

## 문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.  


**예제 입력**
```
5
5
2
3
4
1
```

**예제 출력**
```
1
2
3
4
5
```

## 풀이 코드  

[방법1] Select Sort + Scanner   
``` java
import java.util.Scanner;

//백준 2750: 오름차순 정렬 프로그램
//Select Sort + Scanner

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] arr = new int[N];
		
		for(int i=0; i<N; i++) {
			arr[i] = sc.nextInt();	
		}
		
		// select sort 구현
		for(int i=0; i<N-1; i++) {
			for(int j=i+1; j<N; j++) {
				if(arr[i] > arr[j]) {
					int temp = arr[j];
					arr[j] = arr[i];
					arr[i] = temp;
				}
			}
		}
		
		for(int val : arr) {
			System.out.println(val);
		}
	}
}
```

[방법2] Arrays.sort + BufferedReader  
```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
 
public class Main {
	public static void main(String[] args) throws IOException {
    
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[N];
		
		for(int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
 
		// 정렬 메소드
		Arrays.sort(arr);
		
		for(int val : arr) {
			System.out.println(val);
		}
 
	}
}
```

**설명**  
선택정렬 알고리즘의 기초 예제이다.  
방법1은 선택정렬과 스캐너를 이용한 가장 기본적인 방법이고, 시간복잡도가 가장오래걸릴 것이다.  
방법2는 Arrays.sort와 BufferedReader를 사용한 방법으로, 첫번째 방법보다 성능이 좋다.  
