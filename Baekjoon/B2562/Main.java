import java.util.Scanner;

/*9개의 서로다른 자연수가 있다. 
최댓값을 구하고, 그 최댓값이 몇번째수인지 구하는 프로그램.
*/

public class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		int[] array = new int[9];
		for(int i=0; i<9; i++) {
			array[i] = sc.nextInt();
		}
		
		int max = 0;
		int index = 0;
		
		for(int i=0; i<9; i++) {
			if(array[i] > max) {
				max = array[i];
				index = i+1;
			}
		}
		System.out.println(max);
		System.out.println(index);
	}
}
