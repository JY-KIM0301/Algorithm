import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static char[][] arr;
	
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		arr = new char[n][n]; 
		
		f(0, 0, n, false);
		
		StringBuilder sb = new StringBuilder();
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				sb.append(arr[i][j]);
			}
			sb.append('\n');
		}
		System.out.println(sb);
	}
	
	public static void f(int x, int y, int n, boolean blank) {
		
		// 공백인 경우 
		if(blank) {
			for(int i=x; i<x+n; i++) {
				for(int j=y; j<y+n; j++) {
					arr[i][j] = ' ';
				}
			}
			return;
		}
		
		// n=1인 경우 (더이상 블록을 쪼갤수없음)
		if(n == 1) {
			arr[x][y] = '*'; // 크기가 1인 블록에 모두 *이 찍힌다
			return;
		}
		
		int size = n / 3;
		int idx = 0;
		for(int i=x; i<x+n; i+=size) {
			for(int j=y; j<y+n; j+=size) {
				idx++;
				if(idx == 5) { // 공백칸인 경우
					f(i, j, size, true);
				} else {
					f(i, j, size, false);
				}
			}
		}
	}
}
