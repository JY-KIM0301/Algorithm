# 백준 2675: 문자열 반복
https://www.acmicpc.net/problem/2675 

## 문제
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.
QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다.

**예제 입력**
```
2
3 ABC
5 /HTP
```

**예제 출력**
```
AAABBBCCC
/////HHHHHTTTTTPPPPP
```

## 풀이 코드

``` java
import java.util.Scanner;

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
```
`#java`

**설명**
문자열에서 각 문자를 뽑아내기 위해 charAt() 메소드를 사용해야한다. 각 문자들이 r만큼 반복하면 종료된다. 
특정 문자를 뽑아낼수 있는지 묻는 간단한 예제였다. 
