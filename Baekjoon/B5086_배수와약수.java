package boj;

import java.util.Scanner;

// 백준 5086: 배수와 약수 
//각 테스트 케이스마다 첫 번째 숫자가 두 번째 숫자의 약수라면 factor를, 배수라면 multiple을, 둘 다 아니라면 neither를 출력한다.

public class B5086_배수와약수{
	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		
		for(int i=0; i<10000; i++) {
			int A = sc.nextInt();
			int B = sc.nextInt();
		if(B == A) break;
		if(B % A == 0) {
			System.out.println("factor");
		}
		else if(A % B == 0) {
			System.out.println("multiple");
		}
		else System.out.println("neither");
		}
	}
	
}
