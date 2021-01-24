package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/*백준 2108번: 통계 알고리즘
산술평균, 중앙값, 최빈값, 범위를 구하는 프로그램을 작성하세요*/

public class Main {
	public static void main(String[] args) throws IOException{

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		double[] arr = new double[N];
		double sum = 0;

		
		for(int i = 0; i < N; i++) {
			int input = Integer.parseInt(br.readLine());
			arr[i] = input;
			sum += input;
		}
		
		// 1.산술평균
		System.out.println((int)Math.round(sum / N));
		
		// 2.중앙값
		Arrays.sort(arr);
		System.out.println((int)arr[N/2]);
		
		// 3.최빈값 -- 제일어렵...
		int[] freq = new int[8001];
		for(double d : arr) freq[(int)d+4000]++; // 빈도수 입력
		int maxFrequency = 0; // 최대 빈도값
		int maxIndex = 0; // 최대 빈도값을 가진 인덱스
		for(int i=0; i<8001; i++) {
			if(freq[i] > maxFrequency) {
				maxFrequency = freq[i];
			}
		}
		boolean twice = false; // 두번째인지 구별하기 
		
		for (int i = 0; i < 8001; i++){ 
			if ( freq[i] == maxFrequency ) { // 최빈값인 경우
				if (twice){ 
					maxIndex = i - 4000; 
					break; 
					} 
				maxIndex = i - 4000; 
				twice = true; // 플래그 세우기 
			}
		}
		System.out.println(N==1 ? (int)arr[0] : maxIndex);
		
		// 4.범위
		int result = (int)(arr[N-1] - arr[0]);
		System.out.println(result);
	}

}

/* input
5 
1 
3 
8 
-2 
2
 */

/* output 
2
2
1
10
 */
