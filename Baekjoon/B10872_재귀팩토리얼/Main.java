import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//백준 10872: 재귀 팩토리얼 

public class Main {
	
	public static void main(String[] args) throws IOException {
		//Scanner sc = new Scanner(System.in);
		//n = sc.nextInt();
		//sc.close();
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		int result = f(n);
		System.out.println(result);
	}
	
	public static int f(int n) {
		if(n <= 1) return 1;
		return n * f(n-1);
	}
}
