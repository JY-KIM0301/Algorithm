package Recursion;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		System.out.println(f(n));
		
	}
	
	public static int f(int n) {
		if(n >= 2) {
			return f(n-1) + f(n-2);	
		}
		return n;
		
	}
}
