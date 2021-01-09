//재귀함수로 부분집합 구하는 프로그램 만들기 

public class Main {
	static int[] arr = {3, 5, 7};
	static int N = arr.length;
	static boolean[] v = new boolean[N];
	
	public static void main(String[] args) {
		// 부분집합 개수는?
		System.out.println("부분집합 수: "+ (1<<N));
		f(0,0);
	}	
	
	public static void f(int idx, int cnt) { // (부분집합 구현부, 원소개수 카운팅부)
		if(idx == N) {
			for(int i=0; i<N; i++) {
				if(v[i]) System.out.print(arr[i] + " ");
			}
			System.out.println("==> 원소의 개수: " + cnt);
			return;
		}
		
		v[idx] = true; // idx자리에 원소가 들어있다면 (O라면)
		f(idx+1, cnt+1); // f호출: idx한칸 옆으로, cnt도 하나 증가
		v[idx] = false; // X인경우
		f(idx+1, cnt); // X여도 다음 원소탐색하러 idx는 한칸이동, cnt는 그대로 (개수는 증가안함)
	}
}
