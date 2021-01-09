# 백준 2562: 최댓값
https://www.acmicpc.net/problem/2562 

## 문제
9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

예를 들어, 서로 다른 9개의 자연수

3, 29, 38, 12, 57, 74, 40, 85, 61

이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.  

**예제 입력**
```
3
29
38
12
57
74
40
85
61
```

**예제 출력**
```
85
8
```

## 풀이 코드

``` java
import java.util.Scanner;

/*9개의 서로다른 자연수가 있다. 
최댓값을 구하고, 그 최댓값이 몇번째수인지 구하는 프로그램.
*/
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		int[] array = new int[9];
		for(int i=0; i<9; i++) {
			array[i] = sc.nextInt();
		}
		
		int max = 0;
		int index = 0;
		
		for(int i=0; i<9; i++) {
			if(array[i] > max) {
				max = array[i];
				index = i+1;
			}
		}
		System.out.println(max);
		System.out.println(index);
	}
}
```
`#java`

**설명**    
1차원 배열을 이용해 정수의 최댓값을 찾는 문제이다. for문을 이용해 배열의 크기만큼 입력값을 넣어주고, 
최댓값과 인덱스를 구하기위해 for문안에 조건문을 넣어 특정 숫자가 max값보다 크다면 그 값이 maax에 할당되도록 반복시켰다. 
