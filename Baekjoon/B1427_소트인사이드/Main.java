package boj;

// 백준 1427: 소트인사이드

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		char arr[] = br.readLine().toCharArray(); // toCharArray() -> 문자 배열을 문자열로 전환
		Arrays.sort(arr);
		
		for(int i=arr.length-1; i>=0; i--) {
			System.out.print(arr[i]);
		}
		
	}

}

/*
 * 입력 2143
 * 
 * 출력 4321
 */