# 재귀함수 기초 예제 (1)
재귀함수를 사용해 1부터 100까지의 합계, 팩토리얼, 최대공약수 프로그램을 구현해보자. 

## 코드

``` java
public class 재귀함수_기초1 {

	public static void main(String[] args) {
		System.out.println("---1부터 100까지 합계---");
		System.out.println("단일 for loop: "+sum1(100));
		System.out.println("재귀함수: "+sum2(100));
		System.out.println("---팩토리얼 프로그램---");
		System.out.println(factorial(10));
		System.out.println("---최대공약수 프로그램---");
		System.out.println(gcm(9, 24));
		
	}

	public static int sum1(int n) {
		int sum = 0;
		for(int i=1; i<=n; i++) {
			sum += i;
		}
		return sum;
	}
	
	// 재귀함수는  결국 스택이다. 나중에 들어간 데이터가 먼저나옴. 
	// 입력 n이 커질수록 재귀알고리즘은 반복처리문에 비해 비효율적일 수 있다. 
	
	// 재귀함수로 sum 구현 -> n + (n-1) + (n-2) + ... + 1
	// 재귀함수 사용시 주의사항: 언제 return되는지 명확하게 입력해야한다. 
	public static int sum2(int n) {
		if(n==1) return 1; // n=1이면 종료 
		return n + sum2(n-1); // 나자신을 호출하는 재귀호출 
	}
	
	// 재귀함수로 팩토리얼 구현 -> n * (n-1) * (n-2) * ... * 1
	public static int factorial(int n) {
		if(n==1) return 1; // n=1이면 종료 
		return n * factorial(n-1); // 나자신을 호출하는 재귀호출 
		}
	
	//재귀함수 이용해 x와 y의 최대공약수 구하는 프로그램 
	public static int gcm(int x, int y) {
		if(y == 0) return x;
		return gcm(y, x % y);
	}
}

```
`#java`

## 설명   
먼저, 1부터 100까지의 합을 구하는 프로그램을 sum1과 sum2 함수로 표현했다. sum1은 for문을 이용한 것이고, sum2는 재귀함수를 사용했다.
재귀함수는 언제 return되는지 명확하게 입력하는것이 가장 중요하다!
```java
public static int sum2(int n) {
		if(n==1) return 1; 
		return n + sum2(n-1);  
	}
```
=> 이렇게 sum2메소드 안에서 sum2(n-1)를 호출한것 처럼 자기자신을 호출하는 것을 재귀함수라고 한다. 
만약, n=5를 넣어준다면 가장 처음엔 5 + sum2(4)가 찍히면서 sum2(4)가 호출될 것이다. 
이런식으로 5 + sum2(4) + 4 + sum2(3) + 3 + sum2(2) + 2 + sum2(1) (1반환) = 15가 출력될 것이다. 

마찬가지로 n을 입력하면 n-1를 하면서 n+(n-1)+(n-2)+...+1 까지 더해내려갈 것이다.   

재귀함수를 이용해 팩토리얼과 최대공약수 구하는 프로그램도 작성해보았다. 
최대공약수도 재귀함수를 사용하니 훨씬 간단하게 구현할 수 있었다. 
처음엔 어렵게 느껴졌는데 직접 그려가면서 이해하니까 쉬웠다. 
