# 재귀함수 기초 예제 (2)
1차원 배열 {3, 5, 7}이 있다. 이들의 부분집합을 구하고, 각 집합에 들어있는 원소의 개수를 출력해보자. 
O 라고 표시된 부분이 원소가 들어있다는 의미이다. 재귀함수를 이용해 풀어본다. 

![image](https://user-images.githubusercontent.com/61649201/104103141-cb7db880-52e3-11eb-89ae-9b6a3267d680.png)
## 코드

``` java
//재귀함수로 부분집합 구하는 프로그램 만들기 

public class Main {
	static int[] arr = {3, 5, 7};
	static int N = arr.length;
	static boolean[] v = new boolean[N];
	
	public static void main(String[] args) {
		// 부분집합 개수는?
		System.out.println("부분집합 수: "+ (1<<N));
		f(0,0);
	}	
	
	public static void f(int idx, int cnt) { // (부분집합 구현부, 원소개수 카운팅부)
		if(idx == N) {
			for(int i=0; i<N; i++) {
				if(v[i]) System.out.print(arr[i] + " ");
			}
			System.out.println("==> 원소의 개수: " + cnt);
			return;
		}
		
		v[idx] = true; // idx자리에 원소가 들어있다면 (O라면)
		f(idx+1, cnt+1); // f호출: idx한칸 옆으로, cnt도 하나 증가
		v[idx] = false; // X인경우
		f(idx+1, cnt); // X여도 다음 원소탐색하러 idx는 한칸이동, cnt는 그대로 (개수는 증가안함)
	}
}

```
`#java`

## 설명   
먼저, main함수 body부에서 부분집합의 개수를 구하기위해 ``` (1<<N) ``` 이라고 나타냈고 여기서 N은 배열의 길이다. 
예제에서 배열의 길이는 3이기 때문에 1<<3 하면 2^3인 총 8가지의 부분집합이 출력될 것이다.

이제 원소의 개수를 구해보자. 먼저 함수하나를 만들고 ```f(int idx, int cnt)``` 이렇게 부분집합들을 나타낼 idx와 원소 개수를 카운팅할 cnt를 넣어줬다. 이 문제풀때 어떻게 재귀호출을 할까 정말 고민이었는데.. boolean형의 1차원배열을 하나 만들어주고 인덱스가 있으면 true, 없으면 false를 반환하고 각각의 경우에 맞도록 다시 f를 호출해주었다. 이렇게하니까 원소가 들어있든 없든지 idx는 무조건 한칸옆으로 (+1), cnt는 원소가 있는경우에만 +1증가해 각 집합마다의 원소 개수를 셀 수 있게됐다! 
