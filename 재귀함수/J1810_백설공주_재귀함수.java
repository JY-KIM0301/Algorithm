package test;

import java.util.Scanner;

/*정올 1810: 백설공주 
일곱난장이는 일하러 가고 백설공주는 7명분의 식사를 준비한다.
그런데 어느 날 9명의 난장이가 왔고, 2명의 난장이는 가족이 아니므로 골라내야 한다.
난장이들은 모자에 번호를 써서 다니는데 백설공주의 일곱난장이들의 번호의 합은 정확히 100이었다. 
따라서 9명의 난장이들 중에 모자에 적힌 번호의 합이 100이 되는 7명을 고르면 되는 것이다.
공주를 도와 7명을 고르는 프로그램을 작성해보자.*/

public class J1810_백설공주_재귀함수 {

	static int[] c = new int[9];
	static int[] a = new int[7];
	static int size = c.length;
	static boolean[] v = new boolean[size];
	
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);

		for (int i = 0; i < size; i++) {
			c[i] = sc.nextInt();
		}
		f(0, 0, 0); //재귀함수 호출 
		sc.close();
		sc = null;
	}
	
	public static void f(int idx, int cnt, int sum) { 
		if(idx == 9) return;
		
		if(sum > 100) return;
		if(cnt==7 && sum==100) {
			for(int i=0; i<size; i++) {
				if(v[i]) System.out.println(c[i]);
			}
			System.exit(0); //App 완전 종료 -> 이 조건문의 값이 유일하기 때문에. 
		}
		if(cnt==7 || idx==9) return; 
		
		v[idx] = true;
		f(idx+1, cnt+1, sum+c[idx]);
		
		v[idx] = false;
		f(idx+1, cnt, sum);
	}
}

/* 입력데이터 
7
8
10
13
15
19
20
23
25
*/

/* 출력데이터
7
8
10
13
19
20
23
*/
