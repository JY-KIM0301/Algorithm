package boj;

import java.util.Scanner;

public class B2231 {
	public static void main(String[] args) {
		// 입력받을 자연수 N, 생성자를 저장할 result 선언 및 초기화
		Scanner sc= new Scanner(System.in);
		int N = sc.nextInt();
		int result = 0;
		
		for(int i=0; i<N; i++) {
			int number = i;
			int sum = 0; // 각 자리수의 합을 저장할 변수, sum
			
			while(number != 0) {
				sum += number % 10; // number가 0이 아닌 경우만 각 자리수 더하기 
				number /= 10;
			}
			
			// i값과 각 자리수의 합이 같다 -> 생성자 발견
			if(sum + i == N) {
				result = i;
				break; // 종료 
			}
			
		}
		System.out.println(result);
		
	}
}
