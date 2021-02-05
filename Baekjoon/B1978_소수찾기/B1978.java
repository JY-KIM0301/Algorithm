package boj;

import java.util.Scanner;

//백준1978: 소수찾기 

public class B1978 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int count = 0;
		
		// 수가 수를 나누기 위해서는 그 몫이 항상 필요하며 나누는 수와 몫 중 어느 하나는 반드시 sqrt(n) 이하의 수 
		for(int i=0; i<N; i++) {
			
			// 소수이면 true, 아니면 false
			boolean isPrime = true;
			
			int num = sc.nextInt();
			
			if(num == 1) {
				continue;
			}
			for(int j=2; j<=Math.sqrt(num); j++) {
				if(num % j == 0) {
					isPrime = false;
					break;
				}
			}
			if(isPrime) {
				count++;
			}
		}
		System.out.println(count);
	}

}


/*
 4 
 1 3 5 7
 
 3
 */