package boj;

import java.util.Scanner;

/*100이상 1000이하인 3개의 자연수를 모두 곱한 결과값에서
0부터 9까지 각각의 숫자가 몇번씩 쓰였는지 구하는 프로그램
*/

public class B2577 {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		int value = sc.nextInt() * sc.nextInt() * sc.nextInt(); // 세개 자연수 입력 합
		String str = Integer.toString(value); // 곲한 결과값을 String으로 변환
		sc.close();
		
		for(int i=0; i<10; i++) {
			int count = 0;
			for(int j=0; j<str.length(); j++) {
				if((str.charAt(j) - '0') == i) // charAt(j) - '0' 또는 -48
					count++;
			}
			System.out.println(count);
		}
	}
}
