# 백준 1427: 소트인사이드
https://www.acmicpc.net/problem/1427

## 문제
배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.  


**예제 입력**
```
2143
```

**예제 출력**
```
4321
```

## 풀이 코드

``` java
package boj;

// 백준 1427: 소트인사이드

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		char arr[] = br.readLine().toCharArray(); 
		Arrays.sort(arr);
		
		for(int i=arr.length-1; i>=0; i--) {
			System.out.print(arr[i]);
		}
		
	}

}

/*
 * 입력 2143
 * 
 * 출력 4321
 */
```
`#java`

**설명**    
문자타입의 1차원 배열로 각 숫자들의 공간을 만들어주고, 입력에 들어가는 값은 `toCharArray()`를 사용하여 배열을 문자열로 전환시켜준다.  
그다음부터는 매우간단한데, `Arrays.sort()`로 먼저 오름차순 정렬 해준후에, 반복문을 사용해서 배열 끝부터 0번째까지 내림차순으로 출력하면 된다.  
