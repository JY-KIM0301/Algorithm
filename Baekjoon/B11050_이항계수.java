package boj;

import java.util.Scanner;

/*백준 11050: 이항 계수
자연수 N과 정수 K가 주어질때, 이항계수를 구하는 프로그램
https://www.acmicpc.net/problem/11050
*/
public class B11050_이항계수 {
	public static void main(String[] args) {
	
		Scanner sc= new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		
		int result = factorial(N) / (factorial(K) * factorial(N-K));
		System.out.println(result);
	}
	
	//팩토리얼 함수 
	static int factorial(int n) {
		if(n <= 1) return 1;
		return n * factorial(n-1);
	}
	
}

// 재귀함수를 활용해 팩토리얼 메소드를 만들고, 이항계수 구하는 공식에 사용하는 간단한 문제