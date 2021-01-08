import java.util.Scanner;

//각 문자를 R번 반복해서 새 문자열 P를 만드는 프로그램

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		for(int i=0; i<num; i++) {
		
			int r = sc.nextInt();
			String s = sc.next();
			
			for(int j=0; j<s.length(); j++) {
				for(int k=0; k<r; k++) {
					System.out.print(s.charAt(j));
				}
			}
		System.out.println();
		}

	}
}
