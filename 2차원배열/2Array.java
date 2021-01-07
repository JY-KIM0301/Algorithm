package day01;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Solution0 {
	static int t, r, c;
	static char[][] arr;

	public static void main(String[] args) throws Exception{
		// Scanner sc = new Scanner(System.in); //스캐너 
		
		// BufferedReader -> 이게 성능 더좋아!!! 
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));  

		t=Integer.parseInt(br.readLine());
		String[] read = br.readLine().split(" ");
		r=Integer.parseInt(br.readLine());
		c=Integer.parseInt(br.readLine());
		
		arr = new char[r][c];
		
		for(int i = 0; i < r; i++) {
			String msg = br.readLine(); // nextLine() 썼더니 첫번째줄의 엔터를 읽어 첫째줄이 빈공간이 출력됐다. 
			for(int j=0; j<msg.length(); j++) //한글자씩 뽑자
			{
				arr[i][j] = msg.charAt(j);
			}
		}
		System.out.printf("%d%n%d %d%n", t, r, c);
		for(int i=0; i< r; i++) {
			for (int j=0; j<c; j++) {
				System.out.printf("%c", arr[i][j]);
			}
			System.out.println();
		}
	}
}

/*
input
10
5 10
0000000000
0123456789
0000000000
0000000000
0000000000
*/
