package boj;

import java.util.Scanner;

/*
백준 3036: 링
링들의 반지름이 주어질때, 첫번째 링을 한바퀴 돌리면 나머지 링들은 몇바퀴 도는지 구하는 프로그램
출력결과를 기약분수로 나타내고싶다면 분모와 분자의 최대공약수로 나눠주면 된다 
*/

public class B3036 {
	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		int N = sc.nextInt(); // 링의 개수 입력
		
		// 첫번째 링
		int firstRing = sc.nextInt();
		for(int i=1; i<N; i++) {
			int otherRing = sc.nextInt();
			
			// 최대공약수 구하기
			int gcdResult = gcd(firstRing, otherRing);
			
			// 분모와 분자를 각각 최대공약수로 나누어 출력하기 
			System.out.println((firstRing / gcdResult) + "/" + (otherRing / gcdResult));
		}
		
	}
	
	// 최대공약수 함수
	static int gcd(int a, int b) {
		int r;
		
		while(b != 0) {
			r = a % b;
			a = b;
			b = r;
		}
		return a;
	}
}

