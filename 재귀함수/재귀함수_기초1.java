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

