# 백준 2108번: 통계 알고리즘
https://www.acmicpc.net/problem/2108  

## 문제
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.  

1. 산술평균 : N개의 수들의 합을 N으로 나눈 값  
2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값  
3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값  
4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이  
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.  

**예제 입력**
```
5
1
3
8
-2
2
```
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.  
둘째 줄에는 중앙값을 출력한다.  
셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.  
넷째 줄에는 범위를 출력한다.  

**예제 출력**
```
2
2
1
10
```

## 풀이 코드

``` java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/*백준 2108번: 통계 알고리즘
산술평균, 중앙값, 최빈값, 범위를 구하는 프로그램을 작성하세요*/

public class Main {
	public static void main(String[] args) throws IOException{

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		double[] arr = new double[N];
		double sum = 0;

		
		for(int i = 0; i < N; i++) {
			int input = Integer.parseInt(br.readLine());
			arr[i] = input;
			sum += input;
		}
		
		// 1.산술평균
		System.out.println((int)Math.round(sum / N));
		
		// 2.중앙값
		Arrays.sort(arr);
		System.out.println((int)arr[N/2]);
		
		// 3.최빈값 -- 제일어렵...
		int[] freq = new int[8001];
		for(double d : arr) freq[(int)d+4000]++; // 빈도수 입력
		int maxFrequency = 0; // 최대 빈도값
		int maxIndex = 0; // 최대 빈도값을 가진 인덱스
		for(int i=0; i<8001; i++) {
			if(freq[i] > maxFrequency) {
				maxFrequency = freq[i];
			}
		}
		boolean twice = false; // 두번째인지 구별하기 
		
		for (int i = 0; i < 8001; i++){ 
			if ( freq[i] == maxFrequency ) { // 최빈값인 경우
				if (twice){ 
					maxIndex = i - 4000; 
					break; 
					} 
				maxIndex = i - 4000; 
				twice = true; // 플래그 세우기 
			}
		}
		System.out.println(N==1 ? (int)arr[0] : maxIndex);
		
		// 4.범위
		int result = (int)(arr[N-1] - arr[0]);
		System.out.println(result);
	}

}
```
`#java`

**설명**    
최빈값 구하는게 가장 어려웠다..  
먼저, 정수의 범위가 -4000 ~ +4000 이라는 조건이 주어졌으므로, 8001의 크기를 갖는 1차원 배열을 추가로 생성한다.  
가장 많이 등장하는 값을 `maxFrequency` 변수에 저장, 해당 빈도값이 위치하는 인덱스를 `maxIndex`라고 했다.  
배열안의 값들을 하나씩 순회하면서 maxFrequency보다 큰 (많이 등장하는)값이 있으면 maxFrequency에 다시 저장!   
최댓값을 찾았을때, freq[-4000]에 해당하는 값이 최빈값이 될것이다. 그러나 이경우는 최빈값이 하나일때고!  

문제에서 최빈값이 <b>여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다</b> 라고 했으므로,  
최빈값이 여러개인 경우와 최빈값이 하나일 경우 두가지를 생각해야한다..  

최빈값이 여러개인 경우를 체크하기 위해 boolean 변수 twice를 추가.  
freq 배열의 값이 최빈값보다 크다면, 최빈값의 index를 갱신하고 twice를 flase로 바꾼다.  
그 이후에 최빈값이 같게 나오면 twice를 true로 변경.  

따라서 N이 1이면 arr[0]를 출력하고, 아닌경우 maxIndex에 위치한 값을 출력하면 된다.

![백준2108](https://user-images.githubusercontent.com/61649201/105626875-4d3e1c00-5e76-11eb-8e7a-5ae29cd705e5.PNG)  

